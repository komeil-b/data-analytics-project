# Operations Analytics Starter

A neutral, portfolio-ready project that demonstrates an end-to-end analytics workflow for an omni-channel retail style dataset. It includes Python data generation and cleaning, a simple SQL schema, and a Power BI dashboard outline.

## Stack
- Python for wrangling
- SQL for dimensional modeling
- Power BI for dashboards

## Quick start
1. `pip install -r requirements.txt`
2. `python src/make_dataset.py`
3. `python src/clean_transform.py`
4. Load `sql/schema.sql` into MySQL or any RDBMS and import the processed CSVs.
5. Build visuals in Power BI using `powerbi/measures_dax.md`.
