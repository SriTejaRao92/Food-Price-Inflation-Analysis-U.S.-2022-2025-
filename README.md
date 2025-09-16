# Food-Price-Inflation-Analysis-U.S.-2022-2025-
## Description
Pulled BLS food price data via API, transformed it in Databricks Free Edition using Unity Catalog, calculated monthly/annual inflation, and visualized trends with Databricks Virtual Assistant for actionable insights.

## Project Structure
- `bls_to_local.py` – Extracts U.S. food price data from the BLS API and saves it as JSON.
- `food_price_inflation_analysis.ipynb` – Performs all transformations, calculates monthly and yearly price changes, and generates visualizations for insights.

## Key Steps
1. **Data Extraction** – Used `bls_to_local.py` to fetch data and save locally in JSON format.
2. **Data Loading** – Imported JSON data into Databricks Unity Catalog.
3. **Data Transformation** – Converted `year` and `period` into proper date format, calculated previous month price, monthly percentage change, yearly average price, and yearly average inflation.
4. **Visualization** – Generated charts showing monthly and yearly trends using Databricks Virtual Assistant.

## Requirements
- Databricks Free Edition (Unity Catalog)
- Python 3.11+
- PySpark
- Requests library

## Insights
- Track monthly and yearly food price inflation trends in the U.S.
- Identify months with highest inflation per category.
- Observe long-term price trends across 2022–2025.

## How to Run
1. Run `bls_to_local.py` to fetch JSON data from BLS API.
2. Open `food_price_inflation_analysis.ipynb` in Databricks Free Edition.
3. Load JSON data into Unity Catalog.
4. Execute all cells for transformations and visualizations.
