# from deepchecks.tabular.checks import *
import os


def test_no_of_columns(raw_df):

    assert len(raw_df.columns) == 12

def test_missing_num_cols(raw_df, cols):
    dataframe_columns = raw_df.columns
    missing_numerical_columns = []
    
    for column in cols['num_cols']:
        if column not in dataframe_columns:
            missing_numerical_columns.append(column)

    if len(missing_numerical_columns)>0:
        assert False
    else:
        assert True


def test_missing_cat_cols(raw_df, cols):
    dataframe_columns = raw_df.columns
    missing_categorical_columns = []

    for column in cols['cat_cols']:
        if column not in dataframe_columns:
            missing_categorical_columns.append(column)

    if len(missing_categorical_columns)>0:
        assert False
    else:
        assert True

