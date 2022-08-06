from transformers import pipeline

def sentiment_analysis(data):
    if len(data) == 0:
        return 0

    positive = 0
    negative = 0
    neutral = 0

    #Sentiment Analysis
    def percentage(part,whole):
      return 100 * float(part)/float(whole)

    sentiment_pipeline = pipeline("sentiment-analysis")
    results = sentiment_pipeline(data)

    for res in results:
        if res['label'] == 'POSITIVE':
            positive += 1
        elif res['label'] == 'NEGATIVE':
            negative += 1
        else:
            neutral += 1

    positive = percentage(positive, len(data)) #percentage is the function defined above
    negative = percentage(negative, len(data))
    neutral = percentage(neutral, len(data))

    return positive, neutral, negative
