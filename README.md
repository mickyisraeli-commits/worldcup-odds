# World Cup Odds Tracker

This project tracks FIFA World Cup winner probabilities using Polymarket's public API.

## Features
- Automatic market discovery
- Hourly updates via GitHub Actions
- CSV outputs (long + wide format)
- No API key required

## Output

- `data/odds_long.csv`
- `data/odds_wide.csv`

## Run locally

```bash
pip install -r requirements.txt
python run_pipeline.py


---

# 🚀 What you do now

Inside your repo:

### Option A (easiest)
Copy files via GitHub web UI

### Option B (best)
```bash
git clone https://github.com/mickyisraeli-commits/worldcup-odds
cd worldcup-odds
# paste files
git add .
git commit -m "initial pipeline"
git push
trigger
