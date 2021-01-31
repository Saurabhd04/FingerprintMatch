import os
import shutil
def makeFolder(src):
    directory = 'temp'

    parentDir = "C:/Users/Sourabh/Fingerprints/"

    path = os.path.join(parentDir, directory)

    # src = "C:/Program Files/Mantra/MFS100/Driver/MFS100Test/FingerData"
    
    shutil.copytree(src, path)