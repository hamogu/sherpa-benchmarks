import numpy as np

from sherpa import models
from sherpa.data import Data2D

x_small = np.linspace(-4, 3, 50)
x_large = np.linspace(-4, 300, 5000000)
twod_small = Data2D('data', x_small, x_small, x_small)
twod_large = Data2D('data', x_large, x_large, x_large)

twod_small.ignore(x0low=-3, x0hi=-2, x1lo=-3, x1hi=-2)

# Gauss is a common model, so we pick that as an example here.
# We could do the same benchmarks for all models in Sherpa
# but that might be more than we want ot look at.
# Much of the models shera a common machinary (i.e. they derive
# from the same base class), so a test for a few representative
# models here might be enough as a start.

gauss1d = models.Gauss1D("name")
gauss2d = models.Gauss2D("name")


def time_gauss1d_init():
    g = models.Gauss1d('name')

    
def time_direct_gauss1d_small():
    y = gauss1d(x_small)

    
def time_direct_gauss1d_large():
    y = gauss1d(x_large)


def time_direct_gauss1d_small_binned():
    y = gauss1d(x_small[:-1], x_small[1:])

    
def time_direct_gauss1d_large_binned():
    y = gauss1d(x_large[:-1], x_large[1:])

    
def time_set_par_gauss1d():
    g.fwhm = 1.


def time_calc_gauss1d_small():
    y = gauss1d([5, 0.4, 1], x_small)


def time_calc_gauss1d_large():
    y = gauss1d([5, 0.4, 1], x_large)


def time_direct_gauss2d_small():
    y = gauss2d(x_small, x_small)

    
def time_direct_gauss2d_large():
    y = gauss2d(x_large, x_large)

    
def time_eval_model_gauss2d_small():
    y = twod_small.eval_model(gauss2d)

    
def time_eval_model_gauss2d_large():
    y = twod_large.eval_model(gauss2d)


def time_eval_model_for_fit_gauss2d_small():
    y = twod_small.eval_model_for_fit(gauss2d)

    
def time_eval_model_gauss2d_large():
    y = twod_large.eval_model_for_fit(gauss2d)
