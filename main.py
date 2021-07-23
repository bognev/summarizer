import sys
import argparse
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from src.summarizerpy.summarizer import Summarizer


parser = argparse.ArgumentParser(description='Summarizer')

parser.add_argument('--report',
                    help='summarise dataset statistics',
                    type=int, default=0)

parser.add_argument('--out',
                    help='output file name',
                    type=str, default='report')

parser.add_argument('--output_type',
                    help='output file type',
                    type=str, default='markdown')


def main():
    args = parser.parse_args()
    iris = load_iris()
    df = pd.DataFrame(data=np.c_[iris['data'], iris['target']],
                      columns=iris['feature_names'] + ['target'])
    sum = Summarizer(args.report, args.out, args.output_type)
    if args.report == 1:
        sum.save_report(df)
    if args.report == 0:
        txt = sum.save_report(df)
        print(txt)

    sys.exit(0)


if __name__ == '__main__':
    main()


