import nltk
import os

os.makedirs("data", exist_ok=True)

text_file = "data/gutenberg_sentences.txt"


nltk.download('gutenberg')
nltk.download('punkt')
books = nltk.corpus.gutenberg.fileids()
sentences = []
for book in books:
    for words in nltk.corpus.gutenberg.sents(book):
        sentences.append(" ".join(words))


with open(text_file, 'w') as f:
    f.writelines(sentences)