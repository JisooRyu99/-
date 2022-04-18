'''
Take a look at the hiking dataset. There are several columns here that need encoding, one of which is the Accessible column, which needs to be encoded in order to be modeled. Accessible is a binary feature, so it has two values - either Y or N - so it needs to be encoded into 1s and 0s. Use scikit-learn's LabelEncoder method to do that transformation.
'''

# Set up the LabelEncoder object
enc = LabelEncoder()

# Apply the encoding to the "Accessible" column
hiking['Accessible_enc'] = enc.fit_transform(hiking.Accessible)

# Compare the two columns
print(hiking[['Accessible', 'Accessible_enc']].head())



<script.py> output:
      Accessible  Accessible_enc
    0          Y               1
    1          N               0
    2          N               0
    3          N               0
    4          N               0
