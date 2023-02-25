import streamlit as st
import pandas as pd
import spacy
nlp = spacy.load("en_core_web_sm")

st.write("""
# FLAMES App

**For Fun Purpose only**
""")
text1=st.text_input('Enter Your Name')
text2=st.text_input('Enter Your Fiance Name')
st.button('Click me')
doc1=nlp(text1)
doc2=nlp(text2)
x=doc1.similarity(doc2)
st.write(x)
if x <= 0.1:
    st.write('Try Again')
elif x <= 0.2:
    st.write('Enemies')
elif x <= 0.3:
    st.write('Siblings')
elif x <= 0.4:
    st.write('Relatives')
elif x <= 0.5:
    st.write('Good Friends')
elif x <= 0.6:
    st.write('Crush')
elif x <= 0.7:
    st.write('Lover')
elif x <= 0.8:
    st.write('Marriage')
elif x <=0.9:
    st.write('True Love')
    
elif x == 1.0:
    st.write('Single')
    
    
else:
    st.write('Enter Proper Input')
