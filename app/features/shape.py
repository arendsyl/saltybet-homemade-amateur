import pandas as pd

import typing
from typing import Dict, Any


def dataframe_shape(url: str) -> Dict[str, Any]:

    """dataframe_shape

    Function doing treatment for the POST route /shape

    [17/10/2019]
    Authors
    ----------
    Lucas Pauzies <lucas.pauzies@capgemini.com>

    Parameters
    ----------
    url : str
        The url linked to the csv to use on the web service

    Returns
    ----------
    Dict[str, Any]
        Return the result of the treatment
    """

    df = pd.read_csv(url)
    lines, columns = df.shape
    return {
        "message": {
            "dataframe": {
                "url": url,
                "lines": lines,
                "columns": columns
            }
        }
    }
