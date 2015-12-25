""" 
Please feel free to use the code without citing or crediting the author(s) mentioned below. Cheers to science :-)
I'd be happy to hear from you about how to improve this code, and as to how the code may have been useful to you.
	
Author: Vipin P. Veetil
Contact: vipin.veetil@gmail.com

Paper title: Out-of-equilibrium dynamics with heterogeneous capital goods
Paper URL: http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2600648

Language: Python 

Module name: labor auctioneer
Module description: labor auctioneer equates demand and supply of labor to determine equilibrium wage
"""
from __future__ import division
import parameters as para

class LaborAuctioneer(object):
	def __init__(self):
		
		self.labor_productivity = None
		self.labor_supply = None
		self.unit_of_capital = None
		self.kinds_of_capital = None

		self.wage = 0
		self.capital_firms = []
		self.capital_firms_in_labor_market = []

	def which_capital_firms_in_labor_market(self):
		""" determine which capital firms are in the labor market """
		for firm in self.capital_firms:
			if firm.inventory < self.unit_of_capital:
				self.capital_firms_in_labor_market.append(firm)

	def compute_wage(self):
		""" compute market clearing wage """
		""" equation 9 in the paper """
		sum_scaled_expected_prices = 0
		""" the sum of expected price of capital raised to an exponent """
		exponent = 1 / (1 - self.labor_productivity)
			
		for capital_firm in self.capital_firms_in_labor_market:
			sum_scaled_expected_prices += capital_firm.expected_price ** exponent
	
		first_term = self.labor_productivity / (self.labor_supply ** (1-self.labor_productivity))
		second_term = sum_scaled_expected_prices ** (1-self.labor_productivity)
		market_clearing_wage = first_term * second_term
		self.wage = market_clearing_wage
	
	
	def allocate_labor(self):
		""" allocate labor to capital firms """
		exponent = 1 / (1 - self.labor_productivity)
		common = (self.labor_productivity / self.wage) ** exponent
		
		for capital_firm in self.capital_firms_in_labor_market:
			firm_specific = capital_firm.expected_price ** exponent
			labor = common * firm_specific
			capital_firm.update_labor_wage(labor, self.wage)


