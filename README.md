# Portfolio Optimization with Time Series Forecasting

## Project Overview
This project develops an end-to-end quantitative workflow for forecasting asset prices, optimizing a portfolio, and validating strategy performance through backtesting. The analysis focuses on Tesla (TSLA) as a high-growth asset, combined with SPY and BND for diversification, following principles from time series analysis, Modern Portfolio Theory (MPT), and risk management.

The project is completed as part of **KAIM – Week 9**.

---

## Business Objective
Enhance portfolio management by generating **decision-support insights** rather than precise price predictions. In line with the **Efficient Market Hypothesis (EMH)**, forecasting is used to understand **volatility, risk, and uncertainty**, supporting informed portfolio allocation decisions using risk-adjusted metrics such as **Value at Risk (VaR)** and **Sharpe Ratio**.

---

## Project Structure
portfolio-optimization/
│
├── data/
│ ├── raw/ # Raw data from YFinance
│ └── processed/ # Cleaned and transformed datasets
│
├── notebooks/
│ ├── task1_eda.ipynb
│ ├── task2_forecasting.ipynb
│ ├── task3_forecasting_analysis.ipynb
│ ├── task4_portfolio_optimization.ipynb
│ └── task5_backtesting.ipynb
│
├── src/
│ ├── init.py
│ └── portfolio_utils.py # Reusable utility functions
│
├── tests/ # (Optional) unit tests
│
├── requirements.txt
└── README.md


---

## Tasks Summary

### Task 1 – Data Preprocessing & Exploratory Data Analysis
- Extracted historical data for **TSLA, SPY, and BND** (2015–2026) using YFinance
- Cleaned and validated data (missing values, data types)
- Conducted EDA including price trends, daily returns, and volatility analysis
- Performed stationarity testing using the **Augmented Dickey-Fuller (ADF)** test
- Calculated foundational risk metrics such as **VaR** and **Sharpe Ratio**

---

### Task 2 – Time Series Forecasting
- Split data chronologically into training and testing sets
- Built and evaluated:
  - **ARIMA** (statistical model)
  - **LSTM** (deep learning model)
- Compared models using MAE, RMSE, and MAPE
- Selected the best-performing model based on accuracy and robustness

---

### Task 3 – Forecast Future Market Trends
- Generated 6–12 month forecasts using the selected model
- Visualized forecasts with confidence intervals
- Analyzed trends, uncertainty, and forecast reliability
- Identified potential market opportunities and risks

---

### Task 4 – Portfolio Optimization (Modern Portfolio Theory)
- Combined forecast-based TSLA expected returns with historical SPY and BND returns
- Computed covariance matrix and visualized asset relationships
- Generated the **Efficient Frontier**
- Identified:
  - Maximum Sharpe Ratio portfolio
  - Minimum Volatility portfolio
- Recommended an optimal portfolio with justification

---

### Task 5 – Strategy Backtesting
- Backtested the optimized portfolio on out-of-sample data (2025–2026)
- Compared performance against a **60% SPY / 40% BND benchmark**
- Evaluated:
  - Total return
  - Annualized return
  - Sharpe Ratio
  - Maximum drawdown
- Assessed strategy viability and limitations

---

## Key Results
- LSTM outperformed ARIMA in short-term forecasting accuracy
- Optimized portfolio achieved superior risk-adjusted returns compared to benchmark
- Backtesting demonstrated competitive performance with manageable drawdowns
- Forecast uncertainty increased with longer horizons, reinforcing cautious interpretation

---

## Engineering & Best Practices
- Modularized reusable logic in `src/`
- Applied fail-fast checks and input validation
- Used defensive programming (`try/except`) around external calls
- Ensured reproducibility and clarity through structured notebooks

---

## Limitations & Future Work
- Short backtesting window
- No transaction costs or slippage modeled
- Static portfolio weights (no dynamic rebalancing)
- Future work:
  - Longer backtests
  - Regime-aware models
  - Transaction cost modeling
  - Volatility clustering analysis

---

## Tech Stack
- Python 3.11
- pandas, numpy
- yfinance
- statsmodels
- tensorflow / keras
- PyPortfolioOpt
- matplotlib, seaborn

---

## Author
**Betelhem Kibret Getu**  
KAIM – Week 9 Project
