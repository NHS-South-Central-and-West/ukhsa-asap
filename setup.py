from setuptools import setup

setup(
    name='ukhsa-asap',
    version='0.1.0',
    description='Import the data that feeds the UKHSA dashboard',
    author='Specialist Analytics Team - BI Analytics - South, Central and West CSU',
    author_email='scwcsu.analytics.specialist@nhs.net',
    packages=['ukhsa-asap'],
    install_requires=[
        'polars',
        'pandas',
        'urllib3',
        'json'
    ],
)