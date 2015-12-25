from __future__ import division
from operator import truediv
import economic_functions as ef
import goods_firm
import capital_firm
import capital_market



ef_instance = ef.EconomicFunctions()
gf_instance = goods_firm.GoodsFirm()
cf_instance = capital_firm.CapitalFirm()
market_instance = capital_market.CapitalMarket()

variables = [2,3]
exponents =[0.9,0.3]

gf_instance.kinds_of_capital = 2
gf_instance.initialize()
gf_instance.exponents = exponents
gf_instance.capital_stock = variables
gf_instance.depreciation = 0.5
gf_instance.unit_of_capital = 1
gf_instance.expected_price_of_goods = 10




cf_instance.initialize()
cf_instance.capital_type = 0
cf_instance.labor_productivity = 0.5
cf_instance.labor = 89
cf_instance.unit_of_capital = 1
cf_instance.produce()
cf_instance.wage = 5


cf_instance.compute_cost_per_unit_capital()

inv = cf_instance.is_there_inventory()

cf_instance.update_labor_wage(100, 20)

cf_instance.trade_prices = []
cf_instance.append_trade_price(1)
cf_instance.append_trade_price(2)
cf_instance.append_trade_price(3)
cf_instance.expected_price = 2
error =  cf_instance.expectation_error()

market_instance.kinds_of_capital = 2
market_instance.unit_of_capital = 1
market_instance.initialize()


cf_instance.cost = 1
cf_instance.inventory = 100
ask = cf_instance.ask(0)
print "ask", ask
bid = gf_instance.bid(0)
print "bid", bid


units_traded = market_instance.exhaust_gains_from_trade(cf_instance, gf_instance, 0)

print "units traded",  units_traded




































