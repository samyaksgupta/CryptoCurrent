import streamlit as st
import requests
import pandas as pd

# Fetch data from CoinGecko API
def fetch_data():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=inr"
    response = requests.get(url)
    data = response.json()
    return data

# Convert data into DataFrame
def convert_to_dataframe(data):
    df = pd.DataFrame(data)
    return df

# Fetch and convert data
data = fetch_data()
df = convert_to_dataframe(data)

# Display data in Streamlit
st.title('Crypto Data from CoinGecko')

# Create three columns
left_column, middle_column, right_column = st.columns(3)

# Left Column: Display selected crypto data
selected_crypto = left_column.selectbox('Select Crypto', df['name'].unique())
selected_data = df[df['name'] == selected_crypto]
left_column.line_chart(selected_data['current_price'])

# Middle Column: Graph and Trending Section
mid_graph = middle_column.line_chart(df['current_price'])
mid_trending = middle_column.subheader('Trending Section')
# Add any trending information or analysis here based on your requirements

# Right Column: Most Famous Crypto
famous_crypto = df.nlargest(3, 'market_cap')
right_column.subheader('Most Famous Crypto In The Market')
right_column.dataframe(famous_crypto[['name', 'current_price', 'market_cap']])

# Display hot selling crypto
hot_selling_crypto = df.nlargest(5, 'total_volume')
st.subheader('Hot Selling Crypto')
st.dataframe(hot_selling_crypto[['name', 'current_price', 'total_volume']])
