from collections.abc import Iterator
from pathlib import Path

from app.services.face_analysis.models import VideoFrame
from app.services.face_analysis.video_reader import VideoFrameReader


class FaceVideoAnalyzer:
    def __init__(self, frame_reader: VideoFrameReader | None = None):
        self.frame_reader = frame_reader or VideoFrameReader()

    def read_sampled_frames(self, video_path: str | Path) -> Iterator[VideoFrame]:
        return self.frame_reader.read_frames(video_path)