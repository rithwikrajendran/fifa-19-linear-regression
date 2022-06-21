# Linear Regression on FIFA 19 data

## Introduction

In this pet project, I tried linear regression on EA Sports FIFA 19 player dataset made available on Kaggle. A player's potential rating was predicted using variables like the player's age, player's overall rating in the game etc. The dataset is available on the following link - https://www.kaggle.com/karangadiya/fifa19/data 

### Short Description of the files

1. **player_data_import.py** - Importing necessary libraries and reading the data.
2. **player_data_preparation.py** - Basic data exploration, visualisation and data preparation.
3. **player_data_train.py** - Model training, prediction and performance evaluation. This is where the real work happens.
5. **R2 Score & MSE Score.txt** - Contains R2 score and MSE score of one run of both univariate as well as multivariate linear regressions respectively.

## Conclusion

We do end up with good $R^2$-score (closer to 1), which means our model generalises well and the line of best fit is a good fit for our data. We have a small mean squared error as well, indicating that we ended up with a good model when we went with multiple linear regression.
