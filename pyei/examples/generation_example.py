import pandas as pd
import numpy as np
from r_by_c import RowByColumnEI
from io_utils import to_netcdf

election_dataframe = pd.read_csv("../example_data/Warnock_Loeffler_Example.csv")

# demographic groups of interest sum to 1 within each precinct.
group_fractions_rbyc = np.array(election_dataframe[['White', 'Black', 'Hispanic', 'Asian', 'Other']]).T

# These fractions  must sum to 1 within each precinct.
votes_fractions_rbyc = np.array(election_dataframe[['Warnock', 'Loeffler', 'Abstain']]).T

# the sum of the counts of votes for the candidates of interest
precinct_pops = np.array(election_dataframe['Total Population']).astype(int)

candidate_names_rbyc = ["Raphael Warnock (D)", "Kelly Loeffler (R)", "Abstain"]
demographic_group_names_rbyc = ["White", "Black", "Hispanic", "Asian", "Other"]
# remove the below line if you do not have precinct names or do not need to use them
precinct_names = election_dataframe['PRECINCTID']

# Fitting a first r x c model

# Create a RowByColumnEI object
ei_rbyc = RowByColumnEI(model_name='multinomial-dirichlet')

# Fit the model
ei_rbyc.fit(group_fractions_rbyc,
       votes_fractions_rbyc,
       precinct_pops,
       demographic_group_names=demographic_group_names_rbyc,
       candidate_names=candidate_names_rbyc,
       precinct_names=precinct_names,
       chains=3
)

# Generate a simple report to summarize the results
print(ei_rbyc.summary())

# VERY IMPORTANT, avoids having to re-run the model fitting every time you try to analyze the data
to_netcdf(ei_rbyc, '../netcdfs/WarnockLeoffler_2021.netcdf')
