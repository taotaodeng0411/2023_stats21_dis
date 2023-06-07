import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

uploaded = st.file_uploader('Upload CSV file', type='csv')

if uploaded is not None:
    # Read CSV file into DataFrame
    df = pd.read_csv(uploaded)

    # Display DataFrame
    st.subheader('Data Display')
    st.write(df)

    # Data Summary
    st.subheader('Data Summary')
    st.write('Number of rows:', df.shape[0])
    st.write('Number of columns:', df.shape[1])
    st.write('Column names:', df.columns.tolist())
    st.write('Data type counts:')
    st.write(df.dtypes.value_counts())

    # Data Inspection
    st.subheader('Data Inspection')
    column = st.selectbox('Select a column', df.columns)
    values = df[column].unique()
    st.write('Unique values:', values)

    if df[column].dtype == 'object':
        st.write('Data Type: Categorical')
        st.write('Proportion of each category level:')
        counts = df[column].value_counts(normalize=True) * 100
        st.write(counts)

        # Bar plot
        plt.figure(figsize=(8, 6))
        sns.countplot(data=df, x=column)
        plt.xticks(rotation=45)
        st.pyplot(plt.gcf())

    else:
        st.write('Data Type: Numeric')
        st.write('Summary of Five Numbers:')
        st.write(df[column].describe()[['min', '25%', '50%', '75%', 'max']])

        # Distribution plot
        plt.figure(figsize=(8, 6))
        sns.histplot(data=df, x=column, kde=True)
        plt.xlabel(column)
        plt.ylabel('Count')
        st.pyplot(plt.gcf())   
