import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def sentiment_analysis(text_list):
    nltk.download('vader_lexicon')

    #Sentiment Analysis
    def percentage(part,whole):
      return 100 * float(part)/float(whole)

    #Assigning Initial Values
    positive = 0
    negative = 0
    neutral = 0
    #Creating empty lists
    neutral_list = []
    negative_list = []
    positive_list = []

    #Iterating over the tweets in the dataframe
    for text in text_list:
        analyzer = SentimentIntensityAnalyzer().polarity_scores(text)
        neg = analyzer['neg']
        neu = analyzer['neu']
        pos = analyzer['pos']
        comp = analyzer['compound']

        if neg > pos:
            negative_list.append(text) #appending the text that satisfies this condition
            negative += 1 #increasing the count by 1
        elif pos > neg:
            positive_list.append(text) #appending the text that satisfies this condition
            positive += 1 #increasing the count by 1
        elif pos == neg:
            neutral_list.append(text) #appending the text that satisfies this condition
            neutral += 1 #increasing the count by 1 

    positive = percentage(positive, len(text_list)) #percentage is the function defined above
    negative = percentage(negative, len(text_list))
    neutral = percentage(neutral, len(text_list))

    return positive, neutral, negative
