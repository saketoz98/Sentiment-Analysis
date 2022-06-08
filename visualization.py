import pandas as pd
import plotly.express as px

def visualizeResults(result):
    df = pd.DataFrame(result)
    df['content'] = df['content'].str.slice(0,40)

    fig = px.bar(df, x='content', y='sentimentScore', color="overallSentiment", 
        title="Article Sentiment Scores", text_auto=True)
    fig.show()
    pass