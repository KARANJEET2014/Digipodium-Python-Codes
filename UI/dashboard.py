import pandas as pd
import plotly.express as px
import streamlit as st


#load data

def load_titanic_data():
    return pd.read_csv('UI/titanic.csv')

#clean data (optional)

def clean_data(df):
    df.drop(columns = ['Cabin'], inplace = True)
    df['Age'].fillna(df['Age'].mean(), inplace = True)
    return df

#display

with st.spinner("Loading dataset..."):
    titanic = load_titanic_data()
    titanic = clean_data(titanic)

st.dataframe(titanic)

#visualize

selected_col = st.selectbox('Select a Column', titanic.columns.tolist())
st.metric(f'column: {selected_col}', str(titanic[selected_col].dtype), titanic[selected_col].nunique())

st.write(titanic[selected_col])

#streamlit run UI/dashboard.py ----- to run the program
