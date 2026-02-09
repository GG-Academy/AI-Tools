positive_words = ["good", "great", "love", "excellent", "happy", "amazing"]
negative_words = ["bad", "hate", "terrible", "sad", "awful", "boring"]

def simple_sentiment(text):
    text = text.lower().split()
    score = 0

    for word in text:
        if word in positive_words:
            score += 1
        elif word in negative_words:
            score -= 1

    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    else:
        return "Neutral"

# Example
print(simple_sentiment("I love this amazing course"))   # Positive
print(simple_sentiment("This lecture is boring and bad"))  # Negative
