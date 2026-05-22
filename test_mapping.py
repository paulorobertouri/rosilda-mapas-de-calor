import pandas as pd
import pytest
import config
from empresas import map_regions

def test_region_mapping():
    # Create a mock GeoDataFrame
    data = {'name': ['Paraná', 'São Paulo', 'Goiás', 'Amazonas', 'Bahia', 'Unknown']}
    geo_df = pd.DataFrame(data)
    
    # Apply mapping
    result_df = map_regions(geo_df, config.COLUMN_NAME, config.REGION_MAPPING)
    
    # Verify results
    assert result_df.iloc[0][config.REGION_LABEL] == 'SUL'
    assert result_df.iloc[1][config.REGION_LABEL] == 'SUDESTE'
    assert result_df.iloc[2][config.REGION_LABEL] == 'CENTRO-OESTE'
    assert result_df.iloc[3][config.REGION_LABEL] == 'NORTE'
    assert result_df.iloc[4][config.REGION_LABEL] == 'NORDESTE'
    assert pd.isna(result_df.iloc[5][config.REGION_LABEL])
