from player_data_import import *

#Preparing the data
X = player_data[['Age', 'Overall']]  #Multivariate Linear Regression - For Univariate LR, use one column in X
Y = player_data[['Potential']]  #The target variable/data (The output)

#Visualisation of the actual potential with Age - Scatter Plot
x_axis = player_data[["Age"]]
y_axis = player_data[["Potential"]]
plt.scatter(x_axis, y_axis)
plt.title("Age vs Actual Player Potential")
plt.xlabel = "Age"
plt.ylabel = "Player Potential"
plt.show()

# Splitting the dataset into train and validation sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)