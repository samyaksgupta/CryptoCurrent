import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import requests

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

# Page configuration
st.set_page_config(
    page_title="Crypto Dashboard",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")

# Load data
data = fetch_data()
df = convert_to_dataframe(data)

# Sidebar
with st.sidebar:
    st.title('💰 Crypto Dashboard')

    crypto_list = list(df['name'].unique())
    selected_crypto = st.selectbox('Select Crypto', crypto_list)
    selected_crypto_data = df[df['name'] == selected_crypto]

    color_theme_list = ['blues', 'cividis', 'greens', 'inferno', 'magma', 'plasma', 'reds', 'rainbow', 'turbo', 'viridis']
    selected_color_theme = st.selectbox('Select a color theme', color_theme_list)

# Dashboard Main Panel
col = st.columns((1, 3, 2), gap='medium')

with col[0]:
    st.markdown('#### Selected Crypto Info')
    st.dataframe(selected_crypto_data)

with col[1]:
    st.markdown('#### Crypto Prices Over the Last 7 Days')
    
    # Sparkline chart for the last 7 days
    sparkline_chart = alt.Chart(selected_crypto_data).mark_line().encode(
        x='timestamp:T',
        y='current_price:Q',
        color=alt.Color('name:N', scale=alt.Scale(scheme=selected_color_theme)),
    ).properties(width=600, height=300)
    
    st.altair_chart(sparkline_chart)

with col[2]:
    st.markdown('#### Top Cryptos (INR)')

    top_cryptos = df.nlargest(5, 'market_cap')
    st.dataframe(top_cryptos[['name', 'current_price', 'market_cap']])

    with st.expander('About', expanded=True):
        st.write('''
            - Data: [CoinGecko API](https://www.coingecko.com/en/api).
            - :orange[**Selected Crypto Info**]: Detailed information about the selected cryptocurrency.
            - :orange[**Crypto Prices Over Time**]: Line chart showing the price trend of the selected cryptocurrency.
            - :orange[**Top Cryptos**]: Table displaying the top 5 cryptocurrencies based on market capitalization.
            ''')
user_input = st.text_input("User:", "Type your message here...")

if st.button("Submit"):
        # Process user input
        chatbot_response = simulate_chatbot_response(user_input)

        # Display chatbot response in the chat history
        chat_history = chat_history_placeholder.text_area("Chat History:", value="", height=400)
        chat_history += f"\nUser: {user_input}\nChatbot: {chatbot_response}"
        chat_history_placeholder.text(chat_history)

    # Use custom CSS to fix the position of the chatbot input at the bottom
st.markdown(
        """
        <style>
            .stTextInput {
                position: fixed;
                bottom: 10px;
                right: 10;
                width: 50%;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
