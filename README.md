# HanziNLP

An **user-friendly** and **easy-to-use** Natural Language Processing package specifically designed for Chinese text analysis, modeling, and visualization.

## Table of Contents
- [Introduction](#introduction)
  - [Related Links](#related-links)
  - [Installing and Usage](#installing-and-usage)
- [Character and Word Counting](#character-and-word-counting)
- [Font Management](#font-management)
- [Text Segmentation](#text-segmentation)
  - [Stopword Management](#stopword-management)
  - [Tokenization Specifics](#tokenization-specifics)
    - [Sentence Segmentation](#sentence-segmentation)
    - [Word Tokenization](#word-tokenization)
- [Text Representation](#text-representation)
- [Text Similarity](#text-similarity)
- [Word Embeddings](#word-embeddings)
- [Topic Modeling](#topic-modeling)
- [Sentiment Analysis](#sentiment-analysis)

## Developer

To anyone using HanziNLP, big thanks to you from the developer 施展,Samuel Shi! 🎉🎉🎉 

For any improvement and more information about me, you can find via the following ways:
- **Personal Email**: samzshi@sina.com
- **Personal Webiste**: [https://www.samzshi.com/](https://www.samzshi.com/)
- **Linkedin**: [www.linkedin.com/in/zhanshisamuel](www.linkedin.com/in/zhanshisamuel)

## Introduction

Welcome to **HanziNLP** 🌟 - an ready-to-use toolkit for Natural Language Processing (NLP) on Chinese text, while also accommodating English. It is designed to be user-friendly and simplified tool even for freshmen in python. 

Moreover, HanziNLP features an interactive dashboard for dynamic insights into NLP functionalities, providing a dynamic overview and insights into various NLP functionalities.

### Related Links

- **GitHub Repository**: Explore my code and contribute on [GitHub](https://github.com/samzshi0529/HanziNLP).
- **PyPI Page**: Find me on [PyPI](https://libraries.io/pypi/HanziNLP) and explore more about how to integrate HanziNLP into your projects.

### Installation and Usage

Getting started with HanziNLP is as simple as executing a single command!

```python
pip install HanziNLP
```

## Character and Word Counting

🚀 This basic function count the characters and words in your text, sparing you the manual effot of identifying and splitting Chinese words on your own. 

### char_freq and word_freq Functions
- `char_freq(text, text_only=True)`: Function to calculate the frequency of each character in a given text; If text_only == True, only Chinese and English characters will be counted. If text_only == False, all characters will be counted. Default to be True.
- `word_freq(text)`: Function to calculate the frequency of each word in a given text.
### Code Example
```python
from HanziNLP import char_freq, word_freq

text = "你好, 世界!"
char_count = char_freq(text)
word_count = word_freq(text)

print(f"Character Count: {char_count}")
print(f"Word Count: {word_count}")
```
### Output Example
```python
Charater Count: 4
Word Count: 2
```
## Font Management

When visualizing Chinese text in Python environment, font is a vital resource which is often needed from manual importing. HanziNLP have built-in list of fonts for usage right away. You can use list_fonts() to see and filter all available fonts and use get_font() to retrieve a specific font path for visualization purposes. All built-in fonts are from Google fonts that are licensed under the Open Font License, meaning one can use them in your products & projects – print or digital, commercial or otherwise.

### list_fonts and get_font Functions
- `list_fonts()`: List all available fonts.
- `get_font(font_name, show=True)`: Retrieve a specific font for visualization purposes. If show == True, a sample visualization of the font will be shown. If show == False, nothing will be shown. Default set to be True.

#### list_fonts() example
```python
from HanziNLP import list_fonts

# List all available fonts
list_fonts()
```
#### output
![Example Image](README_PIC/list_fonts().png)

#### get_font() example
```python
from HanziNLP import get_font

font_path = get_font('ZCOOLXiaoWei-Regular') #Enter the font_name you like in list_fonts()
```
#### output
![Example Image](README_PIC/get_font.png)

#### WordCloud Example
You can use the Chinese font_path you defined to make all kinds of plots. A wordcloud example is provided below:
```python
from PIL import Image
from wordcloud import WordCloud,ImageColorGenerator
import matplotlib.pyplot as plt

# A sample text generated by GPT-4 
text = '在明媚的春天里，小花猫咪悠闲地躺在窗台上，享受着温暖的阳光。她的眼睛闪烁着好奇的光芒，时不时地观察着窗外忙碌的小鸟和蝴蝶。小猫的尾巴轻轻摇动，表达着她内心的舒适和满足。在她的身边，一盆盛开的紫罗兰散发着淡淡的香气，给这个宁静的午后增添了几分诗意。小花猫咪偶尔会闭上她的眼睛，沉浸在这美好的时光中，仿佛整个世界都变得温馨和谐。窗外的樱花树在微风中轻轻摇曳，洒下一片片粉色的花瓣，如梦如幻。在这样的一个悠托的春日里，一切都显得如此美好和平静。'

text = " ".join(text)

# Generate the word cloud
wordcloud = WordCloud(font_path= font_path, width=800, height=800,
                      background_color='white',
                      min_font_size=10).generate(text)

# Display the word cloud
plt.figure(figsize=(5, 5), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.title("sample wordcloud")

plt.show()
```
#### output
![Example Image](README_PIC/wordcloud.png)

## Text Segmentation
Text Segmentatino is a vital step in any NLP tasks. The general step is to segment the sentences, remove stopwords, and tokenize each sentences separately. The detailed instructions are introduced below. 

### Stopword Management
To remove stopwords in Chinese text, the package have built-in common stopwords lists include the following ones: (Some stopwords are from [stopwords](https://github.com/goto456/stopwords/))

| Stopword List | File Name |
|----------|----------|
| 中文停用词表 | cn_stopwords.txt |
| 哈工大停用词表 | hit_stopwords.txt |
| 百度停用词表 | baidu_stopwords.txt |
| 四川大学机器智能实验室停用词表 | scu_stopwords.txt |
| 常用停用词表 | common_stopwords.txt |

#### list_stopwords and load_stopwords Functions
- `list_stopwords()`: List all available stopwords.
- `load_stopwords(file_name)`: Load stopwords from a specified file.

##### list_stopwords example
```python
from HanziNLP import list_stopwords

list_stopwords()
```
##### output 
![Example Image](README_PIC/list_stopwords.png)

##### load_stopwords example
```python
from HanziNLP import load_stopwords

stopwords = load_stopwords('common_stopwords.txt') # Enter the txt file name here
```

### Tokenization Specifics
After selecting a stopword to use, we can begin to tokenize the text using the stopword defined. 

#### Sentence Segmentation
- `sentence_segment`: Segment the input text into sentences. 

##### sentence_segment example: This example intentially chooses a hard sentence to split.
```python
from HanziNLP import sentence_segment

sample_sentence = 'hello world! This is Sam.。 除非你不说。我今天就会很开心,hello .you。'
sentence_segment(sample_sentence)
```
##### output 
```python
['hello world!', 'This is Sam.', '。', '除非你不说。', '我今天就会很开心,hello .', 'you。']
```

#### Word Tokenization
- `word_tokenize(text, mode='precise', stopwords='common_stopwords.txt', text_only=False, 
                  include_numbers=True, custom_stopwords=None, exclude_default_stopwords=False)`: Tokenize the input text into words and remove stopwords.
Specific parameter introduciton is listed here:
```python
    Parameters:
    text (str): The input Chinese text.
    mode (str): Tokenization mode ('all', 'precise', or 'search_engine'). Default is 'precise'.
    stopwords (set): A set of stopwords.
    text_only (Boolean): Only tokenize English and Chinese texts if True. Default is False.
    include_numbers (Boolean): Whether to include numbers in the tokenized output. Default is True.
    custom_stopwords (list, optional): A list of custom stopwords to remove. Default is None.
    exclude_default_stopwords (bool, optional): Whether to exclude default stopwords. Default is False.

    Returns:
    list: A list of tokens after removing stopwords.
```
## Text Representation

### BoW, ngrams, TF_IDF, and TT_matrix Functions
- `BoW`: Generate a Bag of Words representation of the input text.
- `ngrams`: Generate n-grams from the input text.
- `TF_IDF`: Generate a TF-IDF representation of the input text.
- `TT_matrix`: Generate a term-term matrix of the input text.

## Text Similarity

### text_similarity Function
- `text_similarity`: Calculate the similarity between two texts using various methods.

## Word Embeddings

### Word2Vec and get_bert_embeddings Functions
- `Word2Vec`: Obtain word embeddings using the FastText model.
- `get_bert_embeddings`: Obtain word embeddings using the BERT model.

## Topic Modeling

### lda_model and print_topics Functions
- `lda_model`: Train an LDA model on the input text.
- `print_topics`: Print the topics identified by the LDA model.

## Sentiment Analysis

### sentiment Function
- `sentiment`: Perform sentiment analysis on the input text using a specified pre-trained model.

---

Feel free to modify the descriptions and add any additional information or usage examples that you think would be helpful for users of your package!
