from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from app.services.face_analysis.analyzer import FaceVideoAnalyzer
from app.services.face_analysis.clustering import FaceClusterer
from app.services.face_analysis.timeline import AppearanceTimelineBuilder
from app.services.face_analysis.video_reader import VideoFrameReader


def main() -> None:
    if len(sys.argv) > 1:
        video_path = Path(sys.argv[1])
    else:
        video_path = PROJECT_ROOT / "uploads" / "session_7.webm"

    if not video_path.is_absolute():
        video_path = PROJECT_ROOT / video_path

    analyzer = FaceVideoAnalyzer(
        frame_reader=VideoFrameReader(frame_interval_seconds=5.0),
        clusterer=FaceClusterer(similarity_threshold=0.45),
        timeline_builder=AppearanceTimelineBuilder(max_gap_seconds=6.0),
    )
    result = analyzer.analyze(video_path)

    print("video_path", result.video_path)
    for appearance in result.appearances:
        print(
            appearance.person_id,
            appearance.start_seconds,
            appearance.end_seconds,
            "detections",
            appearance.detection_count,
        )


if __name__ == "__main__":
    main()
