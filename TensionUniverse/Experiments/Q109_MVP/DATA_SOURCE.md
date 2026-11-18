# Data Source Information: Q109 Migration Dynamics

This experiment uses **real-world external data** to evaluate Semantic Tension (ΔS) across international borders.

## Primary Dataset
- **Provider**: World Bank Open Data
- **Indicator**: Net Migration (`SM.POP.NETM`)
- **License**: Creative Commons Attribution 4.0 International (CC BY 4.0)
- **API Endpoint**: `https://api.worldbank.org/v2/country/all/indicator/SM.POP.NETM?format=json`

## Why we use dynamic API instead of flat CSV
In alignment with WFGY's philosophy of handling "living" tension patterns:
1. **No Static Bloat**: We avoid committing large, static `.csv` files into the repository to keep the core lightweight.
2. **Real-time Relevancy**: By using `urllib`/`requests` to fetch standard JSON from the API, the notebook automatically adapts to the latest global demographic dividend reports without requiring manual updates.

## Fallback Mechanism
If the World Bank API is inaccessible due to firewall or network restrictions during the notebook execution, users can manually download the CSV from [World Bank Data Catalog](https://data.worldbank.org/indicator/SM.POP.NETM) and feed it into the pandas dataframe.
