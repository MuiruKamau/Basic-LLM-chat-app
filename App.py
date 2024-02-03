import streamlit as st
import random
import time

# Streamed response generator
def response_generator():
    response = random.choice([ "Hello there! How can I assist you today?",
            "Hi, human! Is there anything I can help you with?",
            "Do you need help?",
                               ]
                            ) 
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

st.title('Simple Chat')

#initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

#Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#React to user input
if prompt := st.chat_input("What is up?"):
    #Add user message to chat history  
    st.session_state.messages.append({"role": "user", "content": prompt})
    #Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)  
    
  
response = f"Echo: {prompt}"
#Display bot response in chat message container
with st.chat_message("assistant"):
    st.markdown(response)
#Add bot response to chat history
st.session_state.messages.append({"role": "assistant", "content": response})

#Streamed response emulator


        
# Display assistant response in chat message container
with st.chat_message("assistant"):
    for word in response_generator():
        st.write(word, end="")
        time.sleep(0.05)
# Add assistant response to chat history
st.session_state.messages.append({"role": "assistant", "content": response})