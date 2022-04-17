'''
In the volunteer dataset, we're thinking about trying to predict the category_desc variable using the other features in the dataset. First, though, we need to know what the class distribution (and imbalance) is for that label.

Which descriptions occur less than 50 times in the volunteer dataset?

The dataset volunteer has been provided.
The colum you want to check is category_desc.
Use the value_counts() method to check variable counts.
'''

volunteer['category_desc'].value_counts()

'''
Strengthening Communities    307
Helping Neighbors in Need    119
Education                     92
Health                        52
Environment                   32
Emergency Preparedness        15
Name: category_desc, dtype: int64
'''

=> Environment and Emergency Preparedness
