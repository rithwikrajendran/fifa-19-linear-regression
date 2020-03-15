#Training a Linear Regression Model
from player_data_preparation import *
regressor = LinearRegression()

# Fitting the training data to our model
regressor.fit(X_train, Y_train)

# Predicting the player potential for the Validation set
Y_pred = regressor.predict(X_test)

# R2 score closer to 1 is a good model
print(f"R2 score: {r2_score(Y_test, Y_pred)}")

# MSE (Mean Squared Error) score closer to zero is a good model
print(f"MSE score: {mean_squared_error(Y_test, Y_pred)}")