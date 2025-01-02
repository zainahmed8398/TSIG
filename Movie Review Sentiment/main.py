# import requests
# from bs4 import BeautifulSoup
# import streamlit as st
# import pickle
# from sklearn.feature_extraction.text import TfidfVectorizer
# import re
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize
# import pandas as pd
# import matplotlib.pyplot as plt
# import nltk

# # Download necessary NLTK data
# nltk.download('punkt')
# nltk.download('stopwords')

# # Define headers for requests
# HEADERS = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
#     "Accept-Language": "en-US,en;q=0.9",
# }

# # Function to search for IMDb page using Google
# def search_imdb_google(movie_name):
#     query = f"site:imdb.com {movie_name}"
#     google_search_url = f"https://www.google.com/search?q={query}"
#     response = requests.get(google_search_url, headers=HEADERS)
#     soup = BeautifulSoup(response.text, 'html.parser')

#     for link in soup.find_all('a', href=True):
#         href = link['href']
#         if "https://www.imdb.com/title/" in href:
#             imdb_link = href.split("&")[0]  # Extract IMDb link
#             imdb_link = imdb_link.replace("/url?q=", "")  # Clean up URL
#             return imdb_link

#     return None

# # Function to scrape user reviews from IMDb
# def scrape_imdb_reviews(imdb_url):
#     reviews_url = f"{imdb_url}reviews"
#     response = requests.get(reviews_url, headers=HEADERS)
#     soup = BeautifulSoup(response.text, 'html.parser')

#     reviews = []
#     for review_div in soup.find_all('div', class_='text show-more__control'):
#         reviews.append(review_div.text.strip())

#     return reviews

# # Preprocess reviews for the model
# def preprocess_reviews(reviews):
#     stop_words = set(stopwords.words('english'))
#     processed_reviews = []
#     for review in reviews:
#         review = re.sub(r'[^\w\s]', '', review.lower())
#         words = word_tokenize(review)
#         filtered_words = [word for word in words if word not in stop_words]
#         processed_reviews.append(' '.join(filtered_words))
#     return processed_reviews

# # Streamlit app
# def main():
#     st.title("IMDb Movie Sentiment Analyzer")
#     st.write("Enter a movie name to analyze the sentiment of its user reviews on IMDb.")

#     # Load pre-trained model and vectorizer
#     with open("model.pkl", "rb") as model_file:
#         model = pickle.load(model_file)
#     with open("scaler.pkl", "rb") as vectorizer_file:
#         vectorizer = pickle.load(vectorizer_file)

#     # Input movie name
#     movie_name = st.text_input("Enter the movie name:")

#     if st.button("Analyze Sentiments"):
#         if not movie_name:
#             st.warning("Please enter a movie name.")
#             return

#         st.info(f"Searching IMDb for '{movie_name}'...")
#         imdb_url = search_imdb_google(movie_name)

#         if not imdb_url:
#             st.error("Could not find the IMDb page for the given movie.")
#             return

#         st.success(f"Found IMDb page: {imdb_url}")
#         st.info("Scraping user reviews...")

#         # Scrape reviews
#         reviews = scrape_imdb_reviews(imdb_url)

#         if not reviews:
#             st.warning("No user reviews found for this movie.")
#             return

#         st.success(f"Scraped {len(reviews)} reviews.")
#         st.info("Analyzing sentiments...")

#         # Preprocess and classify reviews
#         processed_reviews = preprocess_reviews(reviews)
#         transformed_reviews = vectorizer.transform(processed_reviews).toarray()
#         predictions = model.predict(transformed_reviews)

#         # Count positive and negative reviews
#         positive_count = sum(predictions)
#         negative_count = len(predictions) - positive_count

#         # Display results
#         st.write(f"**Positive Reviews:** {positive_count}")
#         st.write(f"**Negative Reviews:** {negative_count}")

#         # Plot pie chart
#         sentiment_counts = pd.DataFrame({
#             "Sentiment": ["Positive", "Negative"],
#             "Count": [positive_count, negative_count]
#         })

#         fig, ax = plt.subplots()
#         ax.pie(sentiment_counts["Count"], labels=sentiment_counts["Sentiment"], autopct='%1.1f%%', startangle=90, colors=["#4CAF50", "#F44336"])
#         ax.axis("equal")  # Equal aspect ratio ensures the pie chart is circular.
#         st.pyplot(fig)

# if __name__ == "__main__":
#     main()



