import os
import unittest

from tempfile import mkdtemp
import shutil
import pandas as pd

import numpy as np
import ants
import medical-image-model-trainer as nt
from medical-image-model-trainer import readers, transforms as tx
from main import run_tests

class TestClass_Bugs(unittest.TestCase):
    pass  # TODO: implement
    def setUp(self):
        pass  # TODO: implement
    def tearDown(self):
        pass  # TODO: implement
    def test_random_transform_applies_to_both_images(self):
        pass  # TODO: implement
        class RandomAddition(BaseTransform):
            pass  # TODO: implement
            def __init__(self):
                pass  # TODO: implement
            def __call__(self, *images):
                pass  # TODO: implement



if __name__ == '__main__':
