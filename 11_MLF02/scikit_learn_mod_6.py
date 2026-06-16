### DATASETS

# The Iris dataset is a classic example dataset in machine learning and statistics.
# It contains measurements of four features (sepal length, sepal width, petal length, and petal width).
# For three species of iris flowers (Setosa, Versicolor, and Virginica).
# The dataset is often used for classification tasks and is included in the scikit-learn library.
from sklearn.datasets import load_iris
iris = load_iris()
print(f'IRIS DATASET'
      f'\n------------')
print(f'\nKEYS: {iris.keys()}')
print(f'\nSHAPE: {iris.data.shape}')
print(f'\nTARGET NAMES:\n' + '\n'.join(iris.target_names))
print(f'\nFEATURE NAMES:\n' + '\n'.join(iris.feature_names))
print(f'\nFIRST 3 DATA POINTS:')
print(*iris.data[:3], sep="\n")
print(f'\nDESCRIPTION:\n{iris.DESCR}')

# The California Housing dataset is a more complex dataset which is often used for regression tasks.
# It contains measurements of various features (e.g. average number of rooms, average number of bedrooms, etc.)
# For houses in California.
# The dataset is often used for regression tasks and is included in the scikit-learn library.
from sklearn.datasets import fetch_california_housing
housing = fetch_california_housing()
print(f'\nHOUSING DATASET'
      f'\n---------------')
print(f'\nKEYS: {housing.keys()}')
print(f'\nSHAPE: {housing.data.shape}')
print(f'\nTARGET NAMES:\n' + '\n'.join(housing.target_names))
print(f'\nFEATURE NAMES:\n' + '\n'.join(housing.feature_names))
print(f'\nFIRST 3 DATA POINTS:')
print(*housing.data[:3], sep='\n')
print(f'\nDESCRIPTION:\n{housing.DESCR}')

# California Housing Pandas
import pandas as pd
df = pd.DataFrame(housing.data, columns=housing.feature_names)
print(f'\nHOUSING PANDAS'
      f'\n--------------')
print(df)
df['MedHouseVal'] = housing.target
corr = df[['MedInc','MedHouseVal']].corr()
print(f'\nCORRELATION:\n {corr}')