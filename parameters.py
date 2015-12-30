"""
Please feel free to use the code without citing or crediting the author(s) mentioned below. Cheers to science :-)
I'd be happy to hear from you about how to improve this code, and as to how the code may have been useful to you.

Author: Vipin P. Veetil
Contact: vipin.veetil@gmail.com

Paper title: Out-of-equilibrium Dynamics with Heterogeneous Capital Goods
Paper URL: http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2600648

Code language: Python

Module name: parameters
Module description: parameters of the model
"""

from __future__ import division

class Parameters(object):
	def __init__(self):
		after_shock_exponents = None
		depreciation = None
		goods_demand_parameter_deterministic = None
		goods_demand_volatility = None
		goods_firm_exponents = None
		is_goods_demand_stochastic = None
		kinds_of_capital = None
		labor_productivity = None
		labor_supply = None
		number_of_firms = None
		price_adjustment = None
		rounds = None
		shock_time = None
		stochastic_goods_demand_mean = None
		stochastic_goods_demand_variance = None
		time_steps = None
		unit_of_capital = None

		
