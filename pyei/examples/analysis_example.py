from io_utils import from_netcdf

ei = from_netcdf('WarnockLeoffler_2021.netcdf')

print(ei.summary())
# print(ei.candidate_of_choice_report())
# print(ei.candidate_of_choice_polarization_report())

print("Precinct names")
print(ei.precinct_names)

print("Candidate names")
print(ei.candidate_names)

print("Demographic names")
print(ei.demographic_group_names)


print("\nPrinting example 1")
ei.print_PLE_by_precinct_name(precinct_names=["0011B"])

print("\nPrinting example 2")
ei.print_PLE_by_precinct_name(precinct_names=["0011B"], non_candidate_names=["Abstain"], print_only="PCI",
                                groups=["Hispanic"])
print("\nPrinting example 3")
ei.print_PLE_by_precinct_name(precinct_names=["0011B", "009321W"], non_candidate_names=["Abstain"], print_only="PPM",
                                candidates=["Kelly Loeffler (R)"], groups=["White", "Black"])


print("\nGetting example 1")
getting_example1 = ei.get_PLE_by_precinct_name(precinct_names=["0011B"], non_candidate_names=["Abstain"],
                                    candidates=["Kelly Loeffler (R)"], groups=["White", "Black"])
print(getting_example1)


print("\nGetting example 2")
getting_example2 = ei.get_PLE_by_precinct_name(precinct_names=["0011B"], non_candidate_names=["Abstain"],
                                    get_only="PPM",
                                    candidates=["Kelly Loeffler (R)"], groups=["White"])
print(getting_example2)