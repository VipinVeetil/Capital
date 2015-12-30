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
import csv
from scipy import stats

class Simulation(object):
	def __init__(self):
		self.parameters = parameters.Parameters()
		self.run = run.RunEconomy()

	def parameter_values(self):
		self.parameters.depreciation = 0.1
		self.parameters.goods_demand_parameter_deterministic = 1000
		self.parameters.goods_firm_exponents = [0.1, 0.5]
		self.parameters.kinds_of_capital = 2
		self.parameters.labor_productivity = 0.5
		self.parameters.labor_supply = 10000
		self.parameters.number_of_firms = 100
		self.parameters.simulations = 1
 		self.parameters.time_steps = 100
		self.parameters.unit_of_capital = 1
		self.parameters.price_adjustment = 0.1
		self.parameters.goods_demand_volatility = 0

	
	def assign_run_parameters(self):
		self.run.depreciation = self.parameters.depreciation
		self.run.goods_demand_parameter_deterministic = self.parameters.goods_demand_parameter_deterministic
		self.run.goods_firm_exponents = self.parameters.goods_firm_exponents
		self.run.kinds_of_capital = self.parameters.kinds_of_capital
		self.run.labor_productivity = self.parameters.labor_productivity
		self.run.labor_supply = self.parameters.labor_supply
		self.run.number_of_firms = self.parameters.number_of_firms
		self.run.time_steps = self.parameters.time_steps
		self.run.unit_of_capital = self.parameters.unit_of_capital
		self.run.price_adjustment = self.parameters.price_adjustment
		self.run.goods_demand_volatility = self.parameters.goods_demand_volatility
	
	def run_simulation(self):
		self.parameter_values()

		increment_exponents_ratio = 0.005
		first_exponent_list = np.arange(0.01, 0.5, increment_exponents_ratio)
		increment_volatility = 0.0025
		volatility_list = np.arange(0.01, 0.25, increment_volatility)


		with open('stochastic_variance.csv', 'wb') as stochastic_variance:
			for volatility in volatility_list:
				print 'volatility', volatility
			
				self.parameters.goods_demand_volatility = volatility
				self.assign_run_parameters()
				self.run.initialize()
				self.run.create_economy()
				self.run.run_forward_in_time()
				self.run.compute_run_statistics()
				last_ten_percent_time_steps = int(self.parameters.time_steps * 0.1)
				list_stock_ratio = self.run.capital_stock_ratio[-last_ten_percent_time_steps:]
				list_stock_ratio = np.array(list_stock_ratio)
				
				list_stock_ratio = list_stock_ratio[~np.isnan(list_stock_ratio)]
				stock_variance = stats.variation(list_stock_ratio)
				
				list_price_ratio = self.run.capital_price_ratio[-last_ten_percent_time_steps:]
				list_price_ratio = np.array(list_price_ratio)
				list_price_ratio = list_price_ratio[~np.isnan(list_price_ratio)]
				price_variance = stats.variation(list_price_ratio)
				writer = csv.writer(stochastic_variance, delimiter=',')
				writer.writerow([volatility] + [stock_variance] + [price_variance])


		with open('stock_price.csv', 'wb') as data_stock_price:
			for first_exponent in first_exponent_list:
				print 'first_exponent', first_exponent
		
				self.parameters.goods_demand_volatility = 0
				self.parameters.goods_firm_exponents = [first_exponent, 0.5]
				self.assign_run_parameters()
				self.run.initialize()
				self.run.create_economy()
				self.run.run_forward_in_time()
				self.run.compute_run_statistics()
				last_ten_percent_time_steps = int(self.parameters.time_steps * 0.1)
				list_stock_ratio = self.run.capital_stock_ratio[-last_ten_percent_time_steps:]
				list_stock_ratio = np.array(list_stock_ratio)
				list_stock_ratio = list_stock_ratio[~np.isnan(list_stock_ratio)]
				stock_ratio = np.mean(list_stock_ratio[-last_ten_percent_time_steps:])
				
				list_price_ratio = self.run.capital_price_ratio[-last_ten_percent_time_steps:]
				list_price_ratio = np.array(list_price_ratio)
				list_price_ratio = list_price_ratio[~np.isnan(list_price_ratio)]
				price_ratio = np.mean(list_price_ratio[-last_ten_percent_time_steps:])
				
				ratio_exponents = first_exponent / 0.5
				writer = csv.writer(data_stock_price, delimiter=',')
				writer.writerow([ratio_exponents] + [stock_ratio] + [price_ratio])


		with open('stochastic_stock_price.csv', 'wb') as stochastic_stock_price:
			for first_exponent in first_exponent_list:
				self.parameters.goods_demand_volatility = 0.1
				print 'stochastic first_exponent', first_exponent
			
				self.parameters.goods_firm_exponents = [first_exponent, 0.5]
				self.assign_run_parameters()
				self.run.initialize()
				self.run.create_economy()
				self.run.run_forward_in_time()
				self.run.compute_run_statistics()
				last_ten_percent_time_steps = int(self.parameters.time_steps * 0.1)
				list_stock_ratio = self.run.capital_stock_ratio[-last_ten_percent_time_steps:]
				list_stock_ratio = np.array(list_stock_ratio)
				list_stock_ratio = list_stock_ratio[~np.isnan(list_stock_ratio)]
				stock_ratio = np.mean(list_stock_ratio[-last_ten_percent_time_steps:])
				
				list_price_ratio = self.run.capital_price_ratio[-last_ten_percent_time_steps:]
				list_price_ratio = np.array(list_price_ratio)
				list_price_ratio = list_price_ratio[~np.isnan(list_price_ratio)]
				price_ratio = np.mean(list_price_ratio[-last_ten_percent_time_steps:])
				
				ratio_exponents = first_exponent / 0.5
				writer = csv.writer(stochastic_stock_price, delimiter=',')
				writer.writerow([ratio_exponents] + [stock_ratio] + [price_ratio])












