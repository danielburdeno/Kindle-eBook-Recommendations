import pandas as pd
import streamlit as st
import numpy as np
import pickle
import surprise

from surprise.prediction_algorithms import SVD
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler
from PIL import Image

# Header
header_image = Image.open('Images/ebooks.jpg')
st.image(header_image)

# Creating sidebar comments
st.sidebar.title('Kindle eBook Recommendations')

st.sidebar.caption('By [Daniel Burdeno](https://www.linkedin.com/in/daniel-burdeno-39a298ab/)')

# Load in appropriate DataFrames, user ratings
df_user = pd.read_csv('Data/df_user.csv', index_col=0)

# Meta data for collabortive filtering
df_meta = pd.read_csv('Data/meta5.csv', index_col='asin')
df_meta.drop(columns =['Unnamed: 0'], inplace=True)

# Meta data for content based
df_meta_all = pd.read_csv('Data/meta_all.csv', index_col='asin')
df_meta_all.drop(columns =['Unnamed: 0'], inplace=True)

# Document term matrix from tf-idf vectorizor
df_dtm = pd.read_parquet('Data/df_dtm.parquet')

# Import final collab model
collab_model = pickle.load(open('Model/collab_model.sav', 'rb'))

# Combine meta_all and dtm for content features dataframe
model_df = df_dtm.merge(df_meta_all, left_index=True, right_index=True)
model_df.drop(columns=['title', 'author', 'word_wise', 'lending'], inplace=True)
model_df = pd.get_dummies(model_df, columns=['genre'])
model_df.head()

# Def function using model to return recommendations
def user_recommend_books(reviewer_input, n_recs):
    not_reviewed = df_meta.copy()
    have_reviewed = list(df_user.loc[reviewer_input, 'asin'])
    not_reviewed = not_reviewed.drop(have_reviewed)
    not_reviewed.reset_index(inplace=True)
    not_reviewed['est_rating'] = not_reviewed['asin'].apply(lambda x: collab_model.predict(reviewer_input, x).est)
    not_reviewed.sort_values(by='est_rating', ascending=False, inplace=True)
    return not_reviewed.head(n_recs)

# Second function for content based recommendations
def book_review_recommend(book_input, n_recs2):
    y = np.array(model_df.loc[book_input]).reshape(1, -1)
    cos_sim = cosine_similarity(model_df, y)
    cos_sim = pd.DataFrame(data=cos_sim, index=model_df.index)
    cos_sim.sort_values(by = 0, ascending = False, inplace=True)
    results = cos_sim.head(n_recs2+1).index.values[1:]
    results_df = df_meta_all.loc[results]
    return results_df

st.sidebar.subheader('This recommendation system can make two forms of recommendations.')
st.sidebar.write('Existing reviewers looking for books they might enjoy.')
st.sidebar.write('Similiar books based on content.')

st.title("Books on Books on Books")
st.subheader("See the sidebar navigation for options")

page_names = ['Existing Reviewers', 'Similiar Books']
page = st.sidebar.radio('Navigation', page_names)

st.sidebar.caption('Please refer to my [Github](https://github.com/danielburdeno/Kindle-Recommendations) for a deeper look into the code.')

if page == 'Existing Reviewers':
    st.header("You chose the existing reviewer option.")
    reviewer_input = st.text_input("Please input your unique amazon reviewerID.")
    n_recs = st.number_input("Please enter the number of recommendations you would like.", max_value=20)
    rec_button = st.button("Get to reading!!")
    if rec_button:
        results = user_recommend_books(reviewer_input, n_recs)
        st.table(results)

else:
    st.header("You chose the similiar books option.")
    book_input = st.text_input("Please input a unique book product ID.")
    n_recs2 = st.number_input("Please enter the number of recommendations you would like.", max_value=20, key=2)
    book_button = st.button("Get to reading!!", key=2)
    if book_button:
        results2 = book_review_recommend(book_input, n_recs2)
        st.write(f"You entered the book {df_meta_all.loc[book_input, 'title']} by {df_meta_all.loc[book_input, 'author']}")
        st.table(results2)



#st.write('Existing Users!')

#reviewer_input = st.text_input("Please input your unique amazon reviewerID.")

#rec_button = st.button("Get to reading!!")

#st.write('Or find books based on similiar content.')

#book_input = st.text_input("Please input a unique book product ID.")

#book_button = st.button("Get to reading!!", key=2)

#if rec_button:
    

#if book_button:
    #results2 = book_review_recommend(book_input, n_recs)
    #st.write(f"You entered the book {df_meta_all.loc[book_input, 'title']} by {df_meta_all.loc[book_input, 'brand']}")
    #st.table(results2)
