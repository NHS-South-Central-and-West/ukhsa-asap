# ukhsa-asap

## What is it?

A package that makes it easy to import the data from the [UKKHSA dashboard](https://ukhsa-dashboard.data.gov.uk/) using the [API](https://ukhsa-dashboard.data.gov.uk/access-our-data). It is inspired by the `fingertips_py` [package](https://fingertips-py.readthedocs.io/en/latest/) that allows users to import data directly from [Fingertips](https://fingertips.phe.org.uk/)

The intention is to create something user-friendly that does not require knowledge of how to create JSON API calls.

You will find an initial `UKHSA` class and some other exploratory bits in "starting_point.ipynb".

The aim is to get this registered on [PyPI](https://pypi.org/), the official Python package registry. [This](https://packaging.python.org/en/latest/tutorials/packaging-projects/) is the guide they link to for creating a package.

## Notes

Just jotting down some findings so far:

- The default setting for filters such as "stratum" and "sex" is "all", where everything is aggregated, rather than returning data for all of the categories split out.
- The API doesn't seem to support wildcards (as of 2025-10-24).
- "epiweek" refers to Epidemiological Week, which runs from Sunday to Saturday, and the first one of the year is on or after the 4th January.
- The "date" filter refers to activity on a specific `yyyy-mm-dd` date.
- The "sex" filter can be "m", "f" or "all".
