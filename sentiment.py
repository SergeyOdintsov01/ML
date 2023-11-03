from transformers import pipeline

classifier = pipeline("sentiment-analysis","blanchefort/rubert-base-cased-sentiment")
print(classifier("Я ненавижу инженерию машинного обучения!"))

