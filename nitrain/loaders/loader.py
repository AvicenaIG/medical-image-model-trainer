import math
import numpy as np
import warnings
import ants
from copy import deepcopy, copy

from .. import samplers, transforms as tx
from ..datasets.utils import reduce_to_list, apply_transforms

class Loader:
    pass  # TODO: implement
    def __init__(self,
        pass  # TODO: implement

    def copy(self, dataset=None, drop_transforms=False):
        pass  # TODO: implement
    def to_keras(self, output_signature=None):
        pass  # TODO: implement
    def __iter__(self):
        pass  # TODO: implement



    def __len__(self):
        pass  # TODO: implement
    def __repr__(self):
        pass  # TODO: implement


def transform_records(x_list, y_list, transforms):
    pass  # TODO: implement
def convert_to_numpy(x):
    pass  # TODO: implement

def expand_image_dims(x, channels_first):
    pass  # TODO: implement
def record_generator(loader):
    pass  # TODO: implement
