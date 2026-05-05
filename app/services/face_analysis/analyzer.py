from collections.abc import Iterator
from pathlib import Path

from app.services.face_analysis.clustering import FaceClusterer
from app.services.face_analysis.detector import InsightFaceDetector
from app.services.face_analysis.models import (
    ClusteredFaceDetection,
    FaceDetection,
    VideoFrame,
)
from app.services.face_analysis.video_reader import VideoFrameReader


class FaceVideoAnalyzer:
    def __init__(
        self,
        frame_reader: VideoFrameReader | None = None,
        detector: InsightFaceDetector | None = None,
        clusterer: FaceClusterer | None = None,
    ):
        self.frame_reader = frame_reader or VideoFrameReader()
        self.detector = detector or InsightFaceDetector()
        self.clusterer = clusterer or FaceClusterer()

    def read_sampled_frames(self, video_path: str | Path) -> Iterator[VideoFrame]:
        return self.frame_reader.read_frames(video_path)

    def detect_faces(self, video_path: str | Path) -> Iterator[FaceDetection]:
        for video_frame in self.frame_reader.read_frames(video_path):
            yield from self.detector.detect(video_frame)

    def cluster_faces(self, video_path: str | Path) -> Iterator[ClusteredFaceDetection]:
        for detection in self.detect_faces(video_path):
            yield self.clusterer.assign(detection)
