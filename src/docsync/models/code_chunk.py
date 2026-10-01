from dataclasses import dataclass
from enum import Enum
from pathlib import Path


class ChunkType(str, Enum):
    FUNCTION = "function"
    ASYNC_FUNCTION = "async_function"
    CLASS = "class"
    METHOD = "method"


@dataclass(frozen=True, slots=True)
class CodeChunk:
    id: str
    file_path: Path
    name: str
    qualified_name: str
    chunk_type: ChunkType
    source_code: str
    start_line: int
    end_line: int
    docstring: str | None = None
