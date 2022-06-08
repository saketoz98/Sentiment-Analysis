import json

from bs4 import BeautifulSoup
from google.cloud import language_v1
from tqdm import tqdm
import requests

from visualization import *
from properties import NEWS_ARTICLE_HOST

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
    if sentiment.score >= 0.3:
        return "Positive"
    elif sentiment.score <= -0.3:
        return "Negative"
    else:
        return "Neutral"


if __name__ == "__main__":

    html_text = requests.get("https://www.aljazeera.com/where/mozambique/").text
    parsedHtml = BeautifulSoup(html_text, "lxml")
    articles = parsedHtml.find_all("a", class_="u-clickable-card__link")    #Anchor tags with given class name are news headlines 

    result = []

    for article in tqdm(articles, desc="Extract Articles from Web"):
        articleLink = article["href"]
        url = NEWS_ARTICLE_HOST + articleLink
        articleHtmlText = requests.get(url).text
        articleParsedHtml = BeautifulSoup(articleHtmlText, "lxml")
        articleContent = articleParsedHtml.find(
                            "div", 
                            class_="wysiwyg wysiwyg--all-content css-1ck9wyi")  #Content of the article is present inside the div with given class name
        if articleContent is not None:
            text = ""
            paragraphs = articleContent.find_all("p")
            if paragraphs is not None:
                for para in tqdm(paragraphs, desc="Extract Content of Paragraphs from Articles"):
                    text += para.getText()
            articleJson = dict()
            articleJson["url"] = url
            articleJson["content"] = text

            predictedSentiment = getSentimentOfDocument(text)
            sentimentCategoricalValue = categorizeSentimentResult(predictedSentiment)
            articleJson["sentimentScore"] = predictedSentiment.score
            articleJson["overallSentiment"] = sentimentCategoricalValue
            result.append(articleJson)
    
    visualizeResults(result)
    
    with open("articles.json", "w") as f:
        json.dump(result, f, indent=2)







    
