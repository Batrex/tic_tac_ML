from G1 import save_model,_defaultdict_to_dict
from collections import defaultdict
#create the basic file that can be pickeled to later with the model in it 
model_default= defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: [0,0])))
model_dict = _defaultdict_to_dict(model_default)
save_model(model_dict,"model.sav")
