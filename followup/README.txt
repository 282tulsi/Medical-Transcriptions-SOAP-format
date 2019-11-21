

##Subjective Classification as follow up, new patient tagging

##Dependencies

    python >= 3.5
    NLTK library
    requests==2.11.1
    numpy==1.14.0
    pandas==0.22.0

##Usage

python evaluate_poc.py model\1.txt student\st_1.txt 5

First argument to follow-up.py is the model greetings, 2nd argument is doctor-patient conversation.

##Output

Ouput will be displayed in terminal. It shows the

    model answer entities
    matched entites & number of matched entites
    Keyword score, Grammar score, Named entity score
    Total marks obtained by student out of marks given as argument to program


