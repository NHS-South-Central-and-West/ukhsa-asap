# ukhsa-asap development plans

## TODO:

- Create actual .py file; decide which elements should go in `main.py` and which elements should be split out into modules.
- Configure things such as the `setup.py` so that the package can be correctly installed and run as a package.
- Exception handling, for example when there is a bad response or the call returns no data.
- Include docstrings and inline comments.
- Find out how to get a list of all the categories for the optional filters in a request e.g. "stratum" and "age".
- Understand how the "age" filter works since it seems that there are set age bands, but there is also the possibility of using a custom age range.

## Future developments

- A method that returns a tree of all the levels of data available via the API (theme, geography, metric etc.). Suggested library for this is [treelib](https://treelib.readthedocs.io/en/latest/).
- A way for users to simply enter the metric name as a method argument & the whole request URL gets built from that. This may not be possible if metric names are not unique. However, some kind of more user-friendly option than filling out all the query arguments is highly desirable.
