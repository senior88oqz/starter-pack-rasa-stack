# Get Started with RASA

## NLU

NLU understands the user’s message based on your previous training data:

* Intent classification: Interpreting meaning based on predefined intents (Example: I need a GP in 94301 is a find_doctor intent with 93% confidence)
* Entity extraction: Recognizing structured data (Example: GP is a doctor_type and 94301 a zipcode)

### Setup & Training

`nlu.md` : Defines the intents and providing a few ways users might express them

`nlu_config.yml` : Defines how the NLU model will be trained and how the features from the text inputs will be extracted. (See more in [Choosing a Rasa NLU Pipeline](https://rasa.com/docs/nlu/choosing_pipeline/))

- Train rasa.nlu model with `nlu.md` and `nlu_config.yml`, saving at `models/current/nlu`

```bash
python -m rasa_nlu.train -c nlu_config.yml --data nlu.md -o models --fixed_model_name nlu --project current --verbose
```

### Testing

```python
from rasa_nlu.model import Metadata, Interpreter
import json

def pprint(o):
 # small helper to make dict dumps a bit prettier
    print(json.dumps(o, indent=2))

interpreter = Interpreter.load('./models/current/nlu')
pprint(interpreter.parse(u"Hello"))
```

## Core

Core decides what happens next in this conversation. It’s machine learning-based dialogue management predicts the next best action based on the input from NLU, the conversation history and your training data.

### Setup & Training

`stories.md` : Defines response/action per user input, the response/action could be anything including ***making API calls***

`domain.yml` :  Defines what user inputs it should expect to get, what actions it should be able to predict, ***how*** to respond and what information to store

- Call the Rasa Core train function, pass domain and stories files to it and store the trained model into the models/dialogue directory.

```bash
python -m rasa_core.train -d domain.yml -s stories.md -o models/dialogue
```
## Setup for Mac with Anaconda Distribution

- Create and activate the rasa environment (via conda)

```bash
conda create -n rasa python=3.6
source activate rasa
```

- Install tensorflow 1.12.0

```bash
pip install --upgrade https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.12.0-py3-none-any.whl
```

- Install dependencies via requirements.txt

```bash
pip install -r requirements.txt
```

## Get Response through HTTP/Rest API

- [RestInput](https://rasa.com/docs/core/connectors/#restinput)

```bash
curl -XPOST \
 http://localhost:5005/webhooks/rest/webhook \
 -H 'Content-Type: application/json' \
 -d '{
    "message": "hello"
}'
```

- HTTP Endpoints `/conversations/{sender_id}/respond`


```bash
curl -XPOST --data '{"query": "hello"}' "localhost:5005/conversations/default/respond"
```