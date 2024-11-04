import pandas as pd 
from sklearn.tree import DecisionTreeRegressor


melbourne_file_path = 'melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path)
melbourne_data = melbourne_data.dropna(axis=0)
print(melbourne_data.describe())
# y = melbourne_data.Price 
# # print(y)

# melbourne_features = ['Rooms', 'Bathroom', 'Landsize', \
#                       'Lattitude', 'Longtitude']

# X = melbourne_data[melbourne_features]
# # print(X.describe())
# # print(X.head())

# # Define model. Specify a number for random_state to ensure same results each run
# melbourne_model = DecisionTreeRegressor(random_state=1)

# # Fit model
# # fi = melbourne_model.fit(X, y)
# # print(fi)

# melbourne_model.fit(X, y)
# n = 100
# print("Making predictions for the following %d houses:" % n)
# b = X[110:110+n+1]
# print(b)
# print("The predictions are")
# print(melbourne_model.predict(b))