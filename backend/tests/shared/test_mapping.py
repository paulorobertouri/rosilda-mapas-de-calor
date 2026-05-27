import sys
from pathlib import Path

import pandas as pd
from _pytest.monkeypatch import MonkeyPatch

MAPPING_DIR = Path(__file__).resolve().parents[1] / "src" / "mapping"
sys.path.insert(0, str(MAPPING_DIR))

import Config as config  # noqa: E402
import Empresas as empresas  # noqa: E402
import Geral as geral  # noqa: E402
import Utils as utils  # noqa: E402


def test_region_mapping() -> None:
    data = {
        "name": ["Paraná", "São Paulo", "Goiás", "Amazonas", "Bahia", "Unknown"],
    }
    geo_df = pd.DataFrame(data)

    result_df = utils.map_regions(geo_df, config.COLUMN_NAME, config.REGION_MAPPING)

    assert result_df.iloc[0][config.REGION_LABEL] == "SUL"
    assert result_df.iloc[1][config.REGION_LABEL] == "SUDESTE"
    assert result_df.iloc[2][config.REGION_LABEL] == "CENTRO-OESTE"
    assert result_df.iloc[3][config.REGION_LABEL] == "NORTE"
    assert result_df.iloc[4][config.REGION_LABEL] == "NORDESTE"
    assert pd.isna(result_df.iloc[5][config.REGION_LABEL])


def test_create_output_directory(tmp_path: Path) -> None:
    output_dir = tmp_path / "maps"
    assert not output_dir.exists()

    utils.create_output_directory(str(output_dir))

    assert output_dir.exists()
    assert output_dir.is_dir()


def test_empresas_main_generates_expected_output_paths(
    monkeypatch: MonkeyPatch, tmp_path: Path
) -> None:
    captured_paths: list[str] = []

    def fake_create_output_directory(_: str) -> None:
        return None

    def fake_load_geojson(_: str) -> pd.DataFrame:
        return pd.DataFrame({config.COLUMN_NAME: ["Paraná"]})

    def fake_map_regions(
        geo_df: pd.DataFrame, _: str, __: dict[str, str]
    ) -> pd.DataFrame:
        geo_df[config.REGION_LABEL] = "SUL"
        return geo_df

    def fake_plot_heatmap(
        _: pd.DataFrame, __: str, ___: list[int], output_path: str
    ) -> None:
        captured_paths.append(output_path)

    monkeypatch.setattr(empresas.config, "OUTPUT_DIR", str(tmp_path))
    monkeypatch.setattr(
        empresas.utils,
        "create_output_directory",
        fake_create_output_directory,
    )
    monkeypatch.setattr(empresas.utils, "load_geojson", fake_load_geojson)
    monkeypatch.setattr(empresas.utils, "map_regions", fake_map_regions)
    monkeypatch.setattr(empresas.utils, "plot_heatmap", fake_plot_heatmap)

    empresas.main()

    assert len(captured_paths) == 6
    assert {Path(path).name for path in captured_paths} == {
        "cogna.png",
        "cruzeiro do sul.png",
        "ser.png",
        "vitru.png",
        "yduqs.png",
        "\u00e2nima.png",
    }
    assert all(Path(path).parent == tmp_path for path in captured_paths)


def test_geral_main_uses_expected_output_path(
    monkeypatch: MonkeyPatch, tmp_path: Path
) -> None:
    captured_paths: list[str] = []

    def fake_create_output_directory(_: str) -> None:
        return None

    def fake_load_geojson(_: str) -> pd.DataFrame:
        return pd.DataFrame({config.COLUMN_NAME: ["Paraná"]})

    def fake_map_regions(
        geo_df: pd.DataFrame, _: str, __: dict[str, str]
    ) -> pd.DataFrame:
        geo_df[config.REGION_LABEL] = "SUL"
        return geo_df

    def fake_plot_heatmap(
        _: pd.DataFrame, __: str, ___: list[int], output_path: str
    ) -> None:
        captured_paths.append(output_path)

    monkeypatch.setattr(geral.config, "OUTPUT_DIR", str(tmp_path))
    monkeypatch.setattr(
        geral.utils,
        "create_output_directory",
        fake_create_output_directory,
    )
    monkeypatch.setattr(geral.utils, "load_geojson", fake_load_geojson)
    monkeypatch.setattr(geral.utils, "map_regions", fake_map_regions)
    monkeypatch.setattr(geral.utils, "plot_heatmap", fake_plot_heatmap)

    geral.main()

    assert captured_paths == [str(tmp_path / "geral.png")]
