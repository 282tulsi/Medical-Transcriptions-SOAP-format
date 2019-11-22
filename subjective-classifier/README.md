Installation
------------

```bash
conda create -n medicaltranscript python=3.6
activate medicaltranscript
pip install -r requirements.txt
cd data
mkdir word_embeddings
wget http://nlulite.com/download/glove ./data/word_embeddings/
```

Running a source code
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

