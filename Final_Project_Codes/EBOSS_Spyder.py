# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import h5py
from astropy.io import fits
from astropy.io import ascii

hdu = fits.open("/Users/kyleporter/Desktop/ASTR480/sdss_eboss_firefly-dr14.fits")

hdu[1].data
