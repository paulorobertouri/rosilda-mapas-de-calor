# Rosilda - Mapas de Calor

A Python-based tool for generating heat maps of higher education institutions in Brazil. This project analyzes data from major educational groups such as Ânima, Cogna, Cruzeiro do Sul, Ser Educacional, Vitru, and Yduqs for the year 2024.

## Features

- **Data Visualization**: Generates heat maps across different regions of Brazil.
- **Group Analysis**: Specific heat maps for major educational conglomerates.
- **Automated Processing**: Scripts to process raw data and output visual maps.

## Architecture

The project is structured as a collection of Python scripts:
- `geral.py`: Generates the general heat map for all institutions.
- `empresas.py`: Generates individual heat maps for specific educational groups.
- `config.py`: Configuration and data paths.
- `utils.py`: Shared utility functions for map generation.

## Setup

It is recommended to use a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Alternatively, using `uv`:
```bash
uv sync
```

## Run

To generate the general heat map:
```bash
python geral.py
```

To generate specific maps for each group:
```bash
python empresas.py
```

## Testing

Run tests to verify mapping logic:
```bash
pytest test_mapping.py
```
