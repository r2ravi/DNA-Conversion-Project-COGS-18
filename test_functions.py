"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

from functions import *

def test_string_concatenator():

    assert string_concatenator('abc', 'def') == 'abcdef'
    
def test_DNA_to_mRNA_List():
    
    assert DNA_to_mRNA_List('CTGATCG') == ['G', 'A', 'C', 'U', 'A', 'G', 'C']
    
def test_DNA_to_mRNA():

    assert DNA_to_mRNA('CTGATCG', '-') == 'GAC-UAG-C'
    
def test_DNA_to_tRNA_List():
    
    assert DNA_to_tRNA_List('CTGATCG') == ['C', 'U', 'G', 'A', 'U', 'C', 'G']

def test_DNA_to_tRNA():
    
    assert DNA_to_tRNA('CTGATCG', '-') == 'CUG-AUC-G'