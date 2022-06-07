from bs4 import BeautifulSoup
from google.cloud import language_v1
from tqdm import tqdm
import pandas as pd
import plotly.express as px
import requests
import json

def getSentimentOfDocument(content):
    client = language_v1.LanguageServiceClient()
    document = language_v1.Document(
        content=content, type_=language_v1.Document.Type.PLAIN_TEXT
        )
    sentiment = client.analyze_sentiment(
        request={"document": document}
        ).document_sentiment
    return sentiment

def categorizeSentimentResult(sentiment):
    score = sentiment.score

    if score >= 0.3:
        return 'Positive'
    elif score <= -0.3:
        return 'Negative'
    else:
        return 'Neutral'

def visualizeResults(result):
    df = pd.DataFrame(result)
    print(df)
    fig = px.bar(df, x='overallSentiment', y='pop', height=400)
    fig.show()
    pass


if __name__ == "__main__":

    HOST = "https://www.aljazeera.com/"

    html_text = requests.get('https://www.aljazeera.com/where/mozambique/').text
    soup = BeautifulSoup(html_text, 'lxml')
    articles = soup.find_all("a", class_="u-clickable-card__link")


    result = []

    for article in tqdm(articles, desc="Extract Articles from Web"):
        articleLink = article["href"]
        url = HOST + articleLink
        articleHtmlText = requests.get(url).text
        articleParsedHtml = BeautifulSoup(articleHtmlText, 'lxml')
        articleContent = articleParsedHtml.find("div", class_="wysiwyg wysiwyg--all-content css-1ck9wyi")
        if articleContent is not None:
            text = ""
            paragraphs = articleContent.find_all("p")
            if paragraphs is not None:
                for para in tqdm(paragraphs, desc="Extract Content of Paragraphs from Articles"):
                    text += para.getText()
            articleJson = dict()
            articleJson['url'] = url
            articleJson['content'] = text

            predictedSentiment = getSentimentOfDocument(text)
            sentimentCategoricalValue = categorizeSentimentResult(predictedSentiment)
            articleJson['sentimentScore'] = predictedSentiment.score
            articleJson['overallSentiment'] = sentimentCategoricalValue
            result.append(articleJson)
    visualizeResults(result)
    
    with open('articles.json', 'w') as f:
        json.dump(result, f, indent=2)







    
