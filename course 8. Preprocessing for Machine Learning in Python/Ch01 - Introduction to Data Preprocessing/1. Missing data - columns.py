'''
We have a dataset comprised of volunteer information from New York City. The dataset has a number of features, but we want to get rid of features that have at least 3 missing values.

How many features are in the original dataset, and how many features are in the set after columns with at least 3 missing values are removed?

The dataset volunteer has been provided.
Use the dropna() function to remove columns.
You'll have to set both the axis= and thresh= parameters.
'''


volunteer.shape
# (665, 35)

volunteer.dropna(axis=1,thresh=3).shape
# (665, 24)
