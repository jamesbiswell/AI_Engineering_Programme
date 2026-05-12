from transformers import pipeline
from datasets import load_dataset
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load the model
print("Loading model...")
classifier = pipeline("sentiment-analysis",
                     model="distilbert-base-uncased-finetuned-sst-2-english")

print ("Model loaded successfully!\n")

# Load IMDB dataset (we'll use a small subset for speed)
print("Loading dataset...")
dataset = load_dataset("imdb", split="test[:500]")  # First 500 test examples
dataset  = dataset.shuffle (seed=42)

# Function to predict on batch
def predict_sentiment(texts, batch_size=32):
    predictions = []
    for i in range(0, len(texts), batch_size):
        print(i)
        batch = texts[i:i + batch_size]
        results = classifier(batch, truncation=True, max_length=512)
        predictions.extend(results)
    return predictions

# Get predictions
print("Making predictions...")
texts = dataset['text']
predictions = predict_sentiment(texts)

# Convert predictions to binary (POSITIVE=1, NEGATIVE=0)
pred_labels = [1 if p['label'] == 'POSITIVE' else 0 for p in predictions]
true_labels = dataset['label']

# Evaluate
accuracy = accuracy_score(true_labels, pred_labels)
print(f"\nAccuracy: {accuracy:.4f}")
print("\nClassification Report:")
print(classification_report(true_labels, pred_labels,
                            target_names=['Negative', 'Positive']))

# Show some examples
print("\n--- Example Predictions ---")
for i in range(5):
    print(f"\nReview: {texts[i][:200]}...")
    print(f"True: {'Positive' if true_labels[i] == 1 else 'Negative'}")
    print(f"Predicted: {predictions[i]['label']} (confidence: {predictions[i]['score']:.3f})")

# Interactive testing
def analyze_custom_text():
    print("\n" + "=" * 50)
    print("Custom Sentiment Analysis")
    print("=" * 50)
    print("Enter movie reviews to analyze (or 'quit' to exit)\n")

    while True:
        user_input = input("Enter review: ").strip()
        if user_input.lower() == 'quit':
            break

        if user_input:
            result = classifier(user_input)[0]
            print(f"Sentiment: {result['label']}")
            print(f"Confidence: {result['score']:.2%}\n")

analyze_custom_text()