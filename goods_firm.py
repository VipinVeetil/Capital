""" 
Please feel free to use the code without citing or crediting the author(s) mentioned below. Cheers to science :-)
I'd be happy to hear from you about how to improve this code, and as to how the code may have been useful to you.

Author: Vipin P. Veetil
Contact: vipin.veetil@gmail.com

Paper title: Out-of-equilibrium dynamics with heterogeneous capital goods
Paper URL: http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2600648

Code language: Python

Module name: goods_firms
Module description: this module describes the firms that use different kinds of capital goods to produce consumption good.
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
import economic_functions as ef
import parameters as para


class GoodsFirm(object):
	""" goods producing firms """
	def __init__(self):
		self.ef = ef.EconomicFunctions()
		""" economic functions  """
		
		""" parameters of goods firms """
		self.depreciation = None
		""" all kinds of capital depreciate at the same rate """
		self.exponents = None
		""" Cobb-Douglas exponents """
		self.kinds_of_capital = None
		""" the number of kinds of capital used """
		self.unit_of_capital = None
		""" units in which capital is traded """
		self.expected_price_of_goods = None
		""" expected price of goods """
		self.capital_stock = None
		""" the quantity of different kinds of capital held """
		self.goods_output = 0
		""" the output produced """


	def initialize(self):
		self.capital_stock = dict((k, random.uniform(1, 10)) for k in range(0, self.kinds_of_capital))
		self.expected_price_of_goods = random.uniform(1,10)
	
	def produce(self):
		""" produce output """
		self.goods_output = self.ef.cobb_douglas(self.capital_stock,self.exponents)
		
		""" record output """
		for capital in xrange(self.kinds_of_capital):
			""" depreciate capital """
			self.capital_stock[capital] *= (1 - self.depreciation)

	def bid(self, capital_type):
		incremental_product = self.ef.incremental_value(self.capital_stock, self.exponents, capital_type, self.unit_of_capital, "Cobb-Douglas")
		incremental_revenue_product = incremental_product * self.expected_price_of_goods
		return incremental_revenue_product

	def add_capital_stock(self, capital_type):
		""" change capital stock """
		self.capital_stock[capital_type] += self.unit_of_capital
    
	def update_expected_price_of_goods(self, price):
		""" updated the expected price of good """
		self.expected_price_of_goods = price