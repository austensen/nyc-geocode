# NYC-Geocode

Geocode CSV of NYC addresses using [usaddress](https://parserator.datamade.us/usaddress/) to parse the addresses into necessary parts and [docker-geosupport](https://github.com/NYCPlanning/docker-geosupport) for geocoding.

## Getting Started

First you'll need to install [Docker Desktop](https://www.docker.com/get-started).

Add the CSV you want to geocode to the `data/` directory within this project. This file should have a header row for column names, and include a single column with the full street address to be parsed and geocoded.

From the project's root directory, run `docker compose build` to build the container.

To geocode the file, you'll need to set the following arguments: 
* csv file to geocode, 
* csv file for output results, 
* single column name in the csv with the address, 
* optional: any additional columns that you want to include in the output (each as separate arguments), or `"*"` to keep all columns form the input file.

```shell
docker compose run nyc-geocode "data/addresses.csv" "data/addresses_geocoded.csv" "addr_full" "extra_col1" "extra_col2"
```