# import requests
# from bs4 import BeautifulSoup
# import streamlit as st
# import pickle
# from sklearn.feature_extraction.text import TfidfVectorizer
# import re
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize
# import pandas as pd
# import matplotlib.pyplot as plt
# import nltk

# # Download necessary NLTK data
# nltk.download('punkt')
# nltk.download('stopwords')

# # Define headers for requests
# HEADERS = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
#     "Accept-Language": "en-US,en;q=0.9",
# }

# # Function to search for IMDb page using Google
# def search_imdb_google(movie_name):
#     query = f"site:imdb.com {movie_name}"
#     google_search_url = f"https://www.google.com/search?q={query}"
#     response = requests.get(google_search_url, headers=HEADERS)
#     soup = BeautifulSoup(response.text, 'html.parser')

#     for link in soup.find_all('a', href=True):
#         href = link['href']
#         if "https://www.imdb.com/title/" in href:
#             imdb_link = href.split("&")[0]  # Extract IMDb link
#             imdb_link = imdb_link.replace("/url?q=", "")  # Clean up URL
#             return imdb_link

#     return None

# # Function to scrape user reviews from IMDb
# def scrape_imdb_reviews(imdb_url):
#     reviews_url = f"{imdb_url}reviews"
#     response = requests.get(reviews_url, headers=HEADERS)
#     soup = BeautifulSoup(response.text, 'html.parser')

#     reviews = []
#     for review_div in soup.find_all('div', class_='text show-more__control'):
#         reviews.append(review_div.text.strip())

#     return reviews

# # Preprocess reviews for the model
# def preprocess_reviews(reviews):
#     stop_words = set(stopwords.words('english'))
#     processed_reviews = []
#     for review in reviews:
#         review = re.sub(r'[^\w\s]', '', review.lower())
#         words = word_tokenize(review)
#         filtered_words = [word for word in words if word not in stop_words]
#         processed_reviews.append(' '.join(filtered_words))
#     return processed_reviews

# # Streamlit app
# def main():
#     st.title("IMDb Movie Sentiment Analyzer")
#     st.write("Enter a movie name to analyze the sentiment of its user reviews on IMDb.")

#     # Load pre-trained model and vectorizer
#     try:
#         with open("model.pkl", "rb") as model_file:
#             model = pickle.load(model_file)
#         with open("scaler.pkl", "rb") as vectorizer_file:
#             vectorizer = pickle.load(vectorizer_file)
#     except FileNotFoundError:
#         st.error("Model or vectorizer file not found. Ensure 'sentiment_model.pkl' and 'vectorizer.pkl' are in the working directory.")
#         return

#     # Input movie name
#     movie_name = st.text_input("Enter the movie name:")

#     if st.button("Analyze Sentiments"):
#         if not movie_name:
#             st.warning("Please enter a movie name.")
#             return

#         st.info(f"Searching IMDb for '{movie_name}'...")
#         imdb_url = search_imdb_google(movie_name)

#         if not imdb_url:
#             st.error("Could not find the IMDb page for the given movie.")
#             return

#         st.success(f"Found IMDb page: {imdb_url}")
#         st.info("Navigating to user reviews section...")

#         # Scrape reviews
#         reviews = scrape_imdb_reviews(imdb_url)

#         if not reviews:
#             st.warning("No user reviews found for this movie.")
#             return

#         st.success(f"Scraped {len(reviews)} reviews.")
#         st.info("Analyzing sentiments...")

#         # Preprocess and classify reviews
#         processed_reviews = preprocess_reviews(reviews)
#         transformed_reviews = vectorizer.transform(processed_reviews).toarray()
#         predictions = model.predict(transformed_reviews)

#         # Count positive and negative reviews
#         positive_count = sum(predictions)
#         negative_count = len(predictions) - positive_count

#         # Display results
#         st.write(f"**Positive Reviews:** {positive_count}")
#         st.write(f"**Negative Reviews:** {negative_count}")

#         # Plot pie chart
#         sentiment_counts = pd.DataFrame({
#             "Sentiment": ["Positive", "Negative"],
#             "Count": [positive_count, negative_count]
#         })

#         fig, ax = plt.subplots()
#         ax.pie(sentiment_counts["Count"], labels=sentiment_counts["Sentiment"], autopct='%1.1f%%', startangle=90, colors=["#4CAF50", "#F44336"])
#         ax.axis("equal")  # Equal aspect ratio ensures the pie chart is circular.
#         st.pyplot(fig)

# if __name__ == "__main__":
#     main()




import requests
from bs4 import BeautifulSoup
import streamlit as st
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pandas as pd
import matplotlib.pyplot as plt
import nltk

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Define headers for requests
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

