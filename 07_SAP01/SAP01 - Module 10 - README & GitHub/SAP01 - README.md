# Movie Review Sentiment Analysis with DistilBERT

---

An AI-powered sentiment analysis tool that classifies movie reviews as positive or negative. This project uses DistilBERT as a base model, fine-tuned on custom data to understand modern slang and contemporary language patterns.

## Features

---

- **Pre-trained DistilBERT Model:** Leverages the power of transformer-based language models
- **Fine-tuned for Modern Language:** Custom training on movie reviews including modern slang and colloquialisms
- **Confidence Scoring:** Provides probability scores for prediction confidence
- **Dual Interface:** Available as both CLI and web-based Streamlit application
- **Comprehensive Evaluation:** Includes accuracy metrics, classification reports, and confusion matrix visualizations

## Handling Long Reviews

---

DistilBERT has a 512-token limit. For longer reviews, the following strategies are recommended:

**Sliding Window Approach**
- Process the review in overlapping chunks of 512 tokens
- Aggregate predictions from each chunk (voting or averaging confidence scores)
- Provides more comprehensive sentiment analysis for long reviews

**Alternative Model Architectures**

| Model | Benefit |
|---|---|
| Longformer | Supports up to 4,096 tokens |
| BigBird | Efficient attention for longer sequences |
| Hierarchical models | Process paragraph-level sentiments then aggregate |

**Smart Truncation Strategies**
- Keep first and last N tokens (capture introduction and conclusion)
- Attention-based selection of the most relevant sentences
- Summary-based preprocessing before classification

## Future Improvements

---

- Implement a sliding window approach for long reviews
- Add neutral sentiment classification
- Support for multi-language reviews
- Aspect-based sentiment analysis (acting, plot, cinematography)
- API endpoint for integration with other applications
- Mobile-responsive design improvements
- Evaluate alternative models (Longformer, BigBird) for longer text support

## Requirements

---

```
streamlit
transformers
torch
datasets
scikit-learn
pandas
numpy
```

## Model Information

---

| Property | Value |
|---|---|
| Base Model | distilbert-base-uncased-finetuned-sst-2-english |
| Task | Binary Sentiment Classification |
| Labels | POSITIVE / NEGATIVE |
| Max Token Length | 512 |
| Framework | Hugging Face Transformers |

## Acknowledgements

---

- [Hugging Face](https://huggingface.co) for the Transformers library and pre-trained models
- [Streamlit](https://streamlit.io) for the web application framework
- [IT Online Learning](https://itonlinelearning.com) for the project development and training materials
- [IT Online Learning GitHub](https://github.com/ITonlinelearning-code/sentiment-analysis-project) for the example code