from dataclasses import FrozenInstanceError, replace
from pathlib import Path

import pytest

from docsync.models.code_chunk import ChunkType, CodeChunk


@pytest.fixture
def sample_chunk() -> CodeChunk:
    return CodeChunk(
        id="example.py:calculate_total",
        file_path=Path("example.py"),
        name="calculate_total",
        qualified_name="calculate_total",
        chunk_type=ChunkType.FUNCTION,
        source_code="def calculate_total(a, b):\n    return a + b",
        start_line=1,
        end_line=2,
    )


def test_code_chunk_creation(sample_chunk: CodeChunk) -> None:
    assert sample_chunk.id == "example.py:calculate_total"
    assert sample_chunk.file_path == Path("example.py")
    assert sample_chunk.name == "calculate_total"
    assert sample_chunk.qualified_name == "calculate_total"
    assert sample_chunk.chunk_type == ChunkType.FUNCTION
    assert sample_chunk.source_code == ("def calculate_total(a, b):\n    return a + b")
    assert sample_chunk.start_line == 1
    assert sample_chunk.end_line == 2


def test_docstring_defaults_to_none(sample_chunk: CodeChunk) -> None:
    assert sample_chunk.docstring is None


def test_code_chunk_accepts_docstring(sample_chunk: CodeChunk) -> None:
    chunk = replace(sample_chunk, docstring="Calculate the total.")

    assert chunk.docstring == "Calculate the total."


def test_code_chunk_is_immutable(sample_chunk: CodeChunk) -> None:
    with pytest.raises(FrozenInstanceError):
        sample_chunk.name = "modified_name"


def test_equal_chunks_have_equal_hashes(sample_chunk: CodeChunk) -> None:
    identical_chunk = replace(sample_chunk)

    assert identical_chunk == sample_chunk
    assert hash(identical_chunk) == hash(sample_chunk)


def test_different_chunks_are_not_equal(sample_chunk: CodeChunk) -> None:
    different_chunk = replace(sample_chunk, name="another_function")

    assert different_chunk != sample_chunk