# Function to search for IMDb user reviews using Google
def search_imdb_user_reviews_google(movie_name):
    query = f"site:imdb.com {movie_name} User reviews"
    google_search_url = f"https://www.google.com/search?q={query}"
    response = requests.get(google_search_url, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')

    for link in soup.find_all('a', href=True):
        href = link['href']
        if "https://www.imdb.com/title/" in href and "/reviews" in href:
            imdb_reviews_link = href.split("&")[0]  # Extract IMDb reviews link
            imdb_reviews_link = imdb_reviews_link.replace("/url?q=", "")  # Clean up URL
            return imdb_reviews_link

    return None

# Function to scrape user reviews from IMDb
def scrape_imdb_reviews(imdb_reviews_url):
    response = requests.get(imdb_reviews_url, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')

    reviews = []
    # Adjusted logic to locate review containers
    for review_heading in soup.find_all('h3'):
      reviews.append(review_heading.text)

    return reviews

# Preprocess reviews for the model
def clean_review(reviews):
    """
    Cleans a single review by removing HTML, non-alphabet characters, and extra spaces.
    """
    cleaned_reviews =[]
    for text in reviews:
      text = text.lower()
      text = re.sub(r'<.*?>', '', text)  # Remove HTML tags
      text = re.sub(r'[^a-z\s]', '', text)  # Remove non-alphabet characters
      text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
      text = text.strip()
      cleaned_reviews.append(text)
    return cleaned_reviews

# Preprocess reviews for the model
# def preprocess_reviews(reviews):
#     """
#     Preprocess a list of reviews by cleaning each review and removing stopwords.
#     """
#     stop_words = set(stopwords.words('english'))
#     processed_reviews = []
#     for review in reviews:
#         cleaned_review = clean_review(review)
#         words = word_tokenize(cleaned_review)
#         filtered_words = [word for word in words if word not in stop_words]
#         processed_reviews.append(' '.join(filtered_words))
#     return processed_reviews

# Streamlit app
def main():
    st.title("IMDb Movie Sentiment Analyzer")
    st.write("Enter a movie name to analyze the sentiment of its user reviews on IMDb.")

    # Load pre-trained model and vectorizer
    try:
        with open("model.pkl", "rb") as model_file:
            model = pickle.load(model_file)
        with open("scaler.pkl", "rb") as vectorizer_file:
            vectorizer = pickle.load(vectorizer_file)
    except FileNotFoundError:
        st.error("Model or vectorizer file not found. Ensure 'sentiment_model.pkl' and 'vectorizer.pkl' are in the working directory.")
        return

    # Input movie name
    movie_name = st.text_input("Enter the movie name:")

    if st.button("Analyze Sentiments"):
        if not movie_name:
            st.warning("Please enter a movie name.")
            return

        st.info(f"Searching IMDb User Reviews for '{movie_name}'...")
        imdb_reviews_url = search_imdb_user_reviews_google(movie_name)

        if not imdb_reviews_url:
            st.error("Could not find the IMDb User Reviews page for the given movie.")
            return

        st.success(f"Found IMDb User Reviews page: {imdb_reviews_url}")
        st.info("Scraping user reviews...")

        # Scrape reviews
        reviews = scrape_imdb_reviews(imdb_reviews_url)

        if not reviews:
            st.warning("No user reviews found for this movie.")
            return

        st.success(f"Scraped {len(reviews)} reviews.")
        st.info("Analyzing sentiments...")

        # Preprocess and classify reviews
        processed_reviews = clean_review(reviews)
        transformed_reviews = vectorizer.transform(processed_reviews).toarray()
        predictions = model.predict(transformed_reviews)

        # Count positive and negative reviews
        positive_count = sum(predictions)
        negative_count = len(predictions) - positive_count

        # Display results
        st.write(f"**Positive Reviews:** {positive_count}")
        st.write(f"**Negative Reviews:** {negative_count}")

        # Plot pie chart
        sentiment_counts = pd.DataFrame({
            "Sentiment": ["Positive", "Negative"],
            "Count": [positive_count, negative_count]
        })

        fig, ax = plt.subplots()
        ax.pie(sentiment_counts["Count"], labels=sentiment_counts["Sentiment"], autopct='%1.1f%%', startangle=90, colors=["#4CAF50", "#F44336"])
        ax.axis("equal")  # Equal aspect ratio ensures the pie chart is circular.
        st.pyplot(fig)

if __name__ == "__main__":
    main()
