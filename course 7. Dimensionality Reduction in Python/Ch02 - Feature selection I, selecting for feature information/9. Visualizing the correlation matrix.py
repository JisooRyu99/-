'''
Reading the correlation matrix of ansur_df in its raw, numeric format doesn't allow us to get a quick overview. Let's improve this by removing redundant values and visualizing the matrix using seaborn.

Seaborn has been pre-loaded as sns, matplotlib.pyplot as plt, NumPy as np and pandas as pd.
'''

# Create the correlation matrix
corr = ansur_df.corr()

# Draw the heatmap
sns.heatmap(corr,  cmap=cmap, center=0, linewidths=1, annot=True, fmt=".2f")
plt.show()

# Create the correlation matrix
corr = ansur_df.corr()

# Generate a mask for the upper triangle
mask = np.triu(np.ones_like(corr, dtype=bool))

# Create the correlation matrix
corr = ansur_df.corr()

# Generate a mask for the upper triangle 
mask = np.triu(np.ones_like(corr, dtype=bool))

# Add the mask to the heatmap
sns.heatmap(corr, mask=mask, cmap=cmap, center=0, linewidths=1, annot=True, fmt=".2f")
plt.show()


ansure_df.corr()

Elbow rest height  Wrist circumference  Ankle circumference  Buttock height  Crotch height
Elbow rest height             1.000000             0.294753             0.301963       -0.007013      -0.026090
Wrist circumference           0.294753             1.000000             0.702178        0.576679       0.606582
Ankle circumference           0.301963             0.702178             1.000000        0.367548       0.386502
Buttock height               -0.007013             0.576679             0.367548        1.000000       0.929411
Crotch height                -0.026090             0.606582             0.386502        0.929411       1.000000
