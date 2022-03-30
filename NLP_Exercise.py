#The file below is a list/dictionary object of the current top trending topics in New York City on Twitter.
#nyc_trends.py  Download nyc_trends.py 

from pathlib import Path
from textblob import Word
from wordcloud import WordCloud
import imageio
import matplotlib.pyplot as plt
import spacy
from nyc_trends import nyc_trends

#1) Using this information, create a bar chart of the top 10 topics based on their corresponding tweet volume.

#mylist = nyc_trends['trends']
volumes = []

for i in nyc_trends:
    volume = i['trends'][3]
    volumes.append(volume)

print(volumes[:10])

'''
from operator import itemgetter
sorted_items = sorted(items)

print(sorted_items[:10])

sorted_items = sorted(items, key=itemgetter(1), reverse=True)
print(sorted_items[:10])

top20 = sorted_items[:20]

print(top20)
'''

#plt.bar(x=,y=)




#2) Create a Word Cloud of all topics with over 20,000 tweet volume. The size of the word (topic) should be based on their tweet volume.
'''
wordcloud = WordCloud(colormap='prism',mask= ,background_color='white')

wordlcoud = wordcloud.generate(text)

wordcloud =wordcloud.to_file('NYC_TrendsCloud.png')

plt.imshow(wordcloud)
plt.show()
print('done')
'''