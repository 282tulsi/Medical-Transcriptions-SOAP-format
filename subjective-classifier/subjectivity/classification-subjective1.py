import os
from nltk.corpus import stopwords 
import timeit
import time
import json
import nltk
from nltk.tokenize import word_tokenize

# Program extracting first column 
import xlrd 

_path = os.path.dirname(__file__)

_error_message = '''
Please provide a text as an input.
You can either provide the text as an argument: python -m subjectivity.classify this is my opinion.
Or pipe the text from the command line: python -m subjectivity.classify < data/random_text.txt
'''


def _aggregate_sentence(args):
    return_str = ''
    for argument in args:
        return_str += argument + ' '
    return return_str


def _get_subj_or_obj_sentences_from_text(text):
    from subjectivity.subjectivity_classifier import SubjectivityClassifier
    classifier = SubjectivityClassifier(model_filename=os.path.join(_path, '../data/save/subj-29.tf'),
                                        word_filename=os.path.join(_path, '../data/word_embeddings/glove.6B.50d.txt'))
    return classifier.classify_sentences_in_text(text)


def print_sentences(sentences_dict):
    print('\nOBJECTIVE SENTENCES:')

    f.write('\nOBJECTIVE SENTENCES:')
    f.write('\n')
    f.write('\n')
    f.write('\n')
    f.write('\n')
    f.write('\n')
    [print(item) for item in sentences_dict['objective']]
    for item in sentences_dict['objective']:
    	res.append(item)
    	f.write(item + '\n')
    print("RESULT:",res)
    #f.write(str(item for item in sentences_dict['objective']))
    
    print('\nSUBJECTIVE SENTENCES:')
    f.write('\n')
    f.write('\n')
    f.write('\n')
    f.write('\n')
    f.write('\n')
    f.write('\n')
    f.write('\nSUBJECTIVE SENTENCES:')
    f.write('\n')
    f.write('\n')
    f.write('\n')
    f.write('\n')
    f.write('\n')
    [print(item) for item in sentences_dict['subjective']]
    for item in sentences_dict['subjective']:
    	#res.append(item)
    	f.write(item + '\n')
    #f.write(str(item for item in sentences_dict['subjective']))
    f.close()


def remove_stop_words(sentence):
    stop_words = set(stopwords.words('english'))
    words = sentence.split()     
    filtered_words = [r for r in words if not r in stop_words]
    return " ".join(filtered_words)

def remove_punctuations(r_sentence):
    punctuations = '''!()-[]{};:'"\,<>/@#$%^&*_~'''
    '''stop_words = set(stopwords.words('english'))
    words = sentence.split()     
    filtered_words = [r for r in words if not r in stop_words]'''
    no_punct = ""
    for char in r_sentence:
       if char not in punctuations:
           no_punct = no_punct + char
    return no_punct

#sentence = "It's himself. What's up, dear? How doing? Oh, yeah. Wow, long time, huh? It's long, well, I Ireland four months, I telling. INR 18. Oh. Okay. I Ireland four months. I went away. Oh. Okay. Did take medicine no? Oh, gee, I did. Oh, god, I did. The thing I'm terrible problems inhalers. The breathing worse? No, breathing fine. No, I'm keeping control it, -. Okay. Wait I tell happened. I Symbicort. Yeah. And affecting eyesight. That's really weird. Oh, know, know what? What? And see, tell that. As side effect, yeah. It's side effect. And getting bad I take I see. Okay."
#print("Removed stopwords:",remove_stop_words(sentence))

def posTagger(tokenized_sentences) :
    tagged = []
    for sentence in tokenized_sentences :
        tag = nltk.pos_tag(sentence)
        tagged.append(tag)
    return tagged

start_time = time.time()
if __name__ == '__main__':
    import os
    import sys
    f= open("result.txt","w+")
    f1= open("time_result.txt","w+")
    f1.write('\nEXECUTION TIME FOR NEURAL NETWORK:')
    f1.write('\n')
    f1.write('\n')
    res = []
    if len(sys.argv) > 1:
        sentence = _aggregate_sentence(sys.argv[1:])
        print_sentences(_get_subj_or_obj_sentences_from_text(sentence))
    else:
        if os.isatty(0):
            print(_error_message)
            exit(0)
        sentence = sys.stdin.read().strip()
        print("SENTENCES:",sentence)
        r_sentence = remove_stop_words(sentence)
        print("PRINT REMOVED STOP WORDS SENTENCE:",r_sentence)
        rr_sentence = remove_punctuations(r_sentence)
        print("PRINT REMOVED PUNCTUATIONS IN SENTENCE:",rr_sentence)
        tokens = word_tokenize(rr_sentence)
        print("TOKENIZED SENTENCES :",tokens)
        tagged = posTagger(tokens)
        print("P  O  S  : IN SENTENCE:",tagged)
        start_time1 = time.time()
        if sentence:
        	content = _get_subj_or_obj_sentences_from_text(rr_sentence)
        	time.time()
        	print("EXECUTION TIME FOR NEURAL NETWORK-------------------------1")
	        print("--- %s seconds ---" % (time.time() - start_time1))
	        t = time.time() - start_time1
	        f1.write(str(t))
	        print_sentences(_get_subj_or_obj_sentences_from_text(rr_sentence))
	        print(" ")
	        print("EXECUTION TIME FOR NEURAL NETWORK")
	        print("--- %s seconds ---" % (time.time() - start_time1))
            #f1.write(json.dumps(content))
            

#f.close()

print(" ")
print("EXECUTION TIME")
print("--- %s seconds ---" % (time.time() - start_time))
tt = time.time() - start_time
f1.write('\n')
f1.write('\n')
f1.write('\n')
f1.write('\nEXECUTION TIME FOR CODE:')
f1.write('\n')
f1.write('\n')
f1.write(str(tt))
f1.close()  
