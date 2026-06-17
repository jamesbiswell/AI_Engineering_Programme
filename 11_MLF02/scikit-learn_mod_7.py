### ESTIMATORS

## Dataset

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

## Predictors

# Split the dataset into training and test sets
from sklearn.model_selection import train_test_split
x = diabetes.data
y = diabetes.target
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=23)
print(f'\nTRAINING DATASET:')
print(f'\nX TRAIN SHAPE: {x_train.shape}')
print(f'\nX TEST SHAPE: {x_test.shape}')
print(f'\nY TRAIN SHAPE: {y_train.shape}')
print(f'\nY TEST SHAPE: {y_test.shape}')

# Create Ridge linear regression predictor for modelling
from sklearn.linear_model import Ridge
regr = Ridge()
regr.fit(x_train, y_train)
print(f'\nPREDICTED TARGET VALUES:')
regr_predict = regr.predict(x_test)
print(*regr_predict[:10], sep='\n')
print(f'\nACTUAL TARGET VALUES:')
print(*y_test[:10], sep='\n')
print(f'\nPREDICTED TARGET MEAN:\n\n{regr_predict.mean()}')
print(f'\nACTUAL TARGET MEAN:\n\n{y_test.mean()}')

## Transformers

# Scale the data
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)
regre = Ridge()
regre.fit(x_train_scaled, y_train)
print(f'\nUSING SCALER PREDICTED TARGET VALUES:')
regre_predict = regre.predict(x_test_scaled)
print(*regre_predict[:10], sep='\n')
print(f'\nACTUAL TARGET VALUES:')
print(*y_test[:10], sep='\n')
print(f'\nUSING SCALAR PREDICTED TARGET MEAN:\n\n{regre_predict.mean()}')
print(f'\nACTUAL TARGET MEAN:\n\n{y_test.mean()}')

# # Vectorise data example
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
sentences = ["I love apples", "I love oranges", "I love fruits"]
vect = cv.fit_transform(sentences)
print(f'\nVECTOR FEATURE NAMES:')
print(*cv.get_feature_names_out(), sep='\n')
print (f'\nVECTORIZED DATA:')
print(*vect.toarray(), sep='\n')