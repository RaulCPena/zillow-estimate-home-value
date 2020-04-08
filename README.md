# Estimate Home Value
# Slide Presentation Link <- insert link later
#### Background:

- email containing information on each properties location was lost by Zach :anger:
	- property taxes are assessed at the county level and we would like to know what states and counties the properties are located in
- we want to know the distribution of tax rates for each county. What should the data look like :question:
	- The data should have the following:
		- __tax__ amounts and __tax__ values of the home
		- include in report the distribution of tax rates for each county, which will show how much each property varies by county and the rates of the bulk of the properties which are around each property

#### Other notes:
- Our first model will use the following features:
	- square feet of the home
	- number of bedrooms
	- number of bathrooms
	- __taxvalueddollarcnt__ We can expand further after we create a __MVP__(minimally viable product)
#### The process:
- ensure all requirements given by __stakeholders__ are being met and represented in our data, report, and model
- ensure that __QA__(quality assurance) data validation is being done, for example: make sure the data is what we think it is
- use available data and select the best fields that best represent:
	- square foot of home
	- bedroom count
	- bathroom count

# Project Deliverables

- [ ] Predict values of single unit properties using data acquired during the months of May and June 2017
- [x] Identify what states and counties the selected properties are in
- [x] Determine the distribution of tax rates by county
- [ ] A report (in the form of a presentation, both verbal and through slides)
- [ ] Create a github repository that will provide a walkthrough of the pipeline along with all the neccessary .py files to reproduce the model
	- the model will be reproducible with the creation of your own `env.py` file

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
#### Split and Scale:
- [x] train, test, and scale our two dataframes using our `split_scale.py`, 
#### Data Exploration:
- [ ] run at least 1 t-test and 1 correlation test(more if needed)
- [ ] visualize as many combinations of variables
- [ ] identify which independent variables are correlated with the dependent
- [ ] summarize takaways and conclusions

#### Modeling & Evaluation:
- [ ] develop a regression model that performs better than a baseline.
- [x] evaluate a baseline model
- [x] show how the given model performs better than the baseline
- [ ] create a `model.py` file that will have the functions to fit, predict and evaluate the model

Your notebook will contain various algorithms and/or hyperparameters tried, along with the evaluation code and results, before settling on the final algorithm.

Be sure and evaluate your model using the standard techniques:
- plotting the residuals
- computing the evaluation metric (SSE, RMSE, and/or MSE)
- comparing to baseline, plotting ![\y](https://render.githubusercontent.com/render/math?math=%5Cy) by ![\bar{y}](https://render.githubusercontent.com/render/math?math=%5Cbar%7By%7D)
# Hypothesis
![\boldsymbol{H_0}](https://render.githubusercontent.com/render/math?math=%5Cboldsymbol%7BH_0%7D) a homes square feet, bedroom count, and bathroom count are not drivers in a homes value

![\boldsymbol{H_a}](https://render.githubusercontent.com/render/math?math=%5Cboldsymbol%7BH_a%7D) a homes square feet, bedroom count, and bathroom count are not drivers in a homes value




#### Optional Feature Selection:
> - [ ] have the dataframe with the features to be used to build the model
> - [ ] have we chosen all the features needed that will be helpful
> - [ ] use `feature_selection.py` to run whatever functions that will create the dataframe that contains all the best features that will be used to model the data
# What can we conclude from the findings:
- [ ] will add later
- [ ] will add later
- [ ] will add later
- [ ] will add later
# How to Recreate The Project
- [ ] This repo will have all the files needed to replicate the notebook

## **Note:** You will need to create your own `env.py` file to access the database
