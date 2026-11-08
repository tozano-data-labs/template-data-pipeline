from pathlib import Path

import pytest

from pipeline.main import read_csv, run


def test_run_copies_rows(tmp_path: Path):
    source = tmp_path / "source.csv"
    source.write_text("id,value\n1,a\n2,b\n", encoding="utf-8")
    output = tmp_path / "out" / "result.csv"

    assert run(source, output) == 2
    assert read_csv(output) == [{"id": "1", "value": "a"}, {"id": "2", "value": "b"}]


def test_run_rejects_empty_input(tmp_path: Path):
    source = tmp_path / "empty.csv"
    source.write_text("id,value\n", encoding="utf-8")

    with pytest.raises(ValueError, match="vide"):
        run(source, tmp_path / "out.csv")
