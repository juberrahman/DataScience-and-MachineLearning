
## Problem: Quick disaster response
When a disaster strikes, the World Food Programme (WFP), as well as the other humanitarian actors, need to design comprehensive emergency operations. They need to know what to bring and in which quantity. How many shelters? How many tons of food? These needs assessments are conducted by humanitarian experts, based on the first information collected, their knowledge and their experience.

What if we could use past disaster data to help them know what is needed?

## Summary of Materials and Methods:
* Dataset used: merged dataset version 14 (OUTPUT_WBI_exposer_cyclones_v14.csv)
* Data processing : filling missing values, encoding categorical features, dealing skewed distribution
* Missing value: KNN Imputer
* Hyper-parameter tuning: Grid Search CV
* Ensemble Methods: Random Forest, Gradient Boosting Method
* Feature Engineering: Log Conversion
* No. of actual Predictors: 45
* Target: Number of people affected
* Validation scheme: 5-fold cross-validation, Test set performance, Unit test performance
* Train set (80%), Test set (20%)

## Models:
* Random Forest (RF)
* Gradient Boosting Method (GBM)
* Support Vector Regression
* Voting ensemble of RF and GBM
* Stack of Ensembles
* Auto ML
## Findings and Discussions:
* Best performing model: Stack of Ensembles
* Performance: RMSLE=2.41 , R-squared value=0.37
* The model is good in predicting the mid-impact cyclones
* For low impact cyclones predictions are over-estimated
* Overall trend shows a weak but expected trend
