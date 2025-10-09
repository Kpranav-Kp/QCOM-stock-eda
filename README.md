# QCOM Stock Analysis: A Comprehensive Exploration

This notebook presents an in-depth exploratory data analysis (EDA) and time series analysis of **Qualcomm (QCOM) stock**, combining data visualization, statistical metrics, and financial time series concepts.

---

## 1. Data Preparation

* **Loading Data:** Import historical stock data and read into a pandas DataFrame.
* **Datetime Handling:** Convert the 'Date' column to datetime and set as index for time series operations.
* **Initial Data Check:**
    * Inspect DataFrame shape and structure.
    * Review data types, null values, and summary statistics.
    * Identify missing values.

---

## 2. Univariate Distribution & Outlier Detection

* **Histograms:** Visualize distributions of all numerical columns.
* **Outlier Detection:** Use the **Interquartile Range (IQR)** to flag potential outliers.
* **Boxplots:** Graphically assess spread and spot obvious outliers. 

---

## 3. Correlation and Bivariate Relationships

* **Correlation Matrix:** Compute correlations and display as a heatmap. 
* **Close Price vs Volume:** Analyze and visualize both raw and log-transformed volume.
* **Close Price vs Open Price:** Plot relationships with reference line for easy comparison.
* **Simple Moving Averages vs Close Price:** Explore correspondence for **SMA_20** and **SMA_50** against Close.
* **Price vs Returns:** Examine Daily Return versus Close Price, and Volume versus Daily Return.
* **Regression Lines:** Add regression fits to relevant scatterplots.

---

## 4. Multivariate Insights

* **Price Trends & Volume:** Concurrently plot closing price and trading volume over the full period and split subperiods.
* **Returns and Moving Averages:** Visualize with pairplots for multivariate comparison.
* **Cross-Correlation:** Quantify and plot cross-correlation between volume changes and daily returns at varying lags.
* **Rolling Correlations:** Explore how the closing price-volume correlation evolves over **60-day windows**.
* **Volatility vs Volume:** Overlay rolling volatility (20-day) with volume to study co-movement.

---

## 5. Time Series Analysis

* **Price & Returns Over Time:** Line plots for overall and yearly trends in closing price and returns.
* **Seasonal Decomposition:** Decompose Close price series into **trend, seasonality, and residuals** for structural insights.
* **Rolling Volatility:** Plot **20/60-day annualized rolling volatility** to illuminate shifts in market risk.
* **Volatility Clustering:** Use **squared log returns** to expose periods of persistent high or low volatility.
* **Distribution Shape:** Calculate and discuss **skewness and kurtosis** of log returns.
* **Drawdown Analysis:** Chart drawdowns from rolling peak values and print **maximum drawdown**. 


* **Volatility Regimes:** Color-code periods of high/low volatility directly on price chart (red vs blue).
* **Directional Volatility:**
    * **Up-day vs Down-day:** Compute and compare volatility on positive and negative return days to highlight asymmetry.
    * **Volatility vs Volume Revisited:** Joint visualization for pattern discovery.

---

## 6. Return Distribution & Statistical Properties

* **Yearly Return Distributions:** Use **violin plots** to visualize log return distribution for each year.
* **Q-Q Plot:** Compare log returns to a normal distribution via **quantile-quantile plot** (detects fat tails/non-normality). 
* **Autocorrelation Analysis:** Plot and interpret **40-lag autocorrelation function (ACF)** for log returns.
* **Risk-Return Tradeoff:** Scatterplot of annualized rolling return vs volatility.

---

## 7. Interactive Visualization

* **PyGWalker Integration:** Enable interactive, browser-based exploration of the DataFrame with dynamic charts.
