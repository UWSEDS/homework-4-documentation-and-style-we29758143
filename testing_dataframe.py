#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 22:00:44 2019

This is module for testing dataframe for three cases.

1. Test if all the values have correct data type

2. Test if dataframe contains nan value

3. Test if dataframe have at least one row

@author: lvguanxun
"""

import pandas as pd

#read data
def read_data(url):
    """
    Read dataframe from URL and parse into pandas dataframe

    Parameters
    ----------
    url: string
        A string of a desire URL

    Returns
    -------
    dataframe
        Read the csv file and return a pandas dataframe
    """
    return pd.read_csv(url)


#test if correct values type, else raise ValueError
def test_columns_correct(dataframe):
    """
    Test if dataframe contains incorrect datatype

    Parameters
    ----------
    dataframe: pandas dataframe

    Raises
    ------
    ValueError
        If contains incorrect datatype, raise valueError

    Returns
    -------
    is_valid: boolean
        True if correct, False if contains incorrect type
    """
    is_valid = True
    for i in dataframe.columns:
        for j in range(len(dataframe)):
            if type(dataframe[i][j]) != type(dataframe[i][0]):
                is_valid = False
                raise ValueError("values did not have correct type")
    return is_valid

#test if contains nan, else raise ValueError
def test_nan(dataframe):
    """
    Test if dataframe contains nan value

    Parameters
    ----------
    dataframe: pandas dataframe

    Raises
    ------
    ValueError
        If contains nan, raise ValueError

    Returns
    -------
    is_valid: boolean
        True if did not contain nan, False if contain
    """
    is_valid = True
    for i in range(len(dataframe.columns)):
        if dataframe.isnull().any()[i] == True:
            is_valid = False
            raise ValueError("values contain nan")
    return is_valid

#test if dataframe contains at least one row, else raise ValueError
def test_row(dataframe):
    """
    test if dataframe contains at least one row

    Parameters
    ----------
    dataframe: pandas dataframe

    Raises
    ------
    ValueError
        If number of row is smaller than 1, raise ValueError

    Returns
    -------
    is_valid: boolean
        True if greater than 1, False if lower than 1
    """
    is_valid = True
    if len(dataframe) < 1:
        is_valid = False
        raise ValueError("dataframe must has at least one row")
    return is_valid

"""
pylint score
lvguanxunde-MacBook-Pro:homework-4-documentation-and-style-we29758143 lvguanxun$ pylint testing_dataframe.py
************* Module testing_dataframe
testing_dataframe.py:59:15: C0123: Using type() instead of isinstance() for a typecheck. (unidiomatic-typecheck)
testing_dataframe.py:85:11: C0121: Comparison to True should be just 'expr' (singleton-comparison)
testing_dataframe.py:110:7: C1801: Do not use `len(SEQUENCE)` to determine if a sequence is empty (len-as-condition)

------------------------------------------------------------------
Your code has been rated at 8.75/10 (previous run: 7.50/10, +1.25)
"""