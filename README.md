# Sentiment-Analysis

### Steps to run the project
1. Clone "main" branch
2. Move into root directory and open the terminal.
3. Execute - ```pip install -r requirements.txt``` to install all the required packages
4. This project uses Google Cloud NLP Sentiment Analysis Model to predict the sentiments of the articles. To use the GCP API, you need to get API credentials (keys)
5. Follow the steps given in the GCP documentation to generate API key - https://cloud.google.com/natural-language/docs/reference/libraries. Follow the steps till you export the path of credntials file in the terminal. (export GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH")
6. In the terminal, run ```python3 sentimentAnalysis.py```
