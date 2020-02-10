import streamlit as st

import spacy
from textblob import TextBlob   # For sentiment analysis

import nltk
nltk.download('punkt')

def text_analyzer(my_text):
	nlp = spacy.load('en_core_web_sm')
	docx = nlp(my_text)
	
	allData = [('Tokens: {}, \n Lemma: {}'.format(token.text, token.lemma_)) for token in docx]
	return allData
	
def entity_analyzer(my_text):
	nlp = spacy.load('en_core_web_sm')
	docx = nlp(my_text)
	
	ner = [ 'Tokens: {}, \n Entity: {}'.format(entity.text, entity.label_) for entity in docx.ents]
	return ner


def main():
	""" Simple EDA app"""
	st.title("Natural Langauge Processing with Spacy")

	# Tokenization
	if st.checkbox("Show Tokens and Lemma"):
		st.subheader("Tokenize Your Text")
		message = st.text_area("Enter Your Text", "Type Here")
		if st.button("Analyze"):
			nlp_result = text_analyzer(message)
			st.json(nlp_result)
		
	
	# NER
	if st.checkbox("Show Named Entity"):
		st.subheader("Extract Entities From Your Text")
		message = st.text_area("Enter Your Text", "Type Here", key="ner")
		if st.button("Extract"):
			entity_result = entity_analyzer(message)
			st.json(entity_result)
	
	# Sentiment Analysis
	if st.checkbox("Sentiment Analysis"):
		st.subheader("Sentiment of Your Text")
		message = st.text_area("Enter Your Text", "Type Here", key="sentiment")
		if st.button("Analyze", key = "sentiment"):
			blob = TextBlob(message)
			st.success(blob.sentiment)
	
	
	
	
if __name__ == "__main__":
	main()