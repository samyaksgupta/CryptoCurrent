import streamlit as st

def main():
    st.title("Chatbot Simulator")

    # Create a placeholder for displaying the chat history
    chat_history_placeholder = st.empty()

    # Check if the user has submitted a message
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
                left: 100px;
                right: 100px;
                width: 90%;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

if __name__ == "__main__":
    main()
