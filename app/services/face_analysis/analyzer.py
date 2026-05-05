from collections.abc import Iterator
from pathlib import Path

from app.services.face_analysis.clustering import FaceClusterer
from app.services.face_analysis.detector import InsightFaceDetector
from app.services.face_analysis.models import (
    FaceAnalysisResult,
    FaceAppearance,
    ClusteredFaceDetection,
    FaceDetection,
    VideoFrame,
)
from app.services.face_analysis.timeline import AppearanceTimelineBuilder
from app.services.face_analysis.video_reader import VideoFrameReader


class FaceVideoAnalyzer:
    def __init__(
        self,
        frame_reader: VideoFrameReader | None = None,
        detector: InsightFaceDetector | None = None,
        clusterer: FaceClusterer | None = None,
        timeline_builder: AppearanceTimelineBuilder | None = None,
    ):
        self.frame_reader = frame_reader or VideoFrameReader()
        self.detector = detector or InsightFaceDetector()
        self.clusterer = clusterer or FaceClusterer()
        self.timeline_builder = timeline_builder or AppearanceTimelineBuilder()

    def read_sampled_frames(self, video_path: str | Path) -> Iterator[VideoFrame]:
        return self.frame_reader.read_frames(video_path)

    def detect_faces(self, video_path: str | Path) -> Iterator[FaceDetection]:
        for video_frame in self.frame_reader.read_frames(video_path):
            yield from self.detector.detect(video_frame)

    def cluster_faces(self, video_path: str | Path) -> Iterator[ClusteredFaceDetection]:
        for detection in self.detect_faces(video_path):
            yield self.clusterer.assign(detection)

    def build_timeline(self, video_path: str | Path) -> list[FaceAppearance]:
        timeline_builder = AppearanceTimelineBuilder()
        clusterer = FaceClusterer()  # 🔥 이것도 같이 초기화하는 게 중요

        for detection in self.detect_faces(video_path):
            clustered = clusterer.assign(detection)
            timeline_builder.add(clustered)

        return timeline_builder.build()

    def analyze(self, video_path: str | Path) -> FaceAnalysisResult:
        path = Path(video_path)
        appearances = self.build_timeline(path)
        return FaceAnalysisResult(
            video_path=str(path),
            appearances=appearances,
        )
