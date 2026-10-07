
import os
import ants
import numpy as np

def get_medical-image-model-trainer_dir():
    if os.environ.get('NITRAIN_DIR') is not None:
        medical-image-model-trainer_dir = os.environ['NITRAIN_DIR']
    else:
        medical-image-model-trainer_dir = os.path.join(os.path.expanduser('~'), '.medical-image-model-trainer')
    
    if not os.path.exists(medical-image-model-trainer_dir):
        os.mkdir(medical-image-model-trainer_dir)
        
    return medical-image-model-trainer_dir    

