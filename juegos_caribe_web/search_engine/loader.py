import numpy as np
from django.db import models
from math import log
from django.conf import settings

class ModelSearchManager(object):
    def __init__(self, model : models.Model | str, *args):
        if type(model) is str:
            self.__make_vector__(model)
            return

        text = ''
        self.model = model
        
        for field in args:
            text = f'{text} {model.__getattribute__(field)}'
        self.__make_vector__(text)
        

    def __make_vector__(self, text : str):
        text = [e.strip() for e in text.lower().split()]
        count = {}

        for word in text:
            if not word in count:
                count[word] = 0
            count[word] += 1
        
        self.tf = {}
        for word, frec in count.items():
            self.tf[word] = len(count.values()) / frec
        
        self.tf_idf = self.tf.copy()
        self.length = len(self.tf.items())
    
    def __mul__(self, other):
        if self.length > other.length:
            self, other = other, self
        
        v1 = []
        v2 = []

        flag = True

        for word, val in self.tf_idf.items():
            if word in other.tf_idf:
                flag = False
                v1.append(val)
                v2.append(other.tf_idf[word])

        if flag:
            return .0

        v1 = np.array(v1)
        v2 = np.array(v2)

        ans = (v1 @ v2) / (np.sqrt(v1**2).sum() * np.sqrt(v2**2).sum())

        return ans
    
    __rmul__ = __mul__
    
    def multiply_by_idf(self,word : str, idf : float) -> None:
        if word in self.tf_idf:
            self.tf_idf[word] = self.tf[word] * idf
    
    def get_words(self):
        return self.tf.keys()

def get_query_as_vector(query : str):
    v_query = ModelSearchManager(query)

    words = []
    idf = []

    q_count = {}
    for word in set(v_query.get_words()):
        if word not in q_count:
            q_count[word] = 0
        q_count[word] += 1
    
    for word, frec in q_count.items():
        words.append(word)
        added_frec = 0
        if word in settings.doc_count:
            added_frec = settings.doc_count[word]
        idf.append(log((len(settings.documents) + 1) / (frec + added_frec)))
    
    for i in range(len(idf)):
        v_query.multiply_by_idf(words[i], idf[i])
    
    return v_query


def load_models(model : models.Model, *args):
    for mod in model.objects.all():
        settings.documents.append(ModelSearchManager(mod, *args))
    
    for doc in settings.documents:
        for word in set(doc.get_words()):
            if word not in settings.doc_count:
                settings.doc_count[word] = 0
            settings.doc_count[word] += 1
    
    words = []
    idf = []

    for word, frec in settings.doc_count.items():
        words.append(word)
        idf.append(log(len(settings.documents) / frec))
    
    for doc in settings.documents:
        for i in range(len(idf)):
            doc.multiply_by_idf(words[i], idf[i])

def search(query : str):
    v_query = get_query_as_vector(query)

    ans = []
    for doc in settings.documents:
        ans.append((doc * v_query, doc.model))
    
    ans.sort()

    return [i for _,i  in ans]

settings.documents : list[ModelSearchManager] = []
settings.doc_count = {}
