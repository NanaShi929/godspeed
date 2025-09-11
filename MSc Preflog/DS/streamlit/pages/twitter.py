# import streamlit as st
# import pandas as pd
# import nltk
# from nltk.sentiment.vader import SentimentIntensityAnalyzer
# import matplotlib.pyplot as plt

# st.set_page_config(page_title="Sentiment Analysis with VADER", layout="wide")  # <-- wide layout

# nltk.download('vader_lexicon')

# st.title("Sentiment Analysis with VADER and Visualizations")

# uploaded_file = st.file_uploader("Upload CSV file with a 'text' column", type=["csv"])

# if uploaded_file:
#     df = pd.read_csv(uploaded_file)
    
#     if 'text' not in df.columns:
#         st.error("CSV must have a 'text' column.")
#     else:
#         sid = SentimentIntensityAnalyzer()
        
#         def analyze_sentiment(text):
#             scores = sid.polarity_scores(str(text))
#             return pd.Series([scores['neg'], scores['neu'], scores['pos'], scores['compound']])
        
#         df[['neg', 'neu', 'pos', 'compound']] = df['text'].apply(analyze_sentiment)
        
#         def get_sentiment_label(compound):
#             if compound >= 0.05:
#                 return 'positive'
#             elif compound <= -0.05:
#                 return 'negative'
#             else:
#                 return 'neutral'
        
#         df['sentiment'] = df['compound'].apply(get_sentiment_label)
        
#         st.subheader("Sentiment Analysis Result (First 10 rows)")
#         st.dataframe(df.head(10), width=0)  # width=0 means use full width available
        
#         # Calculate sentiment counts
#         sentiment_counts = df['sentiment'].value_counts()
    
#         st.subheader("Sentiment Distribution - Bar Chart")
#         st.bar_chart(sentiment_counts)
        
#         st.subheader("Sentiment Distribution - Pie Chart")
#         fig, ax = plt.subplots(figsize=(3, 3))  # smaller figure size
#         colors = ['#8BC34A', '#FFC107', '#F44336']
#         ax.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=90, colors=colors)
#         ax.axis('equal')
#         st.pyplot(fig)

# else:
#     st.info("Please upload a CSV file containing a 'text' column.")

import streamlit as st
import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

# Set wide layout
st.set_page_config(page_title="Sentiment Analysis with VADER", layout="wide")

# Download VADER lexicon
nltk.download('vader_lexicon')

st.title("Sentiment Analysis with VADER and Visualizations")

# File uploader
uploaded_file = st.file_uploader("Upload CSV file with a 'text' column", type=["csv"])


if uploaded_file:
    df = pd.read_csv(uploaded_file)

    if 'text' not in df.columns:
        st.error("CSV must have a 'text' column.")
    else:
        # Initialize VADER
        sid = SentimentIntensityAnalyzer()

        # Sentiment scoring
        def analyze_sentiment(text):
            scores = sid.polarity_scores(str(text))
            return pd.Series([scores['neg'], scores['neu'], scores['pos'], scores['compound']])

        df[['neg', 'neu', 'pos', 'compound']] = df['text'].apply(analyze_sentiment)

        # Sentiment labeling
        def get_sentiment_label(compound):
            if compound >= 0.05:
                return 'positive'
            elif compound <= -0.05:
                return 'negative'
            else:
                return 'neutral'

        df['sentiment'] = df['compound'].apply(get_sentiment_label)

        # Show data preview
        st.subheader("Sentiment Analysis Result (First 10 rows)")
        st.dataframe(df.head(10), width=0)

        # Count sentiment labels
        sentiment_counts = df['sentiment'].value_counts()

        # Pie chart
        left, center, right = st.columns([1, 2, 1])

        with center:
            st.subheader("Sentiment Distribution - Bar Chart")
            fig2, ax2 = plt.subplots(figsize=(5, 3))
            sentiment_counts.plot(kind='bar',  ax=ax2)
            ax2.set_ylabel("Count")
            ax2.set_xlabel("Sentiment")
            plt.tight_layout()
            st.pyplot(fig2, clear_figure=True)


        # Bar chart
     # Centered chart using 3 columns: empty - content - empty
        left, center, right = st.columns([1, 2, 1])

        with center:
            st.subheader("Sentiment Distribution - Pie Chart")
            fig1, ax1 = plt.subplots(figsize=(4, 4))
            colors = ['#8BC34A', '#FFC107', '#F44336']
            ax1.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=90, colors=colors)
            ax1.axis('equal')
            plt.tight_layout()
            st.pyplot(fig1, clear_figure=True)

else:
    st.info("Please upload a CSV file containing a 'text' column.")
