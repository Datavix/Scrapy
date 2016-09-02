
# coding: utf-8

# In[11]:

import jieba
import numpy as np
import pandas as pd
import json
np.set_printoptions(threshold=np.inf)


# In[12]:

with open('/Users/ChaoTong/Desktop/20160823_mp_result_utf8.json') as f:
    data = pd.DataFrame(json.loads(line, strict=False) for line in f)


# In[13]:

text_list = list(data.title)
text_list
import itertools
text_list = list(itertools.chain.from_iterable(text_list))
text_list


# In[14]:

import jieba
from sklearn.feature_extraction.text import  TfidfVectorizer
from sklearn.cluster import KMeans


# In[15]:

def jieba_tokenize(text):
    return jieba.lcut(text) 


# In[16]:

tfidf_vectorizer = TfidfVectorizer(tokenizer=jieba_tokenize, lowercase=False)


# In[17]:

tfidf_matrix = tfidf_vectorizer.fit_transform(text_list)


# In[18]:

cluster = KMeans(n_clusters = 3, max_iter = 300,init='k-means++')
result = cluster.fit_predict(tfidf_matrix)


# In[19]:

print result


# In[ ]:



