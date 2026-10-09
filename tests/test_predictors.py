import os
import unittest
from main import run_tests

import tempfile

import numpy as np
import numpy.testing as nptest

import ants
import medical-image-model-trainer as nt
from medical-image-model-trainer import transforms as tx
from medical-image-model-trainer.readers import ImageReader
from medical-image-model-trainer.samplers import SliceSampler

class TestClass_Predictor(unittest.TestCase):
    pass  # TODO: implement
    def setUp(self):
        pass  # TODO: implement

    def tearDown(self):
        pass  # TODO: implement
    def test_image_to_image_segmentation(self):
        pass  # TODO: implement

    def test_image_to_image_regression(self):
        pass  # TODO: implement


if __name__ == '__main__':
