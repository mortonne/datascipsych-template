from importlib import resources
import json


def get_data_file():
    """Get path to the data file."""
    data_file = resources.files("project").joinpath("data/2011_Polyn_scored.csv")
    return data_file


def load_data_dict():
    """Read data dictionary for the dataset."""
    dict_file = resources.files("project").joinpath("data/data_dictionary.json")
    with open(dict_file) as f:
        d = json.load(f)
    return d
