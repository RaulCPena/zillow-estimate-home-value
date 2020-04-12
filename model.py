# modeling functions for Zillow project

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, explained_variance_score
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import RFE
from math import sqrt
import warnings
warnings.filterwarnings("ignore")
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.sandbox.regression.predstd import wls_prediction_std

# import script files
import env
import acquire
import prep

# X_train, X_test, y_train, y_test
def model_testing(X_train, X_test, y_train, y_test):
    predictions_train = pd.DataFrame({'actual': y_train.home_value})
    predictions_test = pd.DataFrame({'actual': y_test.home_value})

    # model 1
    lm_1 = LinearRegression()
    lm_1.fit(X_train, y_train)
    lm_1_predictions = lm_1.predict(X_train)
    predictions_train['lm_1'] = lm_1_predictions

    # model 2
    lm_2 = LinearRegression()
    lm_2.fit(X_test, y_test)
    lm_2_predictions = lm_2.predict(X_test)
    predictions_train['lm_2'] = lm_2_predictions

# plot residuals using seaborn

def plot_residuals(actual, predicted):
    residuals = actual - predicted
    plt.hlines(0, actual.min(), actual.max(), ls=':')
    plt.scatter(actual, residuals)
    plt.ylabel('residual ($y - \hat{y}$)')
    plt.xlabel('actual value ($y$)')
    plt.title('Actual vs Residual')
    return plt.gca()
# use seaborn to plot regression

def plot_regression(x, y):
    res = sm.OLS(y, x).fit()
    # draw a plot to compare the true relationship to OLS predictions
    prstd, iv_l, iv_u = wls_prediction_std(res)

    fig, ax = plt.subplots(figsize=(8,6))

    ax.plot(x, y, 'o', label="data")
    ax.plot(x, y_true, 'b-', label="True")
    ax.plot(x, res.fittedvalues, 'r--.', label="OLS")
    ax.plot(x, iv_u, 'r--')
    ax.plot(x, iv_l, 'r--')
    ax.legend(loc='best');
    plt.show()
