# -*- coding: utf-8 -*-
from math import ceil
def xrange(start_stop, stop=None, step=None):
    """
    Funkcja która działa jak funkcja range (wbudowana i z poprzednich zajęć)
    która działa dla liczb całkowitych.
    """
    if stop is None: start_stop, stop = 0, start_stop
    if step is None: step = 1
    if start_stop>=stop and step>0: return []
    N = ceil((stop - start_stop)/step)
    for i in range(N):
      yield start_stop + i*step