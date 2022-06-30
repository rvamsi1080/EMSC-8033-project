import pytest
from src.project_function import *

def test_documentation(doc_type = str):
    # testing the type of the returned variable
    document_type = type(proj_documentation())
    document_len = len(proj_documentation())
    
    assert document_type == doc_type, " *** Failed the test, no documentation to return *** "
    
    
def test_datasets(my_data_len = 5, my_data_type = tuple):
    dataset_1 = 'EN.4.2.2.f.analysis.c14.202104.nc'
    dataset_2 = 'EN.4.2.2.f.analysis.c14.192204.nc'
    data = load_datasets(dataset_1, dataset_2)
    data_type = type(data)
    data_len = len(data)
    
    assert data_len == my_data_len and data_type == my_data_type, " *** Test failed *** "
    
    
    
    
