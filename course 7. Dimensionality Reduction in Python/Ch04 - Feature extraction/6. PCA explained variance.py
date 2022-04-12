'''
You'll be inspecting the variance explained by the different principal components of the pca instance you created in the previous exercise.
'''

1. Print the explained variance ratio per principal component.

# Inspect the explained variance ratio per component
print(pca.explained_variance_ratio_)


2. Calculate the cumulative sum of the explained variance ratio using a method of pca.explained_variance_ratio_.

# Print the cumulative sum of the explained variance ratio
print(pca.explained_variance_ratio_.cumsum())
