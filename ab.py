import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Initialize the VADER sentiment analysis tool
sid = SentimentIntensityAnalyzer()

# Sample text for sentiment analysis
text = "I love this product! It's fantastic."

# Perform sentiment analysis
sentiment_scores = sid.polarity_scores(text)

# Output the sentiment scores
print(sentiment_scores)