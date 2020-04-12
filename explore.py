import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# I'm setting your matplotlib to be XKCD here. Feel free to delete this line.
# plt.xkcd()


def plot_variable_pairs(df, hue=None):
    """Scatterplot and regression line with Kernel Density Estimation kde to estimate the probability density function"""

    g = sns.pairplot(df, hue=hue, kind="reg", corner=True, diag_kind="kde", plot_kws={'line_kws':{'color':'red'}, 'scatter_kws': {'alpha': 0.7}})
    g.fig.suptitle("Scatterplot with Regression for Continuous Variables")
    plt.show()




# Write a function, plot_categorical_and_continous_vars(categorical_var, continuous_var, df),
# that outputs 3 different plots for plotting a categorical variable with a continuous variable, e.g. tenure_years with total_charges. For ideas on effective ways to visualize categorical with continuous: https://datavizcatalogue.com/.
# You can then look into seaborn and matplotlib documentation for ways to create plots.
def plot_categorical_and_continous_vars(categorical_var, continuous_var, df):
    sns.catplot(y=categorical_var, x=continuous_var, data=df)
    sns.catplot(x=categorical_var, kind="count", palette="ch:.25", data=df);
    sns.catplot(x=categorical_var, y=continuous_var, kind="box", data=df);
    sns.catplot(x=categorical_var, y=continuous_var, kind="violin", bw=.15, cut=0, data=df);
