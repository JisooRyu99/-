'''
Now that we know that the Proline column in our wine dataset has a large amount of variance, let's log normalize it.

Numpy has been imported as np in your workspace.
'''

# Print out the variance of the Proline column
print(wine.Proline.var())

# Apply the log normalization function to the Proline column
wine['Proline_log'] = np.log(wine.Proline)

# Check the variance of the normalized Proline column
print(wine.Proline_log.var())



<script.py> output:
    99166.71735542436
    0.17231366191842012
