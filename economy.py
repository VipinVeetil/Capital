""" 
Please feel free to use the code without citing or crediting the author(s) mentioned below. Cheers to science :-)
I'd be happy to hear from you about how to improve this code, and as to how the code may have been useful to you.

Author: Vipin P. Veetil
Contact: vipin.veetil@gmail.com

Paper title: Out-of-equilibrium dynamics with heterogeneous capital goods
Paper URL: http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2600648

Language: Python

Module name: time_step
Module description:

"""



from __future__ import division
import capital_firm as cf
import goods_firm as gf
import capital_market
import goods_auctioneer
import labor_auctioneer
import parameters as para
import random

class Economy(object):
	def __init__(self):
		""" parameters of the economy are listed in alphabetical order """
		self.depreciation = None
		self.is_goods_demand_stochastic = None
		self.goods_demand_parameter_deterministic = None
		self.goods_firm_exponents = None
		self.is_goods_demand_stochastic = None
		self.kinds_of_capital = None
		self.labor_productivity = None
		self.labor_supply = None
		self.number_of_firms = None
		self.price_adjustment = None
		self.stochastic_goods_demand_mean = None
		self.stochastic_goods_demand_variance_percent = None
		self.unit_of_capital = None
		
		self.capital_firms = []
		self.capital_market = None
		self.goods_auctioneer = None
		self.goods_firms = []
		self.labor_auctioneer = None
	
	
	def create_capital_firms(self):
		self.capital_firms = [cf.CapitalFirm() for count in xrange(self.number_of_firms)]
		capital_type = 0
		for capital_firm in self.capital_firms:
			""" assign parameters to capital firms """
			capital_firm.unit_of_capital = self.unit_of_capital
			capital_firm.labor_productivity = self.labor_productivity
			capital_firm.price_adjustment = self.price_adjustment
			capital_firm.capital_type = capital_type
			capital_type += 1
			if capital_type == self.kinds_of_capital:
				capital_type = 0
			capital_firm.initialize()
	
	def create_goods_firms(self):
		""" populate a list with goods firms and assign parameters """
		self.goods_firms = [gf.GoodsFirm() for count in xrange(self.number_of_firms)]
		for goods_firm in self.goods_firms:
			""" assign parameter to goods firms """
			goods_firm.depreciation = self.depreciation
			goods_firm.exponents = self.goods_firm_exponents
			goods_firm.kinds_of_capital = self.kinds_of_capital
			goods_firm.unit_of_capital = self.unit_of_capital
			goods_firm.initialize()
	
	def create_capital_market(self):
		""" create a capital market and assign parameters """
		self.capital_market = capital_market.CapitalMarket()
		self.capital_market.kinds_of_capital = self.kinds_of_capital
		self.capital_market.number_of_firms = self.number_of_firms
		self.capital_market.unit_of_capital = self.unit_of_capital
		self.capital_market.capital_firms = self.capital_firms
		self.capital_market.goods_firms = self.goods_firms
		self.capital_market.initialize()
	
	def create_goods_auctioneer(self):
		""" create a goods auctionner and assign parameters """
		self.goods_auctioneer = goods_auctioneer.GoodsAuctioneer()
		self.goods_auctioneer.goods_demand_parameter_deterministic = self.goods_demand_parameter_deterministic
		self.goods_auctioneer.goods_firms = self.goods_firms
		self.goods_auctioneer.is_goods_demand_stochastic = self.is_goods_demand_stochastic
		self.goods_auctioneer.labor_productivity = self.labor_productivity
		self.goods_auctioneer.stochastic_goods_demand_mean = self.stochastic_goods_demand_mean
		self.goods_auctioneer.stochastic_goods_demand_variance = self.stochastic_goods_demand_variance
	
	def create_labor_auctioneer(self):
		""" create a labor auctioner and assign parameters """
		self.labor_auctioneer = labor_auctioneer.LaborAuctioneer()
		self.labor_auctioneer.capital_firms = self.capital_firms
		self.labor_auctioneer.kinds_of_capital = self.kinds_of_capital
		self.labor_auctioneer.labor_productivity = self.labor_productivity
		self.labor_auctioneer.labor_supply = self.labor_supply
		self.labor_auctioneer.unit_of_capital = self.unit_of_capital
	

	def create_economy(self):
		self.create_capital_firms()
		self.create_goods_firms()
		self.create_capital_market()
		self.create_goods_auctioneer()
		self.create_labor_auctioneer()






