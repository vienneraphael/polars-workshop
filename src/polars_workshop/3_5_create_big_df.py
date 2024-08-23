import polars as pl

if __name__ == '__main__':
    pl.concat(
        [pl.read_parquet('weather.parquet')]*5,
        how='vertical'
    ).write_parquet('weather_big.parquet')