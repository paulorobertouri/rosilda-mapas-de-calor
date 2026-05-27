import os
from typing import Any

import Config as config
import pandas as pd


def create_output_directory(directory: str) -> None:
    """Creates the output directory if it doesn't exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)


def load_geojson(url: str) -> Any:
    """Loads GeoJSON data from a URL."""
    import geopandas as gpd

    return gpd.read_file(url)  # type: ignore


def map_regions(
    geo_df: pd.DataFrame,
    column_name: str,
    region_mapping: dict[str, str],
) -> pd.DataFrame:
    """Maps states to regions in the GeoDataFrame."""
    geo_df[config.REGION_LABEL] = geo_df[column_name].map(region_mapping)
    return geo_df


def plot_heatmap(
    geo_df: pd.DataFrame,
    title: str,
    region_data: list[int],
    output_path: str,
) -> None:
    """Plots and saves a heatmap."""
    import matplotlib.pyplot as plt

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
    plt.title(title)
    plt.axis("off")
    plt.savefig(output_path, dpi=900)
    plt.close()
