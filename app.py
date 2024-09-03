import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np 



def load_data():
    file='aircrahesFullDataUpdated_2024 (1).csv'
    df = pd.read_csv(file)
    # filling up nan value with new and unknown
    df['Country/Region'] = df['Country/Region'].fillna('unknown')
    df['Operator'] = df['Operator'].fillna('unknown')
    # check for duplicate
    duplicate_count = df.duplicated().sum()
    print(duplicate_count)
    #merging year day and month
    df['Date'] = df['Year'].astype(str) + '-' + df['Month'].astype(str) + '-' + df['Day'].astype(str)
    # drop year month and date columns
    df.drop(['Year', 'Month', 'Day'],axis=1, inplace=True)
    return df

# load the dataset 
df = load_data()

# app title
st.title("ANALYSIS OF AIRCRASHES")


Total_Number_of_fatalities_from_1900_till_date  = df['Fatalities (air)'].sum()
Total_number_of_Ground_from_1900_till_date   = df['Ground'].sum()

st.subheader("Calculations")
col1, col2 = st.columns(2)

col1.metric("Total number of Fatalities",Total_Number_of_fatalities_from_1900_till_date )
col2.metric("Total number of  Ground", Total_number_of_Ground_from_1900_till_date)


st.write(df)

try:
    st.write("## Quarterly Fatalities")
    bar1 = df.groupby('Quarter')['Fatalities (air)'].sum()
    st.bar_chart(bar1)
except ValueError as e:
    st.error(
       """ Error: """ % e.reason
    )

st.write("### Quaterly Ground")
bar2 =df.groupby('Quarter')['Aboard'].sum()
st.bar_chart(bar2)

