'''
In this exercise, you will perform part-of-speech tagging on a famous passage from one of the most well-known novels of all time, Lord of the Flies, authored by William Golding.

The passage is available as lotf and has already been printed to the console.
'''

# Load the en_core_web_sm model
nlp = spacy.load('en_core_web_sm')
 
# Create a Doc object
doc = nlp(lotf)
 
# Generate tokens and pos tags
pos = [(token.text, token.pos_) for token in doc]
print(pos)
