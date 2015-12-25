""" 
Please feel free to use the code without citing or crediting the author(s) mentioned below. Cheers to science :-)
I'd be happy to hear from you about how to improve this code, and as to how the code may have been useful to you.
	
Author: Vipin P. Veetil
Contact: vipin.veetil@gmail.com

Paper title: Out-of-equilibrium dynamics with heterogeneous capital goods
Paper URL: http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2600648

Language: Python

Module name: time_step
Module description: the processes that unfold in one time step
"""

from __future__ import division

import numpy as np
from scipy import stats
import parameters as para
import copy



class TimeStep(object):
	def __init__(self):
		self.kinds_of_capital = None
		self.economy = None
		self.prices_capital = None
		""" all the prices at which different kinds of capital are traded """
		self.mean_price_capital = None
		""" the mean price at which different kinds of capital are traded """
		self.stock_capital = None
		""" the stock of different kinds of capital owned by each goods firm """
		self.stock_capital_economy = None
		""" the total stock of each kind of capital """
		self.flow_capital_economy = None
		""" the quantities of different kinds of capital traded """
		self.errors_expectations_capital_price = None
		""" the errors in capital price expectations of each capital firm """
		self.errors_expectations_capital_price_economy = None
		""" the proportion of matches of different kinds of capital that do not result in trades """
		self.unit_of_capital = None
		self.variation_price_expectation = {}
	
	def initialize(self):
		self.kinds_of_capital = self.economy.kinds_of_capital
		self.prices_capital = dict((k, []) for k in range(0, self.kinds_of_capital))
		self.mean_price_capital = dict((k, 0) for k in range(0, self.kinds_of_capital))
		self.stock_capital = dict((k, []) for k in range(0, self.kinds_of_capital))
		self.stock_capital_economy = dict((k, 0) for k in range(0, self.kinds_of_capital))
		self.flow_capital_economy = dict((k, 0) for k in range(0, self.kinds_of_capital))
		self.errors_expectations_capital_price = dict((k, []) for k in range(0, self.kinds_of_capital))
		self.errors_expectations_capital_price_economy = dict((k, []) for k in range(0, self.kinds_of_capital))
		self.variation_price_expectation = dict((k, 0) for k in range(0, self.kinds_of_capital))
	
	def capital_step(self):
		for capital_firm in self.economy.capital_firms:
			if capital_firm.inventory > self.unit_of_capital:
				capital_firm.mark_down_cost()
			else:
				capital_firm.produce()
				""" capital firms produce """
				capital_firm.compute_cost_per_unit_capital()

		self.economy.capital_market.binary_matches()
		""" binary matches between goods firms and capital firms """
		self.prices_capital = self.economy.capital_market.trade_prices_capital
		for capital in xrange(self.kinds_of_capital):
			self.flow_capital_economy[capital] =  self.economy.capital_market.capital_flow[capital]

		self.economy.capital_market.close_capital_market()
		""" sets data store structures to blank """
	
	def labor_step(self):
		self.economy.labor_auctioneer.which_capital_firms_in_labor_market()
		""" labor auctioneer determines which capital firms are in the labor market """
		self.economy.labor_auctioneer.compute_wage()
		"""  labor auctioneer computes market clearing wage """
		self.economy.labor_auctioneer.allocate_labor()
		""" labor auctioneer allocates labor to the capital firms """

	def goods_step(self):
		for goods_firm in self.economy.goods_firms:
			goods_firm.produce()
		""" goods firms produce output """
		self.economy.goods_auctioneer.collect_output_from_goods_firms()
		""" goods auctioneer collects output from the goods firms """
		self.economy.goods_auctioneer.compute_goods_price()
		""" goods auctioneer computes market clearing price """
	
	def compute_statistics(self):
		price_expectations = dict((k, []) for k in range(0, self.kinds_of_capital))

		for capital_firm in self.economy.capital_firms:
			if capital_firm.error_capital_price_expectation != None:
				self.errors_expectations_capital_price[capital_firm.capital_type].append(capital_firm.error_capital_price_expectation)
			price_expectations[capital_firm.capital_type].append(capital_firm.expected_price)
		for capital in xrange(self.kinds_of_capital):
			self.variation_price_expectation[capital] = stats.variation(price_expectations[capital])
		
		for capital in xrange(self.kinds_of_capital):
			self.errors_expectations_capital_price_economy[capital] = np.mean(self.errors_expectations_capital_price[capital])

		for goods_firm in self.economy.goods_firms:
			""" record the stock of different kinds of capital held by different capital firms in the economy"""
			for capital in xrange(self.kinds_of_capital):
				self.stock_capital[capital].append(goods_firm.capital_stock[capital])

		for capital in xrange(self.kinds_of_capital):
			self.stock_capital_economy[capital] = np.sum(self.stock_capital[capital])
	

		for capital in xrange(self.kinds_of_capital):
			self.mean_price_capital[capital] = np.mean(self.prices_capital[capital])
	

	def close_time_step(self):
		self.prices_capital = dict((k, []) for k in range(0, self.kinds_of_capital))
		self.mean_price_capital = dict((k, 0) for k in range(0, self.kinds_of_capital))
		self.stock_capital = dict((k, []) for k in range(0, self.kinds_of_capital))
		self.stock_capital_economy = dict((k, 0) for k in range(0, self.kinds_of_capital))
		self.flow_capital_economy = dict((k, 0) for k in range(0, self.kinds_of_capital))
		self.errors_expectations_capital_price = dict((k, []) for k in range(0, self.kinds_of_capital))
		self.variation_price_expectation = dict((k, 0) for k in range(0, self.kinds_of_capital))
		self.errors_expectations_capital_price_economy = dict((k, []) for k in range(0, self.kinds_of_capital))



