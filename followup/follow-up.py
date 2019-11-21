import math
import requests
import sys, os
import numpy as np
import pickle
from collections import Counter
import nltk
import string

nltk.data.path.append(r'nltk_data_folder')

from nltk import sent_tokenize,word_tokenize,PorterStemmer
from nltk.tag import pos_tag
from nltk.corpus import wordnet,stopwords
from nltk.stem import WordNetLemmatizer
import re


stop_words=stopwords.words('english')
#special=['.',';',',','\'','"','-','/','*','+','=','!','@','$','%','^','&','``','\'\'','We','The','This', 'Thus', 'If', 'In', 'A', 'Then', 'There']
special=['.',';',',','\'','"','-','/','*','+','=','!','@','$','%','^','&','``','\'\'']
ps=PorterStemmer()
lemmatizer=WordNetLemmatizer()

'''def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def predict(k, g, ne):

    pickle_in = open(resource_path('decisiontree_test_trail.pickle'), 'rb')
    clf = pickle.load(pickle_in)

    predicted = clf.predict([[k, g, ne]])
    accuracy = clf.predict_proba([[k, g, ne]])
    #print("class[1-10] : " + str(predicted))

    #print(np.max(accuracy))
    return predicted'''

def normalise(word):
    word = word.lower()
    word = ps.stem(word)
    return word


def get_cosine(vec1, vec2):
    intersection = set(vec1) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return numerator / denominator


def text_to_vector(text):
    words = word_tokenize(text)
    vec=[]
    for word in words:
        if(word not in stop_words):
            if(word not in special):
                w=normalise(word);
                vec.append(w);
    return Counter(vec)



def givKeywordsValue(text1, text2):
    vector1 = text_to_vector(text1)
    vector2 = text_to_vector(text2)
    cosine = round(get_cosine(vector1, vector2),2)*100

    kval = 0
    if cosine > 90:
        kval = 1
    elif cosine > 80:
        kval = 2
    elif cosine > 60:
        kval = 3
    elif cosine > 40:
        kval = 4
    elif cosine > 20:
        kval = 5
    else:
        kval = 6
    return kval

def remove_stopwrds(text):
    words = word_tokenize(text)
    vec=[]
    for word in words:
        if(word not in stop_words):
             if(word not in special):
                vec.append(word);
    return vec
	
def capitalize_words(student_answer):
    LCaps = []
    words = word_tokenize(student_answer)
    for element in words:
        if len(element) > 2:
            if element[0].isupper():
                LCaps.append(element)
            else:
                LCaps.append(string.capwords(element))
    return LCaps


def Intersection(lst1, lst2): 
    return set(lst1).intersection(lst2) 


def check_isupper(lst1):
    vec = [word for word in lst1 if word[0].isupper()]
    return vec 

	
def remove_duplicate(lst1):
    return list(dict.fromkeys(lst1))


def Named_Entity(text1, text2):
    
    vector1 = remove_stopwrds(text1)
    vector1 = check_isupper(vector1)
    vector1 = remove_duplicate(vector1)
    #print("Model answer entites: ", vector1)
    print("\n")
    print("Corpus Entities : ", vector1)

    vector2 = capitalize_words(text2)
    model_count = len(vector1)
    ne = Intersection(vector1, vector2)
    ne_count = len(ne)
    if ne_count == 0:
        print("Matched entites: NONE")
    else:
        #print("Matched entites: ", ne)
        print("\n")

    #print("No of matched entites: ", ne_count)    
    #print("\n")
    kval=0;
    if model_count !=0:
        ne_value = (ne_count*100)/model_count
        if ne_value > 90:
            kval = 1
        elif ne_value > 80:
            kval = 2
        elif ne_value > 60:
            kval = 3
        elif ne_value > 40:
            kval = 4
        elif ne_value > 20:
            kval = 5
        else:
            kval = 6
        return kval
    else :
        kval = 6
        return kval

def classify(model_greet, convo):
    # Similarity ==>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    
    if (len(convo.split())) <= 5:
        return 0
    k = givKeywordsValue(model_greet, convo)

    '''
    # GRAMMAR ==>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    try:
        req = requests.get("https://api.textgears.com/check.php?text=" + convo + "&key=JmcxHCCPZ7jfXLF6")
        no_of_errors = len(req.json()['errors'])
        if no_of_errors > 5 or k == 6:
            g = 0
        else:
            g = 1
    except requests.exceptions.ConnectionError as errc:
        g = 1
    '''
    
    # Named Entity ==>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    ne = Named_Entity(model_greet, convo)
    print("Similarity score : ", k)
    print("\n")
    if(k==1 or k==2 or k==3 or k==4):
        print("Follow up")
        print("\n")
    elif(k==5):
        print("New patient")
        print("\n")
    else:
        print("None")
        print("\n")
    #print("Grammar accuracy score : ", g)
    #print("Named entity score : ", ne)

    # Predict score ==>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    
    '''predicted = predict(k, g, ne)
    result = predicted * int(Total_marks) / 10
    return result[0]'''

model_greet = sys.argv[1]
convo = sys.argv[2]
#Total_marks = sys.argv[3]

file = open(model_greet, 'r', encoding = 'cp1252')
model_greet = file.read()

file = open(convo, 'r', encoding = 'cp1252')
convo = file.read()
print("\n")
print("CONVERSATION :")
print(str(convo))

#res = evaluate_ans(model_ans, student_ans, Total_marks)
classify(model_greet, convo)

#print("Marks Obtained : " + str(int(res)) + " / " + str(Total_marks))