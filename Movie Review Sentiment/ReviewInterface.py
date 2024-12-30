import pandas as pd
import pickle as pkl
from sklearn.feature_extraction.text import TfidfVectorizer
import streamlit as st

model =pkl.load(open('model.pkl','rb'))
scaler =pkl.load(open('scaler.pkl','rb'))
review = st.text_input('Enter Movie Review')

if st.button('Predict'):
    review_scale =scaler.transform([review]).toarray()
    prediction = model.predict(review_scale)
    if prediction == 0:
        st.write('Negative Review')
    else:
        st.write('Positive Review')