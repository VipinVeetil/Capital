""" 
Please feel free to use the code without citing or crediting the author(s) mentioned below. Cheers to science :-)
I'd be happy to hear from you about how to improve this code, and as to how the code may have been useful to you.
	
Author: Vipin P. Veetil
Contact: vipin.veetil@gmail.com

Paper title: Out-of-equilibrium dynamics with heterogeneous capital goods
Paper URL: http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2600648

Language: Python

Module name: capital_firms
Module description: this module describes the firms that use labor to produce different kinds of capital goods.
"""


from __future__ import division
import math
import time
import random
import collections
import csv
import numpy as np
import copy
import operator



class CapitalFirm(object):
	""" capital producing firm """
	def __init__(self):
		
		""" parameters of capital firms  """
		self.capital_type = None
		""" type of capital that the firm produces """
		self.error_capital_price_expectation = None
		self.labor_productivity = None
		""" productivity of labor in producing capital k = l ** labor_productivity """
		self.price_adjustment = None
		""" proportion reduction in asking price of capital if there is unsold inventory """
		self.unit_of_capital = None
		""" quantity of capital exchanged every trade """
		self.labor = None
		""" quantity of labor bought last period """
		self.inventory = None
		""" quantity of inventory of capital """
		self.wage = None
		""" wage paid to labor """
		self.cost = None
		""" cost of producing a unit of capital """
		self.output = None
		""" quantity of output produced """
		self.expected_price = None
		""" expected price of capital. It is initialized with a random number between 0 and 1 """
		self.trade_prices = None
		""" list of the prices at which the firm sells capital. Every time step, the list is erased and filled with new data
		    since a firm sells different units of capital at different prices, the list will have numbers
		"""
	
	def initialize(self):
		price = random.uniform(0,1)
		self.cost = random.uniform(0,1)
		self.expected_price = price
		self.trade_prices = [price]
		self.labor = random.uniform(0,100)
		self.inventory = 0

	def which_capital_type(self):
		""" return the  kind of capital the firm produces"""
		return self.capital_type

	def produce(self):
		""" produce capital using labor and put the output in inventory """
		output = self.labor ** self.labor_productivity
		self.output = output
		self.inventory += output

	def compute_cost_per_unit_capital(self):
		""" compute the cost of producing a unit of capital """
		total_wage = self.wage * self.labor
		self.cost = copy.copy(total_wage / self.output)
	
	def is_there_inventory(self):
		""" return True if the firm has at least one unit of capital in inventory """
		return self.inventory > 1

	def decrease_inventory(self):
		""" decrease inventory """
		self.inventory -= self.unit_of_capital
	
	def ask(self, capital_type):
		assert capital_type == self.capital_type, "firm does not have the kind of capital"
		return self.cost

	def update_labor_wage(self,labor,wage):
		""" update the quantity of labor bought and the wage """
		self.labor = labor
		self.wage = wage

	def append_trade_price(self, trade_price):
		""" record the price at which trades happen """
		self.trade_prices.append(trade_price)

	def compute_expectation_error(self):
		""" Compute the errors in price expectations """
		squared_errors = []
		if len(self.trade_prices) != 0:
			for price in self.trade_prices:
				error = (price - self.expected_price) / price
				squared_error = error ** 2
				squared_errors.append(squared_error)
			self.error_capital_price_expectation = (np.mean(squared_errors)) ** 0.5
	
	def mark_down_cost(self):
		""" mark down the cost of capital if there is unsold inventory """
		""" the decrease in cost, lowers ask prices """
		assert self.inventory > self.unit_of_capital, "There is no unsold inventory"
		self.cost *= (1 - self.price_adjustment)
	
	def update_price_expectation(self):
		#		print "trade price", self.trade_prices
		""" set next periods expected price as last periods mean trade price """
		if len(self.trade_prices) != 0:
			self.expected_price = copy.copy(np.mean(self.trade_prices))


	def end_capital_market(self):
		""" resets variables at the end of a time step """
		self.trade_prices = []
