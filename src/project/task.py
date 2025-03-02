from importlib import resources


def get_data_file():
    """Get path to the data file."""
    data_file = resources.files("project").joinpath("Polyn_2011_scored.csv")
    return data_file
