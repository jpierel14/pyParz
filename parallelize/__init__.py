# Licensed under a 3-clause BSD style license - see LICENSE.rst

# Packages may add whatever they like to this file, bu# should keep this content at the top.
# ----------------------------------------------------------------------------
from ._astropy_init import *
# ----------------------------------------------------------------------------

if not _ASTROPY_SETUP_:
    # For egg_info test builds to pass, put package imports here.

    import multiprocessing,cPickle
    from multiprocessing import Pool
    import numpy as np
    
