'''
We'll combine the votes of the 3 models you built in the previous exercises, to decide which features are important into a meta mask. We'll then use this mask to reduce dimensionality and see how a simple linear regressor performs on the reduced dataset.

The per model votes have been pre-loaded as lcv_mask, rf_mask, and gb_mask and the feature and target datasets as X and y.
'''

# Sum the votes of the three models
votes = np.sum([lcv_mask, rf_mask, gb_mask], axis=0)

'''
<script.py> output:
    [1 0 2 2 0 1 0 3 1 1 1 3 1 1 1 3 0 1 1 2 1 1 2 1 1 3 2 1 3 1 3 3]
'''

# Create a mask for features selected by all 3 models
meta_mask = votes >= 3

'''
<script.py> output:
    [False False False False False False False False False False False False
     False False False False False False False False False False False False
     False False False False False False False False]

<script.py> output:
    [False False False False False False False  True False False False  True
     False False False  True False False False False False False False False
     False  True False False  True False  True  True]
'''


# Apply the dimensionality reduction on X
X_reduced = X.loc[:, meta_mask]

'''
<script.py> output:
    Index(['chestcircumference', 'forearmcircumferenceflexed', 'hipbreadth', 'thighcircumference', 'waistcircumference', 'wristheight', 'BMI'], dtype='object')
'''

# Plug the reduced dataset into a linear regression pipeline
X_train, X_test, y_train, y_test = train_test_split(X_reduced, y, test_size=0.3, random_state=0)
lm.fit(scaler.fit_transform(X_train), y_train)
r_squared = lm.score(scaler.transform(X_test), y_test)
print('The model can explain {0:.1%} of the variance in the test set using {1:} features.'.format(r_squared, len(lm.coef_)))

'''
<script.py> output:
    The model can explain 86.8% of the variance in the test set using 7 features.
'''    


