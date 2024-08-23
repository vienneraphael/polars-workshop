### Take back your code from exercise 2 and try to run it lazily using `.lazy` or `scan_parquet` as well as `.collect()` in the end.

### Using `weather_big.parquet`, write a function that:
### 1. Selects the `timestamp` and `location_id` variables
### 2. Transform `location_id` to uppercase
### 3. Filter `location_id` being equal to `F244JQUZYJKB`
### 4. Return the corresponding df

### Write two versions of that function, one will be eager and one will be lazy.