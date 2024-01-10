# PyEI_U
An updated version of PyEI, a Python library for ecological inference.

Credit for the original version of PyEI:
Knudson et al., (2021). PyEI: A Python package for ecological inference. Journal of Open Source Software, 6(64), 3397, https://doi.org/10.21105/joss.03397

Original GitHub: https://github.com/mggg/ecological-inference

## Installation

Using PyEI requires the following:
```
jax 0.4.14
jaxlib 0.4.14
numba 56.4
numpy 1.23.5
pandas 1.5.3
pymc 4.0.0b5
```

**PyEI may not function properly unless these specific package versions are installed**

Any version of Python >= 3.7 should work, although only Python 3.10 has been fully tested.

PyCharm is **highly** recommended, as it is the only confirmed working environment, and it is very straightforward to install specific package versions with.

Refer to the "PyCharm Setup.pdf" file, supplied by Professor Kelly to install PyCharm. To install specific package versions, follow the same guide and select the specific version box when installing your packages.

## Examples

pyei/examples has some example programs which show how to utilize some basic functions of PyEI and its updated features.

pyei/example_data has some small example data sets to use as well.

The original PyEI [GitHub](https://github.com/mggg/ecological-inference) has many examples and intro notebooks, however, it is recommended to start with the examples included here and go to the original examples if further documentation is needed.

## Data Requirements

PyEI's ecological inference functionality requires both candidate votes by precinct, demographic-specific population by precinct, and total population by precinct.
PyEI requires input data to have all candidates' votes and demographics info to be in fractions by precinct (as in candidate votes/total votes demographic-specific population/total population), with the total population column in whole numbers.

PyEI takes data in file formats such as csv with the help of pandas. Csv is the only confirmed working file format.

The size breakdown of the "precincts" is irrelevant, and so VTDs or even districts work with PyEI as well as precincts.

It is highly recommended to use the [Redisticting Data Hub](https://redistrictingdatahub.org/), as their data is relatively reliable and plentiful.
Their website requires an account to download data, but it is free and very quick and easy to register.  
Keep in mind that data will still likely have mistakes, and that further effort may be required when combining and aligning multiple data sets (for example, 1 for demographics and 1 for candidate votes is often required).
Also of note, the RDH has many data sets which are broken down by "VTD" as opposed to by "precinct", but know these are very similar breakdowns and are often seen as interchangeable.

## Added functionalities

Here is a brief summary of the functionalities that PyEI_U has added to PyEI. See the in-code documentation for further detail

```
r_by_c.py:

    New:

    get_PLE_by_precinct_name(precinct_names ...):
        --prints the formatted PLE data for the given array of precinct ids.
        Takes optional arguments for restricting the candidates, groups, and type of PLE data(PPM or PCI only)

    get_PLE_by_precinct_name(precinct_names ...):
        --returns an array of the the PLE data for the given array of precinct ids.
        Takes optional arguments for restricting the candidates, groups, and type of PLE data(PPM or PCI only)

    Updated:

    precinct_level_plot():
        --has the optional 'max_precincts' argument added.
         
    precinct_level_estimates():
        --automatically calls calculate_turnout_adjusted_summary if not called prior when non_candidate_names is not None

plot_utils.py:

    Updated:

    plot_precincts(voting_prefs):
        --has the 'max_precincts' argument and functionality added.

```