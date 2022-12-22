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
    df['Survived'] = df['Survived'].apply(lamda x: 'Yes' if x==1 else 'No') # to plot zero values properly in the graph
    return df

#display

with st.spinner("Loading dataset..."):
    titanic = load_titanic_data()
    titanic = clean_data(titanic)

if st.sidebar.checkbox('Show the Titanic Dataset'):
    st.header('Titanic Dataset')
    st.dataframe(titanic)

if st.sidebar.checkbox('View data types for each column'):
    st.header('Data types for each column')
    c1, c2, c3 = st.columns(3)
    total_cols = len(titanic.columns)
    for idx,col in enumerate(titanic.columns):
        if idx < total_cols/3:
            c1.metric(f'Column: {col}', f'Type: {titanic[col].dtype}', f'Unique: {titanic[col].nunique()}')

        elif idx < 2*total_cols/3:
            c2.metric(f'Column: {col}', f'Type: {titanic[col].dtype}', f'Unique: {titanic[col].nunique()}')

        else:
            c3.metric(f'Column: {col}', f'Type: {titanic[col].dtype}', f'Unique: {titanic[col].nunique()}')

if st.sidebar.checkbox('View summary statistics for each column'):
    st.header('Summary statistics for each column')
    st.dataframe(titanic.describe(include= 'all'), use_container_width = True)

st.header('Univariate Column Analysis')
goptions = ['bar', 'histogram', 'box', 'violin', 'scatter']
c1, c2 = st.columns(2)
selected_col = c1.selectbox('select a column', titanic.columns.tolist())
graph_type = c2.selectbox('select a graph type', goptions)

if graph_type == goptions[0]:
    fig = px.bar(titanic, x = selected_col)
elif graph_type == goptions[1]:
    fig = px.histogram(titanic, x = selected_col)
elif graph_type == goptions[2]:
    fig = px.box(titanic, x = selected_col)
elif graph_type == goptions[3]:
    fig = px.violin(titanic, x = selected_col)
elif graph_type == goptions[4]:
    fig = px.scatter(titanic, x = selected_col, y = 'Age')

st.plotly_chart(fig)


st.header('Bivariate Column Aanlysis')
goptions = ['scatter', 'box', 'violin']
c1, c2, c3 = st.columns(3)
sc1 = c1.selectbox('Select a column for X', titanic.columns.tolist())
sc2 = c2.selectbox('Select a column for Y', titanic.columns.tolist())
graph_type = c3.selectbox('Select a graph type', goptions)

try:
    if graph_type ==goptions[0]:
        fig = px.scatter(titanic, x=sc1, y=sc2)
    elif graph_type == goptions[1]:
        fig =px.box(titanic, x=sc1, y=sc2)
    elif graph_type == goptions[2]:
        fig = px.violin(titanic, x=sc1, y=sc2)
    st.plotly_chart(fig)

except Exception as e:
    st.error(f'Error: {e}')
    st.error('Please select a different column for X and Y')


st.header('Important Visualizations')

#Survival rate with respect to Passenger class

fig = px.bar(titanic, y = 'Pcalss', x= 'Survived', facet_col = 'Sex', color = 'Survived', title = 'Survival Rate with respect to Passenger class', color_discrete_sequence = px.colors.qualitative.dark24)

st.plotly_chart(fig)

#streamlit run UI/dashboard2.py -------- to run the code