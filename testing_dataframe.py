#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 22:00:44 2019

This is module for testing dataframe for three cases.

1. Test if dataframe meets three requirements

2. Test if all the values have correct data type

3. Test if dataframe contains nan value

4. Test if dataframe have at least one row

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

#check three requirements
def test_create_dataframe(dataframe, col_name):
    """
    This function check three requirements
    1.Check if dataframe columns contains only the columns in second parameter
    2.Check if number of rows is greater than 10
    3.Check if values are the correct type

    Parameters
    ----------
    dataframe: pandas dataframe
    col_name: list of column

    Returns
    -------
    is_valid: boolean
        True if meet three requirements, false if not
    """
    is_valid = True
    if list(dataframe.columns) != col_name:
        is_valid = False
    if len(dataframe) < 10:
        is_valid = False
    for i in dataframe.columns:
        for j in range(len(dataframe)):
            if type(dataframe[i][j]) != type(dataframe[i][0]):
                is_valid = False
                break
    return is_valid

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
