from transformers import pipeline

classifier = pipeline("sentiment-analysis", device=0)
classifier("Good food")
print(classifier)