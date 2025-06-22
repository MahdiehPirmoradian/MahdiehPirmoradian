# Semantic Similarity Search with BERT

This project demonstrates how to calculate semantic similarity between sentences using the BERT-based model `bert-base-nli-mean-tokens` with the help of the `sentence-transformers` library.

## 📌 Project Overview

The goal of this project is to:
- Encode multiple English sentences into vector representations.
- Calculate the **cosine similarity** between sentence embeddings to determine how semantically similar they are.

## 🔧 Technologies Used

- **Google Colab**: The project is built and run in Google Colab, which supports external libraries and provides an ideal environment for NLP and ML tasks.
- **sentence-transformers**: A Python framework that allows easy use of pre-trained models for sentence or text embedding.
- **scikit-learn**: Used for calculating cosine similarity between encoded sentence vectors.

## 🧠 Model

The following pre-trained model was used:
- `bert-base-nli-mean-tokens`: A sentence embedding model fine-tuned for semantic textual similarity tasks.

## 🚀 How It Works

1. Load the pre-trained BERT model.
2. Define a list of English sentences.
3. Encode these sentences into vector representations.
4. Use cosine similarity to compare how similar the first sentence is to all the others.

## 📄 Sample Sentences Used

- "A group of students is attending a lecture."
- "The weather is beautiful today."
- "I like to drink coffee today."
- "It's a lovely day outside."
- "The project was finished before the deadline."
- "She is studying British literature."
- "I have a dentist appointment tomorrow."

## 📈 Output

The cosine similarity scores indicate how close in meaning each sentence is to the first one, helping us identify which sentences are semantically related.

## 🔗 Access the Project

You can view and run the full notebook here:  
👉 [Open in Google Colab](https://colab.research.google.com/drive/1LWuPF_FJWIskiS3OxUPzugYLiiUlrdk3?usp=sharing)

## 📬 Contact

For questions or improvements, feel free to reach out or fork the notebook.

