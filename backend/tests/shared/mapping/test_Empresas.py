import sys
from pathlib import Path

import pandas as pd
from _pytest.monkeypatch import MonkeyPatch

SRC_DIR = Path(__file__).resolve().parents[3] / "src" / "shared" / "mapping"
sys.path.insert(0, str(SRC_DIR))

import Config as config  # noqa: E402
import Empresas as empresas  # noqa: E402


def test_main_generates_one_file_per_company(monkeypatch: MonkeyPatch, tmp_path: Path) -> None:
    captured_paths: list[str] = []

    monkeypatch.setattr(empresas.config, "OUTPUT_DIR", str(tmp_path))
    monkeypatch.setattr(empresas.utils, "create_output_directory", lambda _: None)
    monkeypatch.setattr(
        empresas.utils,
        "load_geojson",
        lambda _: pd.DataFrame({config.COLUMN_NAME: ["Paraná"]}),
    )
    monkeypatch.setattr(
        empresas.utils,
        "map_regions",
        lambda df, _, __: df.assign(**{config.REGION_LABEL: "SUL"}),
    )
    monkeypatch.setattr(
        empresas.utils,
        "plot_heatmap",
        lambda _, __, ___, output_path: captured_paths.append(output_path),
    )

    empresas.main()

    assert len(captured_paths) == 6
    assert all(Path(path).suffix == ".png" for path in captured_paths)
    assert all(Path(path).parent == tmp_path for path in captured_paths)

