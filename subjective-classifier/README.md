Installation
------------

```bash
virtualenv --python=/usr/bin/python3 .env 
source .env/bin/activate 
pip install -r requirements.txt
wget http://nlulite.com/download/glove ./data/word_embeddings/
```

Running a simple example
------------------------

Pipe a text file from the command line: 
```bash
python -m subjectivity.classification-subjective1 < data/input.txt
```

The output will look like the following:
```text
OBJECTIVE SENTENCES
<list of objective sentences in the text>

SUBJECTIVE SENTENCES
<list of subjective sentences in the text>
```

