# Shared configuration and constants for heatmap generation

OUTPUT_DIR = ".outputs"
GEOJSON_URL = "https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson"
COLUMN_NAME = "name"
REGION_LABEL = "Região"

REGIONS = [
    "SUL",
    "SUDESTE",
    "CENTRO-OESTE",
    "NORTE",
    "NORDESTE",
]

REGION_MAPPING = {
    "Paraná": "SUL",
    "Santa Catarina": "SUL",
    "Rio Grande do Sul": "SUL",
    "São Paulo": "SUDESTE",
    "Rio de Janeiro": "SUDESTE",
    "Espírito Santo": "SUDESTE",
    "Minas Gerais": "SUDESTE",
    "Goiás": "CENTRO-OESTE",
    "Mato Grosso": "CENTRO-OESTE",
    "Mato Grosso do Sul": "CENTRO-OESTE",
    "Acre": "NORTE",
    "Amazonas": "NORTE",
    "Roraima": "NORTE",
    "Amapá": "NORTE",
    "Rondônia": "NORTE",
    "Pará": "NORTE",
    "Tocantins": "NORTE",
    "Bahia": "NORDESTE",
    "Sergipe": "NORDESTE",
    "Alagoas": "NORDESTE",
    "Pernambuco": "NORDESTE",
    "Paraíba": "NORDESTE",
    "Rio Grande do Norte": "NORDESTE",
    "Ceará": "NORDESTE",
    "Piauí": "NORDESTE",
    "Maranhão": "NORDESTE",
}
