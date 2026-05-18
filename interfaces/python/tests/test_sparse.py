import os
import sys
import re
import numpy as np
import scipy as sp
from numpy.testing import *
from subprocess import Popen, PIPE, STDOUT

from qpoases import PyQProblem as QProblem
from qpoases import PyQProblemB as QProblemB
from qpoases import PySQProblem as SQProblem
from qpoases import PySolutionAnalysis as SolutionAnalysis
from qpoases import PyBooleanType as BooleanType
from qpoases import PySubjectToStatus as SubjectToStatus
from qpoases import PyOptions as Options
from qpoases import PyPrintLevel as PrintLevel


def test_sparse_solve():
    x0 = np.array([3., 2.])

    lb = np.array([0., 0.])
    ub = np.array([1, 1.])

    qp = QProblemB(2)

    H = sp.sparse.eye_array(2, 2, format="csc")

    nWSR = 10

    import pdb; pdb.set_trace()

    qp.init(H, -2*x0,
            lb,
            ub,
            nWSR)
