from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class VideoFrame:
    timestamp_seconds: float
    frame_index: int
    frame: Any

