""" 
Please feel free to use the code without citing or crediting the author(s) mentioned below. Cheers to science :-)
I'd be happy to hear from you about how to improve this code, and as to how the code may have been useful to you.
	
Author: Vipin P. Veetil
Contact: vipin.veetil@gmail.com

Paper title: Out-of-equilibrium dynamics with heterogeneous capital goods
Paper URL: http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2600648

Language: Python

Module name: simulations
Module description: runs the economy many times
"""

from __future__ import division
import run
import parameters
import matplotlib.pyplot as plt
import numpy as np

class Simulation(object):
	def __init__(self):
		self.parameters = parameters.Parameters()
		self.simulations = 1
		self.run = run.RunEconomy()
		""" the number of simulations """

	def parameter_values(self):
		self.parameters.depreciation = 0.1
		self.parameters.goods_demand_parameter_deterministic = 1000
		self.parameters.goods_firm_exponents = [0.3, 0.7]
		self.parameters.is_goods_demand_stochastic = False
		self.parameters.kinds_of_capital = 2
		self.parameters.labor_productivity = 0.5
		self.parameters.labor_supply = 10000
		self.parameters.number_of_firms = 100
		self.parameters.simulations = 1
 		self.parameters.stochastic_goods_demand_mean = self.parameters.goods_demand_parameter_deterministic
		self.parameters.stochastic_goods_demand_variance = 0.1
 		self.parameters.time_steps = 1000
		self.parameters.unit_of_capital = 1
		self.parameters.price_adjustment = 0.1
	
	def assign_run_parameters(self):
		self.run.depreciation = self.parameters.depreciation
		self.run.goods_demand_parameter_deterministic = self.parameters.goods_demand_parameter_deterministic
		self.run.goods_firm_exponents = self.parameters.goods_firm_exponents
		self.run.is_goods_demand_stochastic = self.parameters.is_goods_demand_stochastic
		self.run.kinds_of_capital = self.parameters.kinds_of_capital
		self.run.labor_productivity = self.parameters.labor_productivity
		self.run.labor_supply = self.parameters.labor_supply
		self.run.number_of_firms = self.parameters.number_of_firms
		self.run.stochastic_goods_demand_mean = self.parameters.stochastic_goods_demand_mean
		self.run.stochastic_goods_demand_variance = self.parameters.stochastic_goods_demand_variance
		self.run.time_steps = self.parameters.time_steps
		self.run.unit_of_capital = self.parameters.unit_of_capital
		self.run.price_adjustment = self.parameters.price_adjustment
	
	def run_simulation(self):
		for simulation in xrange(self.simulations):
			self.parameter_values()
			self.assign_run_parameters()
			self.run.initialize()
			self.run.create_economy()
			self.run.run_forward_in_time()
			self.run.compute_run_statistics()
	

		plt.plot(list(range(0,self.run.time_steps)), self.run.variation_price_expectation[0])
		plt.plot(list(range(0,self.run.time_steps)), self.run.variation_price_expectation[1])
		plt.ylabel("variation in price expectation")
		plt.show()
		
		plt.plot(list(range(0,self.run.time_steps)), self.run.errors_expectations_capital_price[0])
		plt.plot(list(range(0,self.run.time_steps)), self.run.errors_expectations_capital_price[1])
		plt.ylabel("errors")
		plt.show()
		
		plt.plot(list(range(0,self.run.time_steps)), self.run.capital_stock[0])
		plt.plot(list(range(0,self.run.time_steps)), self.run.capital_stock[1])
		plt.ylabel("stock")
		plt.show()
		
		plt.plot(list(range(0,self.run.time_steps)), self.run.capital_stock_ratio)
		plt.ylabel("stock ratio")
		plt.ylim([0,1])
		plt.show()

		plt.plot(list(range(0,self.run.time_steps)),self.run.relative_price_capital)
		plt.ylabel("price ratio")
		plt.ylim([0,1])
		plt.show()





