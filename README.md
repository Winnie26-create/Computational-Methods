# Computational-Methods

This repository implements a structured quantitative finance workflow covering **model calibration, stochastic simulation, and portfolio construction**.  
The project was completed as part of a **graduate-level quantitative finance course** and focuses on translating theoretical models into simulation-based portfolio insights for risk-aware decision-making.

---

## Quantitative Workflow

The analysis follows a three-stage process commonly used in quantitative finance:

1. **Model Calibration**  
   Estimate model parameters from market data to ensure realistic asset price dynamics.

2. **Simulation**  
   Use calibrated parameters to generate asset price and return distributions via Monte Carlo simulation.

3. **Portfolio Construction & Analysis**  
   Construct and evaluate portfolios based on simulated outcomes to analyze risk–return trade-offs.

---

## Project Structure

### 1. Model Calibration

- **calibration.ipynb**  
  Calibrates the Heston stochastic volatility model to market option data and estimates key parameters governing asset price behavior.

---

### 2. Simulation Engine (`simulation/`)

This folder contains reusable Python modules supporting simulation and numerical analysis.

- stock_price_simulation.py — Simulates stock price paths under the calibrated Heston model  
- monte_carlo.py — Runs Monte Carlo simulations to generate payoff and return distributions  
- acuire_stock_and_option_price.py — Retrieves stock prices and option inputs for modeling  
- covariance_mat.py — Computes covariance and correlation matrices from simulated returns  
- lagrange_polynomial.py — Implements numerical interpolation methods used in calibration and pricing  

---

### 3. Portfolio Construction & Analysis

- **portfolio_construction.ipynb**  
  Constructs option portfolios using simulated return distributions and evaluates risk–return characteristics through portfolio optimization techniques.

---

## Key Findings & Insights

- Model calibration significantly influences simulated price dynamics, highlighting the sensitivity of portfolio outcomes to underlying parameter estimates.  
- Monte Carlo simulations reveal non-linear payoff distributions and asymmetric risk profiles that are not captured by closed-form expectations alone.  
- Portfolio construction based on simulated return distributions improves risk awareness by explicitly accounting for tail risk and volatility clustering.  
- Scenario-based analysis demonstrates how changes in volatility and correlation assumptions materially affect portfolio risk–return trade-offs, reinforcing the importance of robust modeling assumptions in decision-making.

---

## Methodologies

- Stochastic volatility modeling (Heston model)  
- Monte Carlo simulation  
- Numerical optimization and interpolation  
- Covariance estimation and risk analysis  
- Portfolio construction and performance evaluation  

---

## Tech Stack

- Python (NumPy, Pandas, Matplotlib)  
- Time-series analysis  
- Quantitative risk modeling  
- Scenario-based simulation and analytical reporting  

---

## Notes

This project emphasizes modular design and a clear separation between calibration, simulation, and portfolio analysis, mirroring real-world quantitative research and financial engineering workflows.
