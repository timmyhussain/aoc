# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 11:22:20 2023

@author: Timmy
"""

import unittest 
from unittest.mock import patch, MagicMock
import aoc8


class TestFunc(unittest.TestCase):
    
    def setUp(self):
        pass
        
    def test_count_trees(self):
        "testing count trees"
        self.assertEqual(aoc8.count_trees("input_8.txt"), 1711)
        pass

if __name__ == "__main__":
    unittest.main(verbosity=1, exit=True)