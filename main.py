from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
import os

os.environ["GOOGLE_API_KEY"]="AIzaSyAH6A_uQy_Phff-n-5X2nHmWKw_52iJqqk"
tweet_template="Give me {number} tweets on {topic}"
tweet_prompt=PromptTemplate(template=tweet_template,input_variables=['number','topic'])
gemini_model=ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
chain=tweet_prompt|gemini_model



import streamlit as st
st.header("Tweet Generator")
st.subheader("Generate tweets using Generative AI")

topic = st.text_input("Topic",value="")
num_tweets = st.number_input("Nnumber of tweets", min_value=1, max_value=10, value=1, step=1)
if st.button("Generate"):
    tweets=chain.invoke({"number":num_tweets,"topic" :topic})

st.write(tweets.content)


