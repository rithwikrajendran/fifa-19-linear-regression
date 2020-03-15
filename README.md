A sample linear regression project where we take EA Sports' FIFA 19 player dataset from Kaggle and peform linear regression to correlate a player's potential rating with other factors/parameters like age, overall rating etc..

Steps Followed -

1. Download the dataset. Link - (https://www.kaggle.com/karangadiya/fifa19/data) 
2. player_data_import.py - Import all the necessary libraries and also read the dataset.
3. player_data_preparation.py - Plot a very basic scatter plot with Age & Potential. Here, we also prepare the data and split the dataset into train and test sets.
4. player_data_train.py - Fit the training data to our model followed by which we predict and create the validation set. In the end, we calculate the R2 score as well as the mean squared error score (MSE). The model performs better if R2 score is closer to 1 and MSE is closer to 0.
5. R2 Score & MSE Score.txt - Contains R2 score and MSE score of one run of both univariate as well as multivariate linear regressions respectively.
