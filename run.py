""" 
Please feel free to use the code without citing or crediting the author(s) mentioned below. Cheers to science :-)
I'd be happy to hear from you about how to improve this code, and as to how the code may have been useful to you.
	
Author: Vipin P. Veetil
Contact: vipin.veetil@gmail.com

Paper title: Out-of-equilibrium dynamics with heterogeneous capital goods
Paper URL: http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2600648

Language: Python

Module name: run
Module description: runs the economy foward in time
"""
from __future__ import division
import parameters as para
import time_step as ts
import economy
from operator import truediv
from operator import add
from operator import mul
import numpy as np


class RunEconomy(object):
	def __init__(self):

		self.time_step = ts.TimeStep()
		""" time steps """
		self.economy = economy.Economy()
		""" economy """

		""" the parameters of the economy are listed in alphabetical order """
		
		self.depreciation = None
		self.goods_demand_parameter_deterministic = None
		self.goods_firm_exponents = None
		self.is_goods_demand_stochastic = None
		self.kinds_of_capital = None
		self.labor_productivity = None
		self.labor_supply = None
		self.number_of_firms = None
		self.stochastic_goods_demand_mean = None
		self.stochastic_goods_demand_variance = None
		self.time_steps = None
		self.unit_of_capital = None
		self.price_adjustment = None
		
		
		""" following data are recorded """

		self.capital_stock = {}
		self.capital_stock_ratio = []
		""" the stock of different kinds of capital at each time step """
		self.errors_expectations_capital_price = {}
		""" the mean error in price expectation of different kinds of capital at each time step """
		self.flow_capital = {}
		""" the quantity of different kinds of capital traded at each time step """
		self.mean_price_capital = {}
		"""  mean price at which different kinds of capital are traded each time step """
		
		""" following data are computed from recorded data """

		self.errors_weighted = []
		self.relative_price_capital = []
		""" price of capital zero divided by price of capital one """
		self.capital_stock_ratio = []
		""" stock of capital zero divided by stock of capital one  """
		self.total_errors = []
		self.variation_price_expectation = {}
	
	def initialize(self):
		""" initial data structures """
		self.capital_stock = dict((k, []) for k in range(0, self.kinds_of_capital))
		self.errors_expectations_capital_price = dict((k, []) for k in range(0, self.kinds_of_capital))
		self.flow_capital = dict((k, []) for k in range(0, self.kinds_of_capital))
		self.mean_price_capital = dict((k, []) for k in range(0, self.kinds_of_capital))
		self.time_step.unit_of_capital = self.unit_of_capital
		self.variation_price_expectation = dict((k, []) for k in range(0, self.kinds_of_capital))

	def create_economy(self):
		""" create economy and assign parameters """
		self.economy.price_adjustment = self.price_adjustment
		self.economy.depreciation = self.depreciation
		self.economy.goods_demand_parameter_deterministic = self.goods_demand_parameter_deterministic
		self.economy.goods_firm_exponents = self.goods_firm_exponents
		self.economy.kinds_of_capital = self.kinds_of_capital
		self.economy.labor_productivity = self.labor_productivity
		self.economy.labor_supply = self.labor_supply
		self.economy.number_of_firms = self.number_of_firms
		self.economy.stochastic_goods_demand_mean = self.stochastic_goods_demand_mean
		self.economy.stochastic_goods_demand_variance = self.stochastic_goods_demand_variance
		self.economy.unit_of_capital = self.unit_of_capital

		self.economy.create_economy()
		""" create economy is at the end because the above parameters are assigned when economy is created """

	def record_data(self):
		for capital in xrange(self.kinds_of_capital):
			self.capital_stock[capital].append(self.time_step.stock_capital_economy[capital])
			self.errors_expectations_capital_price[capital].append(self.time_step.errors_expectations_capital_price_economy[capital])
			self.flow_capital[capital].append(self.time_step.flow_capital_economy[capital])
			self.mean_price_capital[capital].append(self.time_step.mean_price_capital[capital])
			self.variation_price_expectation[capital].append(self.time_step.variation_price_expectation[capital])

	def run_forward_in_time(self):
		self.time_step.economy = self.economy
		self.time_step.initialize()
		for time in xrange(self.time_steps):
			if time % 100 == 0:
				print "time step", time
			self.time_step.labor_step()
			self.time_step.capital_step()
			self.time_step.goods_step()
			self.time_step.compute_statistics()
			self.record_data()
			self.time_step.close_time_step()

	def compute_run_statistics(self):
		self.relative_price_capital = map(truediv, self.mean_price_capital[0], self.mean_price_capital[1])
		""" price of capital zero divided by price of capital one """
		self.capital_stock_ratio = map(truediv, self.capital_stock[0], self.capital_stock[1])
		""" stock of capital zero divided by stock of capital one  """



"""
		market.create_firms()
		for time in self.time_steps:
			market.time_step()
			if self.shock==True:
                if time == self.shock_time:
                    self.goods_firms_exponents = self.after_shock_exponents
                    for j in self.goods_firms:
                        j.exponents = self.goods_firms_exponents

        self.compute_summary_statistics()
		
"""

