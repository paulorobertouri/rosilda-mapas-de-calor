import os

import Config as config
import pandas as pd
import Utils as utils


def main() -> None:
    utils.create_output_directory(config.OUTPUT_DIR)

    data = {
        "Empresa": ["ÂNIMA", "COGNA", "YDUQS", "SER", "CRUZEIRO DO SUL", "VITRU"],
        "SUL": [5, 4, 3, 2, 4, 2],
        "SUDESTE": [14, 2, 9, 6, 7, 0],
        "CENTRO-OESTE": [2, 6, 0, 0, 1, 0],
        "NORTE": [0, 1, 5, 8, 0, 0],
        "NORDESTE": [8, 3, 10, 11, 1, 0],
    }

    base_df = pd.DataFrame(data)
    geojson = utils.load_geojson(config.GEOJSON_URL)
    geojson = utils.map_regions(geojson, config.COLUMN_NAME, config.REGION_MAPPING)

    for _, row in base_df.iterrows():
        company_name = str(row["Empresa"])
        # Extract values for the regions in the order defined in config.REGIONS
        region_values = [int(row[region]) for region in config.REGIONS]

        output_path = os.path.join(config.OUTPUT_DIR, f"{company_name.lower()}.png")
        print(f"Generating heatmap for {company_name}...")
        utils.plot_heatmap(geojson, company_name, region_values, output_path)


if __name__ == "__main__":
    main()
