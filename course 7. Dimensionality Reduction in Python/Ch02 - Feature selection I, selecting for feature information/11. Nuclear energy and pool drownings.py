'''
The dataset that has been pre-loaded for you as weird_df contains actual data provided by the US Centers for Disease Control & Prevention and Department of Energy.

Let's see if we can find a pattern.

Seaborn has been pre-loaded as sns and matplotlib.pyplot as plt.
'''

# Print the first five lines of weird_df
print(weird_df.head())

# Put nuclear energy production on the x-axis and the number of pool drownings on the y-axis
sns.scatterplot(x='nuclear_energy', y='pool_drownings', data=weird_df)
plt.show()

# Print out the correlation matrix of weird_df
print(weird_df.corr())

Question
What can you conclude from the strong correlation (r=0.9) between these features?
Possible Answers = 4

1. If the nuclear energy production increases next year I'd better not go swimming.

2. You could bring the nuclear energy production down by increasing pool safety.

3. To build a Uranium usage forecaster, I should use pool drownings or nuclear energy production as features but not both.

4. Not much, correlation does not imply causation.
