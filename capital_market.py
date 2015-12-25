""" 
Please feel free to use the code without citing or crediting the author(s) mentioned below. Cheers to science :-)
I'd be happy to hear from you about how to improve this code, and as to how the code may have been useful to you.
	
Author: Vipin P. Veetil
Contact: vipin.veetil@gmail.com

Paper title: Out-of-equilibrium dynamics with heterogeneous capital goods
Paper URL: http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2600648

Language: Python 

Module name: market
Module description: describes the structure of interact between the different firms
"""

from __future__ import division
import random


class CapitalMarket(object):
	""" the process through which goods-firms buy capital from capital firms  """
	def __init__(self):

		""" parameters of the capital market are listed in alphabetical order """
		self.kinds_of_capital = None
		self.number_of_firms = None
		self.unit_of_capital = None

		self.capital_firms = []
		self.goods_firms = []
		self.trade_prices_capital = None
		""" store the price at which different kinds of capital are traded """
		self.capital_flow = None
		self.count = 0
	
	def initialize(self):
		self.capital_flow = dict((k, 0) for k in range(0, self.kinds_of_capital))
		self.trade_prices_capital = dict((k, []) for k in range(0, self.kinds_of_capital))

	def exhaust_gains_from_trade(self,capital_firm, goods_firm, capital_type):
		""" a recursive function to exhausted gaints from trade between the two firms """

		ask = capital_firm.ask(capital_type)
		bid = goods_firm.bid(capital_type)
		
	
		if capital_firm.is_there_inventory() == True and bid > ask:
			self.count += 1
			tradePrice = (bid + ask) / 2
			""" trade price is the mean of bid and ask """
			capital_firm.decrease_inventory()
			""" the capital firm decreases its inventory of capital """
			goods_firm.add_capital_stock(capital_type)
			""" the goods firm increases it stock of capital """
			self.trade_prices_capital[capital_type].append(tradePrice)
			capital_firm.append_trade_price(tradePrice)
			self.capital_flow[capital_type] += self.unit_of_capital
			self.exhaust_gains_from_trade(capital_firm, goods_firm, capital_type)
			""" recurssion """

	def binary_matches(self):
		trades = dict((k, []) for k in range(0, self.kinds_of_capital))
		random.shuffle(self.capital_firms)
		""" shuffle the capital firms so that the same firms are not matched every round """
		
		for index in xrange(self.number_of_firms):
			self.count = 0
			goods_firm = self.goods_firms[index]
			capital_firm = self.capital_firms[index]
			capital_type = capital_firm.which_capital_type()
			self.exhaust_gains_from_trade(capital_firm, goods_firm, capital_type)
	#			print "count", self.count

#print "capital type", capital_type
#			print "inventory", capital_firm.inventory
#			print "cost", capital_firm.cost
#			inc = goods_firm.bid(capital_type)
#			print "incremental product", inc
#			print "stock of goods firm", goods_firm.capital_stock



	def close_capital_market(self):
		for capital_firm in self.capital_firms:
			capital_firm.compute_expectation_error()
			capital_firm.update_price_expectation()
			capital_firm.end_capital_market()

		self.capital_flow = dict((k, 0) for k in range(0, self.kinds_of_capital))
		self.trade_prices_capital = dict((k, []) for k in range(0, self.kinds_of_capital))







