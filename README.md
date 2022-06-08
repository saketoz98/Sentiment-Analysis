# Sentiment-Analysis

### Steps to run the project
1. Clone "main" branch
2. Move into root directory and open the terminal.
3. Execute - ```pip3 install -r requirements.txt``` to install all the required packages. (You may execute this command by creating and activating virtual environment on your machine)
4. This project uses Google Cloud NLP Sentiment Analysis Model to predict the sentiments of the articles. To use the GCP API, you need to get API credentials (keys)
5. Follow the steps given in the GCP documentation to generate API key - https://cloud.google.com/natural-language/docs/reference/libraries. Follow the steps till you export the path of credentials file in the terminal. (export GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH")
6. In the terminal, run ```python3 sentimentAnalysis.py```

### Summary of the project files
#### **articles.json**
1. File contains the details of the articles extracted from the https://www.aljazeera.com/where/mozambique/ website and result of the sentiment analysis performed on these articles. 
2. Attributes: <br />
   **url** - URL of the article <br />
   **content** - Content of the article extracted using beautifulsoup python library. <br />
   **sentimentScore** - Sentiment Score predicted by GCP Sentiment Analysis model. [Range: -1 (Negative)  to 1 (Positive)] <br />
   **overallSentiment** - Based on the predicted score, article is categorized into "Positive", "Negative" and "Neutral" sentiments.
3. overallSentiment is calculated using the following logic: <br />
   sentimentScore > 0.2 - Positive <br />
   sentimentScore < -0.2 - Negative <br />
   sentimentScore >= -0.2 and sentimentScore <= 0.2 - Neutral <br />

#### **sentimentAnalysis.py**
1. This is the main file which has the code to perform the web scrapping using beautifulsoup and predict the sentiment of the extracted articles.

#### **visualization.py**
1. This includes the code to visualize the predicted sentiments of the articles using plotly visualization library.

#### **Visualizations Folder**
1. The folder contains the screenshot of the Bar Chart showing articles with their sentiment score and categorization.

### Summary of the Results
1. Articles Scrapped from Web - 10
2. GCP Sentiment Analysis model predicts 3 "Neutral" and 7 "Negative" Sentiments. Results are documented in articles.json and visualization graphs.