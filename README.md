# PyEI_U
An updated version of PyEI, a Python library for ecological inference.


Credit for the original version of PyEI:
Knudson et al., (2021). PyEI: A Python package for ecological inference. Journal of Open Source Software, 6(64), 3397, https://doi.org/10.21105/joss.03397


Original GitHub: https://github.com/mggg/ecological-inference


## Installation

Using PyEI requires the following:
```
pyei 1.0.1
jax 0.4.14
jaxlib 0.4.14
pymc 4.0.0b5
pandas 1.5.3
numpy 1.23.5
```

**PyEI may not function properly unless these specific package versions are installed**

Any version of Python >= 3.7 should work, although only Python 3.10 has been fully tested.

PyCharm is **highly** recommended, as it is the only confirmed working environment, and it is very straightforward to install specific package versions with.

Refer to the "PyCharm Setup.pdf" file, supplied by Professor Kelly to install PyCharm. To install specific package versions, follow the same guide and select the specific version box when installing your packages.


## Examples

pyei/examples has some example programs which show how to utilize some basic functions of PyEI and its updated features.

pyei/sample_data has some small example data sets to use as well.

The original PyEI [GitHub](https://github.com/mggg/ecological-inference) has many examples and intro notebooks, however, it is recommended to start with the examples included here and go to the original examples if further documentation is needed.


## Added functionalities


A brief summary of the functionalities PyEI_U has added to PyEI. See the in-code documentation for further detail


```
r_by_c.py :

    Updated:

    precinct_level_plot() :
        --has the optional 'max_precincts' argument added.
         
    precinct_level_estimates() :
        --automatically calls calculate_turnout_adjusted_summary if not called prior when non_candidate_names is not None

    New:

    get_PLE_by_precinct_name(precinct_names ...): 
        --prints the formatted PLE data for the given array of precinct ids. 
        Takes optional arguments for restricting the candates, groups, and type of PLE data(PPM or PCI only)

    get_PLE_by_precinct_name(precinct_names ...): 
        --returns an array of the the PLE data for the given array of precinct ids. 
        Takes optional arguments for restricting the candates, groups, and type of PLE data(PPM or PCI only)

plot_utils.py :

    Updated:

    plot_precincts(voting_prefs) :
        --has the 'max_precincts' argument and functionality added.

```