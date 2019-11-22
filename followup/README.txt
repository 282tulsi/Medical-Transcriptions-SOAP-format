##Subjective Classification as follow up, new patient tagging

##Dependencies

    python >= 3.5
    NLTK library
    requests==2.11.1
    numpy==1.14.0
    pandas==0.22.0

##Usage

python follow-up.py model/test.txt convo/text.txt 

First argument to follow-up.py is the model greetings, 2nd argument is doctor-patient conversation.

##Output

Ouput will be displayed in terminal. It shows the

    model answer entities
    cosine similarity score 
    matched entites & number of matched entites
    classified class as follow-up or new-patient or none
