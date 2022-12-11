# Interpretable machine learning methods for battery voltage prediction


# Research Goal
Interpretation of machine learning models is one of the key ways to get intuition on how to improve the model. In this study we explore the interpretability of machine learning models to guide us to a path of finding better accuracy in the models for estimating Density Functional Theory(DFT) calculated voltage of battery materials. 

# Findings
We show that by excluding low impact features that we figure out from our interpretation, we can get better accuracy in our model. We achieve a maximum $R^2$ score of 0.9908 and minimum RMSE of 0.1205 in estimating DFT calculated maximum voltage which outperforms other approaches in existing literatures on the same dataset. 

![SHAP summary plot XGboost model](https://github.com/rajoy99/battery_intepretable/blob/main/summaryplotXgboost.png "SHAP summary plot XGboost model")

# Application 
We built a desktop GUI app by PyQT5 to make it easier for non tech people to make inferences from the developed machine learning model in materials science/chemical engineering research labs. 
