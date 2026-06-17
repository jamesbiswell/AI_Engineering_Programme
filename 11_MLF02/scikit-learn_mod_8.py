from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

## Load data and split - always done outside the pipeline
iris = load_iris()
x, y = iris.data, iris.target
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

## Manual

# Step 1: Scale manually
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

# Step 2: Train model
model = LogisticRegression(max_iter=1000)
model.fit(x_train_scaled, y_train)

# Step 3: Evaluate
model_y_pred = model.predict(x_test_scaled)
print(f'Manual Accuracy: {accuracy_score(y_test, model_y_pred)}')


## Pipeline
from sklearn.pipeline import Pipeline

# Create the pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LogisticRegression(max_iter=1000))
])

print(f'Pipeline: {pipeline}')
print(f'Pipeline steps: {pipeline.steps}')
print(f'Pipeline named steps: {pipeline.named_steps}')
print(f'Pipeline features: {pipeline.get_params().keys()}')

# Train the pipeline
pipeline.fit(x_train, y_train)

# Evaluate the pipeline
pipe_y_pred = pipeline.predict(x_test)
print('Pipeline Accuracy: ', accuracy_score(y_test, pipe_y_pred))


## Pipeline cross-validation example
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

pipe = make_pipeline(StandardScaler(), RandomForestClassifier(random_state=42))

iris = load_iris()
x, y = iris.data, iris.target
scores = cross_val_score(pipe, x, y, cv=5)
print(f'Cross-validation scores: {scores}')
print(f'Mean cross-validation score (accuracy): {scores.mean()}')