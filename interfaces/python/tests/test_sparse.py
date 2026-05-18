import os
import sys
import re
import numpy as np
import scipy as sp
from numpy.testing import *
from subprocess import Popen, PIPE, STDOUT

from qpoases import PyQProblemB as QProblemB
from qpoases import PyHessianType as HessianType


def test_sparse_solve():
    x0 = np.array([3., 2.])

    lb = np.array([0., 0.])
    ub = np.array([1, 1.])

    qp = QProblemB(2, HessianType.POSDEF)

    H = sp.sparse.eye_array(2, 2, format="csc")

    nWSR = 10

    qp.init(H,
            -2*x0,
            lb,
            ub,
            nWSR)
