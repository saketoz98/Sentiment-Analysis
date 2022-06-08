# Sentiment-Analysis

### Steps to run the project
1. Clone "main" branch
2. Move into root directory and open the terminal.
3. Execute - ```pip install -r requirements.txt``` to install all the required packages. (You may execute this command by creating and activating virtual environment on your machine)
4. This project uses Google Cloud NLP Sentiment Analysis Model to predict the sentiments of the articles. To use the GCP API, you need to get API credentials (keys)
5. Follow the steps given in the GCP documentation to generate API key - https://cloud.google.com/natural-language/docs/reference/libraries. Follow the steps till you export the path of credntials file in the terminal. (export GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH")
6. In the terminal, run ```python3 sentimentAnalysis.py```

### Summary
#### articles.json file -
1. File contains the details of the articles extracted from the https://www.aljazeera.com/where/mozambique/ website and result of the sentiment analysis performed on these articles. 
2. Attributes:
   url - URL of the article <br />
   content - Content of the article extracted using beautifulsoup python library. <br />
   sentimentScore - Sentiment Score predicted by GCP Sentiment Analysis model. <br />
   overallSentiment - Based on the predicted score, article is categorized into "Positive", "Negative" and "Neutral" sentiments.
3. overallSentiment is calculated using following logic:
   sentimentScore > 0.2 - Positive <br />
   sentimentScore < -0.2 - Negative <br />
   sentimentScore >= -0.2 and sentimentScore <= 0.2 - Neutral <br />
