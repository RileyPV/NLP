#The file below is a list/dictionary object of the current top trending topics in New York City on Twitter.
#nyc_trends.py  Download nyc_trends.py 
from pathlib import Path
from textblob import Word
from wordcloud import WordCloud
import pandas as pd
import imageio
import matplotlib.pyplot as plt
import spacy
from nyc_trends import nyc_trends

#1) Using this information, create a bar chart of the top 10 topics based on their corresponding tweet volume.
volumes = []
topics = []
mylist = {}
for i in nyc_trends:
    for x in i['trends']:
        topic = x['name']
        volume = x['tweet_volume']
        if x['tweet_volume'] != None:
            volumes.append(volume)
            topics.append(topic)
            
for key in topics:
    for value in volumes:
        mylist[key] = value
        volumes.remove(value)
        break

#print(topics[:10],volumes[:10])
#print(mylist)

from operator import itemgetter
sorted_items = sorted(mylist.items(), key=itemgetter(1), reverse=True)
#, key=itemgetter(1), reverse=True)
print(sorted_items[:10])

top10 = sorted_items[:10]
print(top10)

df = pd.DataFrame(top10, columns=['Topics', 'Volume'])

print(df)
df.plot.bar(x='Topics',y='Volume')
plt.gcf().tight_layout()
plt.show()


#2) Create a Word Cloud of all topics with over 20,000 tweet volume. The size of the word (topic) should be based on their tweet volume.
mydict = dict()

for (key,value) in mylist.items():
    if value > 20000:
        mydict[key] = value

#print(len(mydict))
print(mydict)

wordcloud = WordCloud(colormap='prism',background_color='white')

wordlcoud = wordcloud.generate_from_frequencies(mydict)

wordcloud = wordcloud.to_file('NYC_TrendsCloud.png')

plt.imshow(wordcloud)
plt.show()
print('done')
