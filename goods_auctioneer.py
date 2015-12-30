"""
Please feel free to use the code without citing or crediting the author(s) mentioned below. Cheers to science :-)
I'd be happy to hear from you about how to improve this code, and as to how the code may have been useful to you.
	
Author: Vipin P. Veetil
Contact: vipin.veetil@gmail.com

Paper title: Out-of-equilibrium dynamics with heterogeneous capital goods
Paper URL: http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2600648

Language: Python

Module name: goods auctioneer
Module description: goods auctioneer equates demand and supply for the good to determine equilibrium price
"""
from __future__ import division
import parameters as para
import numpy as np
import copy
import economic_functions as ef

class GoodsAuctioneer(object):
	def __init__(self):
		
		""" the parameters of the goods auctioneer are listed in alphabetical order """
		self.goods_demand_parameter_deterministic = None
		self.goods_demand_parameter_last_time_step = None
		self.goods_demand_volatility = None
		self.goods_firms = None
		self.labor_productivity = None
		self.goods_output_economy = 0
		self.market_clearing_price = 0
		self.ef = ef.EconomicFunctions()

	def collect_output_from_goods_firms(self):
		""" once all goods firms have produced output, the goods auctioneer collects the output """
		self.goods_output_economy = 0
		for goods_firm in self.goods_firms:
			self.goods_output_economy += copy.copy(goods_firm.goods_output)

	def compute_goods_price(self):
		""" compute the market clearing price of the good """
		if self.goods_demand_volatility == 0:
			self.market_clearing_price = self.goods_demand_parameter_deterministic / self.goods_output_economy
		else:
			demand = self.ef.geometric_brownian_motion_single_value(0, self.goods_demand_volatility, self.goods_demand_parameter_last_time_step)
			self.market_clearing_price = demand / self.goods_output_economy
			self.goods_demand_parameter_last_time_step = demand

	def pass_price_to_goods_firms(self):
		for goods_firm in self.goods_firms:
			goods_firm.update_expected_price_of_goods(self.market_clearing_price)
