from importlib import resources


def get_data_file():
    """Get path to the data file."""
    data_file = resources.files("project").joinpath("2011_Polyn_scored.csv")
    return data_file
