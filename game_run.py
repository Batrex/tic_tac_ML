import logging
log = logging.getLogger(__name__)


#use this file to actually run anything that is needed to be run

logging.basicConfig(level=logging.INFO)
from coordination import playgame,G1,human
for i  in range(1):
	log.info("----game: "+str(i)+"-----")
	playgame(G1,human)
