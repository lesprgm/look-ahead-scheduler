from dataclasses import dataclass
from enum import Enum
from typing import Callable


class Mode(str, Enum):
    FIFO = "fifo"
    PREDICTIVE = "predictive"
    MLFQ = "mlfq"


@dataclass(frozen=True)
class Task:
    id: int
    type: str
    dependencies: tuple[int, ...]
    run: Callable[[], None]
