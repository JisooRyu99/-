'''
You'll be working on a slightly modified subsample of the ANSUR dataset with just head measurements pre-loaded as head_df.
'''

# Create the boxplot
head_df.boxplot()
 
plt.show()

# Normalize the data
normalized_df = head_df /head_df.mean()

normalized_df.boxplot()
plt.show()

# Normalize the data
normalized_df = head_df / head_df.mean()

# Print the variances of the normalized data
print(normalized_df.var())

