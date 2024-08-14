pip install streamlit

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Iris dataset
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
    return pd.read_csv(url)

iris = load_data()

# Title of the app
st.title('Iris Dataset Visualizations')

# Sidebar for user inputs
st.sidebar.title('Navigation')
question = st.sidebar.selectbox('Choose a question to explore:', [
    'Show the Average Sepal Length for Each Species',
    'Display a Scatter Plot Comparing Two Features',
    'Filter Data Based on Species',
    'Display a Pairplot for the Selected Species',
    'Show the Distribution of a Selected Feature'
])

# Question 1: Show the Average Sepal Length for Each Species
if question == 'Show the Average Sepal Length for Each Species':
    st.header('Average Sepal Length for Each Species')
    avg_sepal_length = iris.groupby('species')['sepal_length'].mean()
    
    fig, ax = plt.subplots()
    avg_sepal_length.plot(kind='bar', color='skyblue', ax=ax)
    ax.set_title('Average Sepal Length for Each Species')
    ax.set_ylabel('Average Sepal Length')
    ax.set_xlabel('Species')
    st.pyplot(fig)

# Question 2: Display a Scatter Plot Comparing Two Features
elif question == 'Display a Scatter Plot Comparing Two Features':
    st.header('Scatter Plot Comparing Two Features')
    feature_x = st.selectbox('Select the first feature:', iris.columns[:-1])
    feature_y = st.selectbox('Select the second feature:', iris.columns[:-1])
    
    fig, ax = plt.subplots()
    ax.scatter(iris[feature_x], iris[feature_y], c='blue', alpha=0.5)
    ax.set_title(f'{feature_x} vs. {feature_y}')
    ax.set_xlabel(feature_x)
    ax.set_ylabel(feature_y)
    st.pyplot(fig)

# Question 3: Filter Data Based on Species
elif question == 'Filter Data Based on Species':
    st.header('Filter Data Based on Species')
    species = st.selectbox('Select the species:', iris['species'].unique())
    filtered_data = iris[iris['species'] == species]
    
    st.write(f'Data for {species}:')
    st.dataframe(filtered_data)

# Question 4: Display a Pairplot for the Selected Species
elif question == 'Display a Pairplot for the Selected Species':
    st.header('Pairplot for Selected Species')
    species = st.selectbox('Select the species for pairplot:', iris['species'].unique())
    filtered_data = iris[iris['species'] == species]
    
    fig = sns.pairplot(filtered_data)
    st.pyplot(fig)

# Question 5: Show the Distribution of a Selected Feature
elif question == 'Show the Distribution of a Selected Feature':
    st.header('Distribution of a Selected Feature')
    feature = st.selectbox('Select the feature:', iris.columns[:-1])
    
    fig, ax = plt.subplots()
    sns.histplot(iris[feature], kde=True, color='green', ax=ax)
    ax.set_title(f'Distribution of {feature}')
    ax.set_xlabel(feature)
    ax.set_ylabel('Frequency')
    st.pyplot(fig)
