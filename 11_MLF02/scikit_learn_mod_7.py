### ESTIMATORS

# The diabetes dataset is a classic example dataset in machine learning and statistics.
# It contains measurements of various features (e.g. number of times pregnant, blood pressure, etc.)
# For patients with diabetes.
# The dataset is often used for regression tasks and is included in the scikit-learn library.
from sklearn.datasets import load_diabetes
diabetes = load_diabetes()
print(f'\nDIABETES DATASET'
      f'\n---------------')
print(f'\nKEYS: {diabetes.keys()}')
print(f'\nSHAPE: {diabetes.data.shape}')
print(f'\nFEATURE NAMES:\n' + '\n'.join(diabetes.feature_names))
print(f'\nFIRST 3 DATA POINTS:')
print(*diabetes.data[:3], sep='\n')
print(f'\nDESCRIPTION:\n{diabetes.DESCR}')

# Linear Regression
from sklearn.linear_model import Ridge
