import sys
from pathlib import Path

import pandas as pd
from _pytest.monkeypatch import MonkeyPatch

SRC_DIR = Path(__file__).resolve().parents[3] / "src" / "shared" / "mapping"
sys.path.insert(0, str(SRC_DIR))

import Config as config  # noqa: E402
import Geral as geral  # noqa: E402


def test_main_generates_geral_png(monkeypatch: MonkeyPatch, tmp_path: Path) -> None:
    captured_paths: list[str] = []

    monkeypatch.setattr(geral.config, "OUTPUT_DIR", str(tmp_path))
    monkeypatch.setattr(geral.utils, "create_output_directory", lambda _: None)
    monkeypatch.setattr(
        geral.utils,
        "load_geojson",
        lambda _: pd.DataFrame({config.COLUMN_NAME: ["Paraná"]}),
    )
    monkeypatch.setattr(
        geral.utils,
        "map_regions",
        lambda df, _, __: df.assign(**{config.REGION_LABEL: "SUL"}),
    )
    monkeypatch.setattr(
        geral.utils,
        "plot_heatmap",
        lambda _, __, ___, output_path: captured_paths.append(output_path),
    )

    geral.main()

    assert captured_paths == [str(tmp_path / "geral.png")]
