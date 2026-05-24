import os

import config
import utils


def main() -> None:
    utils.create_output_directory(config.OUTPUT_DIR)
    
    data = [
        20, # SUL
        38, # SUDESTE
        9,  # CENTRO-OESTE
        14, # NORTE
        33, # NORDESTE
    ]
    
    output_file = os.path.join(config.OUTPUT_DIR, "geral.png")
    geojson = utils.load_geojson(config.GEOJSON_URL)
    geojson = utils.map_regions(geojson, config.COLUMN_NAME, config.REGION_MAPPING)

    print("Generating general heatmap...")
    utils.plot_heatmap(geojson, "BRASIL", data, output_file)


if __name__ == "__main__":
    main()
