from koneroj import makebook
list=[ 'partition.tex',
'partition_subinterval.tex',
'norm_of_a_partition.tex',
'riemann_sum.tex',
'definite_integral.tex',
'continues_functions_are_intergratable.tex',
'piecewise_continuous_function.tex',
'piecewise_continuous_functions_are_intergratable.tex',
'nonintergratable_function.tex']

intergration_rules = [
'intergral_rules/order_of_intergration.tex',
'intergral_rules/zero_width_interval.tex',
'intergral_rules/intergration_constant.tex',
'intergral_rules/intergration_sum_and_difference.tex',
'intergral_rules/additivity.tex',
'intergral_rules/max_min_inequality.tex',
'intergral_rules/domination.tex'
]

list += intergration_rules
list += [
'area.tex',
'mean_value_theorem_for_defininte_intergrals.tex',
'antiderivites_intergral.tex' ,
'intergral_of_odd_function.tex',
'intergral_of_even_function.tex',
'area_between_curves.tex'
]
volumn = [
'volume/volumn.tex',
'volume/volumn_by_disk.tex',
'volume/volumn_by_shell.tex'
]
list += volumn
name = 'calculus'
makebook(list,name)

