from project import create_model, create_df, evaluate
import keras
import pytest

def test_evaluate():
    with pytest.raises(TypeError):
        evaluate(None)
        
def test_create_df():
    assert type(create_model([1])) == keras.src.models.sequential.Sequential

def test_create_df():
    assert type(create_df("./data.csv",1)) == tuple
    with pytest.raises(Exception):
        create_df("")
