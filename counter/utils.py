from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import matplotlib.pyplot as plt
from wordcloud import STOPWORDS, WordCloud
import base64
import io
import urllib.parse
        

stopwords = set(STOPWORDS)

def show_wordcloud(data):
    try:
        wordcloud = WordCloud(
            background_color="white",max_words=200,max_font_size=40,
            scale=3,random_state=0,stopwords=stopwords)
        wordcloud.generate(str(data))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        image = io.BytesIO()
        plt.savefig(image, format="png")
        image.seek(0)
        text_dictionary = wordcloud.process_text(data)
        word_freq={k: v for k, v in sorted(text_dictionary.items(),reverse=True, key=lambda item: item[1])}
        rel_freq=wordcloud.words_
        plt.show()
        return word_freq
    except ValueError:
        return None