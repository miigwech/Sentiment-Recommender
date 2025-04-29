import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pickle

# Load necessary data
pt = pickle.load(open('pt.pkl', 'rb'))
books = pickle.load(open('books.pkl', 'rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl', 'rb'))

def recommend(book_name):
    index = np.where(pt.index == book_name)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:5]
    
    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
        data.append(item)
    
    return data

# Streamlit UI
st.title('Book Recommendation System')

# Input for book title
book_title = st.text_input('Enter a book title:', 'The Da Vinci Code')

if st.button('Get Recommendations'):
    recommendations = recommend(book_title)
    if recommendations:
        st.write("Top 4 Recommended Books:")
        for rec in recommendations:
            st.write(f"Title: {rec[0]}")
            st.write(f"Author: {rec[1]}")
            st.image(rec[2], caption='Book Cover', use_column_width=True)
            st.write('---')
    else:
        st.write("No recommendations found.")
