import pandas as pd
import polars as pl
import argparse

def polars_lazy():
    ...

def polars_eager():
    ...

def main(lazy: bool=False):
    if lazy:
        print('executing lazy mode')
        return polars_lazy()
    else:
        print('executing eager mode')
        return polars_eager()
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Measure time of two executions.')
    parser.add_argument('-l', '--lazy', action='store_true', default=False, help='use lazy execution')
    args = parser.parse_args()
    main(args.lazy)
