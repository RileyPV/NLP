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