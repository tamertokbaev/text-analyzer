from textblob import TextBlob


def analyze_text(text_content: str):
    analyzing_results = TextBlob(text_content)
    return {
        "polarity": analyzing_results.polarity,
        "subjectivity": analyzing_results.subjectivity
    }
