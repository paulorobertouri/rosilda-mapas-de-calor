import os

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


def plot_heatmap(
    geo_df: gpd.GeoDataFrame,
    title: str,
    region_data: list[int],
    output_path: str,
) -> None:
    """Plots and saves a heatmap."""
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
