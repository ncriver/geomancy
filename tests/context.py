""" context.py """
""" A file for providing context to the test modules. """
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import geomancy
import geomancy.stringfuncs as stringfuncs
import geomancy.structures as structures
