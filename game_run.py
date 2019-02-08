from coordination import playgame,G1,human
from log_import import log

"""
use this file to actually run anything that is needed to be run
"""

for i  in range(2000):
	log.info("----game: "+str(i)+"-----")
	playgame(G1,G1)
