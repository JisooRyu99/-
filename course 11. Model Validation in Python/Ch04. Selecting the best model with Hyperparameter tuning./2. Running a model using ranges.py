'''
You have just finished creating a list of hyperparameters and ranges to use when tuning a predictive model for an assignment. You have used max_depth, min_samples_split, and max_features as your range variable names.
'''

from sklearn.ensemble import RandomForestRegressor

# Fill in rfr using your variables
rfr = RandomForestRegressor(
    n_estimators=100,
    max_depth=random.choice(max_depth),
    min_samples_split=random.choice(min_samples_split),
    max_features=random.choice(max_features))

# Print out the parameters
print(rfr.get_params())
