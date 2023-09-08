import pandas as pd
import numpy as np


def load_juris_meta(path: str):
    """
    loads the meta data of all labor related and non
    labor related jurisprudence documents

    path - path where juris_meta.csv file is located
    """
    
    juris_meta = pd.read_csv(path, index_col=0)

    return juris_meta 