import sys
import os
import argmedical-image-model-trainer
import unittest
import warnings
import contextlib
from functools import wraps
from itertools import product
from copy import deepcopy

def run_tests():
    import faulthandler
    faulthandler.enable()
    unittest.main(verbosity=2)