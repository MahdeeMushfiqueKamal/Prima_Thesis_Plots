# Prima Thesis Plots

Python codes for generating plots of Tasfiah Prima's Thesis

## Scripts

### `OD_graph/plot_od.py`
Generates OD600 growth curve plots per concentration condition using averaged replicates with error bars.

**Input:** `_L.lactis vs pMGI OD graph - flat_data.csv`  
**Output:** `plot_<concentration>.png` for each unique concentration

### `CFU/plot_cfu.py`
Generates a CFU/mL time-series plot for *L. lactis*, *L. lactis pMGI*, and *S. hominis*.

**Input:** `CFU  - Sheet5.csv`  
**Output:** `cfu_plot.png`

## Setup

Linux/Mac:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Windows:
```bat
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

```bash
cd OD_graph
python plot_od.py

cd ../CFU
python plot_cfu.py
```
