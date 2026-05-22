import os
from typing import Any

import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

import config


def create_output_directory(directory: str) -> None:
    """Creates the output directory if it doesn't exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)


def load_geojson(url: str) -> gpd.GeoDataFrame:
    """Loads GeoJSON data from a URL."""
    return gpd.read_file(url)  # type: ignore


def map_regions(
    geo_df: gpd.GeoDataFrame,
    column_name: str,
    region_mapping: dict[str, str],
) -> gpd.GeoDataFrame:
    """Maps states to regions in the GeoDataFrame."""
    geo_df[config.REGION_LABEL] = geo_df[column_name].map(region_mapping)
    return geo_df


def plot_company_heatmap(
    geo_df: gpd.GeoDataFrame,
    company_name: str,
    region_data: list[int],
    output_path: str,
) -> None:
    """Plots and saves a heatmap for a specific company."""
    df = pd.DataFrame(
        {
            config.REGION_LABEL: config.REGIONS,
            "Valor": region_data,
        }
    )

    geo_df_merged = geo_df.merge(df, on=config.REGION_LABEL)

    _, ax = plt.subplots(1, 1, figsize=(10, 8))

    geo_df_merged.plot(
        column="Valor",
        cmap="YlOrRd",
        legend=False,
        ax=ax,
        edgecolor="black",
    )

    # Create custom legend
    unique_values = sorted(set(region_data))
    for value in unique_values:
        if max(unique_values) == 0:
            color = plt.cm.YlOrRd(0)
        else:
            color = plt.cm.YlOrRd(value / max(unique_values))
        ax.scatter([], [], c=[color], label=f"{value}")

    ax.legend()
    plt.title(company_name)
    plt.axis("off")
    plt.savefig(output_path, dpi=900)
    plt.close()


def main() -> None:
    create_output_directory(config.OUTPUT_DIR)
    
    data = {
        "Empresa": ["ÂNIMA", "COGNA", "YDUQS", "SER", "CRUZEIRO DO SUL", "VITRU"],
        "SUL": [5, 4, 3, 2, 4, 2],
        "SUDESTE": [14, 2, 9, 6, 7, 0],
        "CENTRO-OESTE": [2, 6, 0, 0, 1, 0],
        "NORTE": [0, 1, 5, 8, 0, 0],
        "NORDESTE": [8, 3, 10, 11, 1, 0],
    }
    
    base_df = pd.DataFrame(data)
    geojson = load_geojson(config.GEOJSON_URL)
    geojson = map_regions(geojson, config.COLUMN_NAME, config.REGION_MAPPING)

    for _, row in base_df.iterrows():
        company_name = str(row["Empresa"])
        # Extract values for the regions in the order defined in config.REGIONS
        region_values = [int(row[region]) for region in config.REGIONS]
        
        output_path = os.path.join(config.OUTPUT_DIR, f"{company_name.lower()}.png")
        print(f"Generating heatmap for {company_name}...")
        plot_company_heatmap(geojson, company_name, region_values, output_path)


if __name__ == "__main__":
    main()
