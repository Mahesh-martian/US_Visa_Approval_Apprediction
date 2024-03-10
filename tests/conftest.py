from us_visa.constants import COLLECTION_NAME
from us_visa.data_access.usvisa_data import USvisaData
import pytest
from deepchecks.tabular import Dataset
from us_visa.utils.main_utils import read_yaml_file
from us_visa.constants import TARGET_COLUMN, SCHEMA_FILE_PATH
from sklearn.model_selection import train_test_split
import os


os.chdir('..')

schema = read_yaml_file(SCHEMA_FILE_PATH)
cat_cols = schema['categorical_columns']
num_cols = schema['numerical_columns']
complete_cols = cat_cols + num_cols
label = schema['target_column'][0]

us_data = USvisaData()
df = us_data.export_collection_as_dataframe(collection_name=COLLECTION_NAME)

@pytest.fixture
def raw_df():
    return df

@pytest.fixture
def complete_df():

    return Dataset(df, label = label, cat_features=[])

@pytest.fixture
def train_test():

    train_set, test_set = train_test_split(df, test_size=0.3)

    train_df = Dataset(train_set, label = label, cat_features=[])
    test_df = Dataset(test_set, label = label, cat_features=[])

    return train_df, test_df 

@pytest.fixture
def cols():
    col_names = {'cat_cols':cat_cols, 'num_cols':num_cols, 'complete_cols':complete_cols, 'label':label}
    return col_names




