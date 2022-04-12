'''
You'll visually inspect a 4 feature sample of the ANSUR dataset before and after PCA using Seaborn's pairplot(). This will allow you to inspect the pairwise correlations between the features.

The data has been pre-loaded for you as ansur_df.
'''
1. Create a Seaborn pairplot to inspect ansur_df.

# Create a pairplot to inspect ansur_df
sns.pairplot(ansur_df)

plt.show()


2. Create the scaler and standardize the data.

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
 
# Create the scaler
scaler = StandardScaler()
ansur_std = scaler.fit_transform(ansur_df)
 
  
3. Create the PCA() instance and fit and transform the standardized data.

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
 
# Create the scaler
scaler = StandardScaler()
ansur_std = scaler.fit_transform(ansur_df)
 
# Create the PCA instance and fit and transform the data with pca
pca = PCA()
pc = pca.fit_transform(ansur_std)
pc_df = pd.DataFrame(pc, columns=['PC 1', 'PC 2', 'PC 3', 'PC 4'])
 
4. Create a pairplot of the principal component dataframe.

# Create a pairplot of the principal component dataframe
sns.pairplot(pc_df)
plt.show()
