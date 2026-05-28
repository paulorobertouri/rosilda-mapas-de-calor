import sys
import types
from pathlib import Path

import pandas as pd

SRC_DIR = Path(__file__).resolve().parents[3] / "src" / "shared" / "mapping"
sys.path.insert(0, str(SRC_DIR))

import Config as config  # noqa: E402
import Utils as utils  # noqa: E402


def test_map_regions_assigns_expected_region_labels() -> None:
    df = pd.DataFrame({config.COLUMN_NAME: ["Paraná", "Amazonas", "Unknown"]})
    mapped = utils.map_regions(df, config.COLUMN_NAME, config.REGION_MAPPING)

    assert mapped.iloc[0][config.REGION_LABEL] == "SUL"
    assert mapped.iloc[1][config.REGION_LABEL] == "NORTE"
    assert pd.isna(mapped.iloc[2][config.REGION_LABEL])


def test_create_output_directory_creates_folder(tmp_path: Path) -> None:
    output_dir = tmp_path / "maps"
    utils.create_output_directory(str(output_dir))
    assert output_dir.exists()
    assert output_dir.is_dir()


def test_load_geojson_delegates_to_geopandas_read_file(monkeypatch) -> None:
    captured: dict[str, str] = {}

    fake_gpd = types.SimpleNamespace(
        read_file=lambda url: captured.setdefault("url", url) or "geojson"
    )
    monkeypatch.setitem(sys.modules, "geopandas", fake_gpd)

    result = utils.load_geojson("https://example.com/data.geojson")

    assert result == "https://example.com/data.geojson"
    assert captured["url"] == "https://example.com/data.geojson"


def test_plot_heatmap_builds_legend_and_saves(monkeypatch, tmp_path: Path) -> None:
    class FakeAx:
        def __init__(self) -> None:
            self.scatter_calls = 0
            self.legend_calls = 0

        def scatter(self, *args, **kwargs) -> None:
            self.scatter_calls += 1

        def legend(self) -> None:
            self.legend_calls += 1

    class FakeMerged:
        def plot(self, **kwargs) -> None:
            return None

    class FakeGeoDataFrame:
        def merge(self, _df, on: str) -> FakeMerged:
            assert on == config.REGION_LABEL
            return FakeMerged()

    fake_ax = FakeAx()
    captured_paths: list[str] = []

    fake_pyplot = types.SimpleNamespace()
    fake_pyplot.cm = types.SimpleNamespace(YlOrRd=lambda value: value)
    fake_pyplot.subplots = lambda *_args, **_kwargs: (None, fake_ax)
    fake_pyplot.title = lambda *_args, **_kwargs: None
    fake_pyplot.axis = lambda *_args, **_kwargs: None
    fake_pyplot.savefig = lambda output_path, **_kwargs: captured_paths.append(
        output_path
    )
    fake_pyplot.close = lambda *_args, **_kwargs: None

    monkeypatch.setitem(sys.modules, "matplotlib", types.ModuleType("matplotlib"))
    monkeypatch.setitem(sys.modules, "matplotlib.pyplot", fake_pyplot)

    utils.plot_heatmap(
        FakeGeoDataFrame(),  # type: ignore[arg-type]
        "title",
        [1, 2, 3, 4, 5],
        str(tmp_path / "map.png"),
    )

    assert fake_ax.scatter_calls == 5
    assert fake_ax.legend_calls == 1
    assert captured_paths == [str(tmp_path / "map.png")]
