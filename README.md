# rent-prediction-ML
 Machine learning project using
 
- python
- web scraping
- pandas
- sklearn
- numpy
- preprocessing
- exploratory data analysis

## Algorithms Used :

 - **Linear Regression**: 
A simple regression model that assumes a linear relationship between the input variables and the target variable (rent price).

 - **Decision Tree Regression**: A tree-based model that splits the dataset into subsets based on feature values, aiming to predict rent based on the most influential features.

 - **Random Forest**: An ensemble learning method based on decision trees, which improves the prediction by averaging the results of multiple trees.

 - **Support Vector Regression (SVR)**: A method that tries to fit the best line within a threshold of error, optimizing for a balance between underfitting and overfitting.

 - **K-Nearest Neighbors (KNN)**: A non-parametric method that predicts rent by averaging the prices of the K nearest data points.

 - **Lasso Regression**: A linear model that includes L1 regularization, which helps in feature selection by penalizing the absolute size of coefficients.

 - **Ridge Regression**: A linear model that uses L2 regularization, which penalizes the square of the coefficients to prevent overfitting.


## Preprocessing
Before training the models, I performed the following preprocessing steps:

 - Data Cleaning: Handled missing values and removed irrelevant features.

 - Feature Engineering: Created new features that could better capture the variation in rent prices.

 - Normalization/Scaling: Applied feature scaling to ensure that algorithms like KNN and SVR perform optimally.

## Model Evaluation
I used the following metrics to evaluate the models:

 - Mean Squared Error (MSE): The average squared difference between the predicted and actual values.

 - R-squared: A measure of how well the model explains the variance in the data.
