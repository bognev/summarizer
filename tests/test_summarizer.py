from src.summarizerpy.summarizer import Summarizer
from sklearn.datasets import load_iris
import pandas as pd
import numpy as np


def test_summary_iris():
    df = pd.DataFrame({
        "sepal length (cm)":[150, 5.843333, 0.828066, 4.3, 5.1, 5.8, 6.4, 7.9],
        "sepal width (cm)": [150, 3.057333, 0.435866, 2, 2.8, 3, 3.3, 4.4],
        "petal length (cm)": [150, 3.758, 1.765298, 1, 1.6, 4.35, 5.1, 6.9],
        "petal width (cm)": [150, 1.199333, 0.762238, 0.1, 0.3, 1.3, 1.8, 2.5],
        "target":[150, 1, 0.819232, 0, 0, 1, 2, 2]},
        index=['count', 'mean','std','min','25%','50%','75%','max'])

    return df


class TestApp:
    def test_summary_iris(self):
        iris = load_iris()
        df = pd.DataFrame(data=np.c_[iris['data'], iris['target']],
                          columns=iris['feature_names'] + ['target'])
        sum = Summarizer()
        res = sum.save_report(df)
        df = test_summary_iris()
        assert res == df.to_string()

    def test_create_file(tmp_path='./'):
        iris = load_iris()
        df = pd.DataFrame(data=np.c_[iris['data'], iris['target']],
                          columns=iris['feature_names'] + ['target'])
        sum = Summarizer(1, 'report', 'markdown')
        sum.save_report(df)
        df = test_summary_iris()
        p = open('./report.markdown', 'r').read()
        assert p == df.to_markdown()

