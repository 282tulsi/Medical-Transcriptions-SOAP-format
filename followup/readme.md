Subjective Classification as follow up, new patient tagging
-----------------------------------------------------------


Dependencies
------------

    python >= 3.5
    NLTK library
    requests==2.11.1
    numpy==1.14.0
    pandas==0.22.0


Usage
-----

    python follow-up.py model/text.txt convo/test.txt 

    First argument to follow-up.py is the model greetings, 2nd argument is doctor-patient conversation.


Output
------

Ouput will be displayed in terminal. It shows the

    conversation
    corpus entities
    similarity score 
    classified class as follow-up or new-patient or none
