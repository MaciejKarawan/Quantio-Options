# Quanto Option on Gold with PLN Payout

**Pricing and hedging a cross-currency (quanto) call on gold (XAU/USD) that pays out in Polish złoty, under correlated geometric Brownian motions.**

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-SciPy-013243?logo=numpy)
![Plotly](https://img.shields.io/badge/Plotly-interactive-3F4F75?logo=plotly)
![Topic](https://img.shields.io/badge/topic-derivatives%20%7C%20FX-blueviolet)

## The problem

Valuation date: 30 June 2023. The instrument pays at T = 30 June 2024

```
payoff = 100 PLN × max( S(T) / S(0) − K , 0 ),     0 ≤ K ≤ 2
```

where S(t) is the gold price in USD. The holder takes gold-price risk but receives a fixed number of złoty, so the USD/PLN exchange rate X(t) enters the price only through its **correlation** with gold.

The whole analysis is carried out in two equivalent model formulations, and the project checks whether they really agree:

1. **(X, S)**: the USD/PLN rate and gold in USD
2. **(X, Y)**: the USD/PLN rate and gold in PLN, Y(t) = X(t)·S(t)

## What's implemented

- **Calibration** from daily XAU/USD and USD/PLN data (2010 to June 2023): rolling volatilities, mean returns and rolling correlation over 1–4 year windows, combined with PLN and USD interest-rate assumptions
- **Closed-form pricing** with the quanto drift adjustment (as a dividend-yield-like correction), plus delta
- **Correlated GBM simulation** via Cholesky decomposition (with a regularisation fallback) and empirical validation of the simulated correlation
- **Delta hedging of the quanto** in both formulations: P&L distribution vs. rehedging frequency, portfolio composition over time, and a backtest on the realised 2023–2024 path
- **Sensitivity analysis**: price heatmaps over pairs of parameters (time, strike, ρ, gold volatility, interest rates) and P&L tests vs. strike, volatility, ρ and hedging frequency, run side by side for both formulations
- Interactive **Plotly** visualisations and animations

The calibrated gold vs. USD/PLN correlation is negative (ρ ≈ −0.33). This sets the sign of the quanto drift correction.

## Repository structure

```
src/quanto_options/   data_loader, pricing, simulation (correlated GBM),
                      hedging, visualization, dual_model_visualization
scripts/              run_analysis (calibration → pricing → hedging), examples, animation
data/raw/             xauusd_d.csv, usdpln_d.csv (daily prices)
reports/              project brief (PDF, in Polish)
```

## How to run

```bash
python -m pip install -e .
python -m scripts.run_analysis
```

Smoke tests: `python -m unittest discover -s tests`.

## Background

📄 [Project brief (PDF, Polish)](reports/Projekt%203%20%20-%20IF1%202025.pdf). Financial Engineering I course project, 2024/2025.
