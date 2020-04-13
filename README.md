# Slide Presentation Link [Slide](https://docs.google.com/presentation/d/1Ps1UUwBc6hx88SbUTtkanYUtPfDVdXA1LBRmZkVT-HE/edit?usp=sharing)

# Plan
- As a junior data scientist, an :email: requesting the following is recieved:
    - Predict the values of single unit properties that a tax district assesses using property data from whos last transaction was during the "hot months" (in terms of real estate demand) of May and June 2017.
    
    - A few problems exist:    
    __a:__ the current data which gave the location of each property has been lost by __Zach__ :no_good:. We need to know what county each property is located in. So we will have to find a way to acquire this data.
    	- :bulb: the data consists of a fips number which is an identifier to what county it is located in, so we will have to identify all the unique fips and include that in our dataframe.
    - ❗️ The Zillow Data Science team would also like to know the distribution of tax rates for each county but specified this is not part of the __MVP__ ❗️
        - since the data already has the tax amounts and tax value of the home it should be easy to create a new notebook with this information. 
        __We cannot use this information in our model__

# Deliverables
- [x] Create a report in the form of slides and present it verbally.
- [x] Create a github repository containing all my work, which should consist of the following:
    - [x] at least 1 jupyter notebook that walks throuh the pipeline
    - [x] ensure all questions are being answered 
    - [x] add all the `.py` files so our work can be reproduced, knowing that for this to be reporduced by someone else they would have to have their own `env.py` so they can access the SQL  Zillow database


# The Pipeline

#### Project Planning and README
- [x] brainstorm ideas, hypotheses related to how variables might impact or relate to each other, both within independent variables anbd between the independent variables and the dependent variable. 
- [x] have a detailed `README.md`

#### Acquire:
- [x] create a dataframe ready to prepare
- [x] `acquire.py` will be able to reproduce gathering data from SQL

#### Prep:
- [x] create dataset ready to be analyzed
- [x] use what we learned to plot distributions of individual variables and identify any outliers and if needed plan out how to handle them.

#### Data Exploration:
- [x] visualize as many combinations of variables
- [x] identify which independent variables are correlated with the dependent
- [x] summarize takaways and conclusions

#### Modeling & Evaluation:
- [x] develop a regression model that performs better than a baseline.
- [x] evaluate a baseline model
- [x] show how the given model performs better than the baseline
- [x] create a `model.py` file that will have the functions to fit, predict and evaluate the model

Be sure and evaluate your model using the standard techniques:
- plotting the residuals
- computing the evaluation metric (SSE, RMSE, and/or MSE)
- comparing to baseline, plotting ![\y](https://render.githubusercontent.com/render/math?math=%5Cy) by ![\bar{y}](https://render.githubusercontent.com/render/math?math=%5Cbar%7By%7D)
# Hypothesis
![\boldsymbol{H_0}](https://render.githubusercontent.com/render/math?math=%5Cboldsymbol%7BH_0%7D) a home’s square footage, bedroom count, and bathroom count are not predictors of home value

![\boldsymbol{H_a}](https://render.githubusercontent.com/render/math?math=%5Cboldsymbol%7BH_a%7D) a home’s square footage, bedroom count, and bathroom count are predictors of home value

# Data Dictionary
| variables  | count  | datatype |
|---|---|---|
| parcelid  |   | int64  |
| bathrooms  |   | float64  |
| bedrooms  |   | float64  |
| square_feet  |   | float64  |
| fips_number |   | float64  |
| propertylandusetypeid  |   | int64  |
| propertylandusedesc  |   | object  |
|  home_value |   | float64  |
| tax_amount  |   | float64  |
| dtype: object  |   |   |

# What can we conclude from the findings:
- [x] The OLS model produced a model_RMSE < baseline_RMSE; therfore the OLS model had __VALUE__.
- [x] The r^2 score has a p_value < 0.05; therfore the value is __SIGNIFICANT__.
- [x] Using feature elimination for  Multilinear Regression  and Polynomial Regression Models, the RMSE for both were similar. However, the RMSE for the OLS model was lower (closer to zero) and therefore a better model for predicting home value.
- [x] Based on the results of all 3 models, the null hypothesis can be rejected, and the alternative hypothesis can be accepted:
__A home’s square footage, bedroom count, and bathroom count are predictors of home value__

# How to Recreate The Project
- [x] This repo will have all the files needed to replicate the notebook

## **Note:** You will need to create your own `env.py` file to access the database
