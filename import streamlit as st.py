 import streamlit as st
import pickle
import pandas as pd

similarity = pickle.load(open('similarity.pkl', 'rb'))
product = pd.read_csv('new_df_recom.csv')

def recommend(product_name):
    product_index = product[product['Product Name'] == product_name].index[0]
    distances = similarity[product_index]
    product_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_products = []
    recommended_product_posters = []
    for i in product_list:
        prod_name = product.iloc[i[0]]['Product Name']
        
        recommended_products.append(prod_name)
        prod_poster = product.iloc[i[0]]['Image']
        recommended_product_posters.append(prod_poster)
    return recommended_products, recommended_product_posters


st.title('Product Recommendation System')

selected_product_name = st.selectbox(
'How would you like to be contacted?',
product['Product Name'].values)

if st.button('Recommend'):
    names,posters = recommend(selected_product_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        #st.header(names[0])
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])