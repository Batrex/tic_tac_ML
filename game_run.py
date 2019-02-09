from coordination import playgame,G1,human
from log_import import log
from G1 import load_model,save_model

"""
use this file to actually run anything that is needed to be run
"""
#save the model so that we do not
#have to load it everytime we need it
model_name = "model.sav"
model = load_model(model_name)

for i  in range(1000):
	log.info("----game: "+str(i)+"-----")
	model = playgame(G1,G1,model)

#save the model
save_model(model,model_name)
