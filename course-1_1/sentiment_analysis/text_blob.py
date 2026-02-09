# install first:
# pip install textblob

from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity   # range: -1 (negative) to +1 (positive)

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Example
texts = [
    "I love this course!",
    "This lecture was boring.",
    "The exam was okay."
]

for t in texts:
    print(t, "->", analyze_sentiment(t))
