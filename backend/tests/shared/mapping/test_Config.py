import sys
from pathlib import Path

SRC_DIR = Path(__file__).resolve().parents[3] / "src" / "shared" / "mapping"
sys.path.insert(0, str(SRC_DIR))

import Config as config  # noqa: E402


def test_regions_and_mapping_are_consistent() -> None:
    assert len(config.REGIONS) == 5
    assert "SUL" in config.REGIONS
    assert config.REGION_MAPPING["Paraná"] == "SUL"
    assert config.REGION_LABEL == "Região"

