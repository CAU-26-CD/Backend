from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class VideoFrame:
    timestamp_seconds: float
    frame_index: int
    frame: Any


@dataclass(frozen=True)
class FaceDetection:
    timestamp_seconds: float
    frame_index: int
    bbox: tuple[float, float, float, float]
    embedding: list[float]
    confidence: float
