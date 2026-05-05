from pathlib import Path
from dataclasses import asdict
import json
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

    def progress(
        sampled_frame_count: int,
        timestamp_seconds: float,
        detection_count: int,
    ) -> None:
        if sampled_frame_count == 1 or sampled_frame_count % 10 == 0:
            print(
                "progress",
                f"frames={sampled_frame_count}",
                f"timestamp={timestamp_seconds:.1f}s",
                f"detections={detection_count}",
                file=sys.stderr,
            )

    result = analyzer.analyze(video_path, progress_callback=progress)

    print(json.dumps(asdict(result), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
