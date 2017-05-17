import logging
from src import ConfigurationHandler as CH
import multiprocessing as mp
# Internal Magic Varable for safety protection
processlock = CH.getconfig("Experimental", "ProcessLock")
processcount = None
def createProcess(Pfunction, *functionargs):
    if processcount <= processlock:
        process = mp.Process(target=Pfunction, args=functionargs)
        process.start()
        return True
    else:
        logging.CRITICAL("unable to summon new process. ProcCount: " + str(processcount) + " ProcLock:" + processlock)
