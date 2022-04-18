'''
One of the columns in the volunteer dataset, category_desc, gives category descriptions for the volunteer opportunities listed. Because it is a categorical variable with more than two categories, we need to use one-hot encoding to transform this column numerically. Use Pandas' get_dummies() function to do so.
'''

# Transform the category_desc column
category_enc = pd.get_dummies(volunteer["category_desc"])

# Take a look at the encoded columns
print(category_enc.head())


<script.py> output:
       Education  Emergency Preparedness  Environment  Health  Helping Neighbors in Need  Strengthening Communities
    0          0                       0            0       0                          0                          0
    1          0                       0            0       0                          0                          1
    2          0                       0            0       0                          0                          1
    3          0                       0            0       0                          0                          1
    4          0                       0            1       0                          0                          0
