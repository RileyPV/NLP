from textblob import TextBlob

text = "Today is a beautiful day. Tomorrow looks like bad weather."

blob = TextBlob(text)

#print(blob)

sentences = blob.sentences

#print(sentences)

words = blob.words

#print(words)

#print(blob.tags)

#print(blob.noun_phrases)

print(blob.sentiment.polarity)
print(blob.sentiment.subjectivity)

#Display polarity of each sentence

for i in sentences:
    print(round(i.sentiment.polarity,3))

from textblob.sentiments import NaiveBayesAnalyzer

blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())

print(blob.sentiment)

print(blob.sentiment.classification)


for i in blob.sentences:
    print(i.sentiment)

spanish = blob.translate(to='es')

print(spanish)

chinese = blob.translate(to='zh')

print(chinese)

french = blob.translate(to='fr')

print(french)

hindi = blob.translate(to='hi')

print(hindi)

nepal = blob.translate(to='ne')

print(nepal)

english = nepal.translate(to='en')

print(english)

#Change plural words to singular
from textblob import Word
index = Word('index')


#Change singular to plural
cacti = Word('cacti')

print(index.pluralize())

print(cacti.singularize())

#wordlist
animals = TextBlob('dog cat fish bird').words
print(animals.pluralize())

#spellcheck and corrections
word = Word('theyr')

print(word.spellcheck())

print(word.correct())

#from nltk.stem import WordNetLemmatizer

word1 = Word('studies')
word2 = Word('varieties')

print(word1.stem())
print(word2.stem())

#print(word1.lemmatize())
#print(word2.lemmatize())

happy = Word('happy')
#print(happy.definitions)
print(happy.synsets)

