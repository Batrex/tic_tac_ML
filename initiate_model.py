import pickle 
from collections import defaultdict
from G1 import _defaultdict_to_dict
def initiate_model(model_name):
	model = _defaultdict_to_dict(defaultdict(lambda: defaultdict(lambda: [0,0])))
	pickle.dump(model, open(model_name, 'wb'))

initiate_model("model.sav")