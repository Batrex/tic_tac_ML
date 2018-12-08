#use this file to actually run anything that is needed to be run 
from coordination import playgame,G1,human
for i  in range(10000):
	print("game "+str(i))
	playgame(G1,G1)