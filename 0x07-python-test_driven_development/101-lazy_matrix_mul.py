#!/usr/bin/python3
""" lazy matrix """


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ lazy matrix """
    if type(m_a) is not list or type(m_b) is not list:
        raise ValueError("Scalar operands are not allowed, use '*' instead")

    h_a = len(m_a)
    w_a = 0 if h_a == 0 else len(m_a[0])
    h_b = len(m_b)
    w_b = 0 if h_b == 0 else len(m_b[0])

    if h_a == 0 or w_a == 0 or h_b == 0 or w_b == 0:
        raise ValueError("shapes ({:d},{:d}) and\
                         ({:d},{:d}) not aligned: {:d} (dim {:d}) != {:d}\
                          (dim {:d})\
                         ".format(w_b, h_a, w_b, w_b, h_a, h_b, w_b, h_a))

    for r_a in m_a:
        if len(r_a) != len(m_a[0]):
            raise ValueError("setting an array element with a sequence.")
        for c_a in r_a:
            if type(c_a) is not int and type(c_a) is not float:
                raise TypeError("invalid data type for einsum")
    for r_b in m_b:
        if len(r_b) != len(m_b[0]):
            raise ValueError("setting an array element with a sequence.")
        for c_b in r_b:
            if type(c_b) is not int and type(c_b) is not float:
                raise TypeError("invalid data type for einsum")
    if len(m_a[0]) != len(m_b):
        raise ValueError("shapes ({:d},{:d}) and ({:d},\
                         {:d}) not aligned: {:d} (dim {:d}) != {:d} \
                         (dim {:d})\
                         ".format(w_b, h_a, w_b, w_b, h_a, h_b, w_b, h_a))

    return np.matmul(m_a, m_b)
