"""
Please feel free to use the code without citing or crediting the author(s) mentioned below. 
Cheers to science :-)
I'd be happy to hear from you about how to improve this code.

Author: Vipin P. Veetil
Contact: vipin.veetil@gmail.com

Code language: Python

Module name: economic  sfunctions
Module description: functions that are commonly used in economics.
"""

from __future__ import division
import math
import copy
import random

class EconomicFunctions(object):
	def __init__(self):
		self.some_variable = 1

	def cobb_douglas(self, variables_list, exponents_list):
		""" Cobb-Douglas Function """
		number_of_variables = len(variables_list)
		number_of_exponents = len(exponents_list)
		assert number_of_variables == number_of_exponents, "number of variables does not equal number of exponents"
		value = 1
		for variable in xrange(number_of_variables):
			temp = variables_list[variable] ** exponents_list[variable]
			value *= temp
		return value

	def incremental_value(self, variables_list, exponents_list, which_variable, incremental_quantity, which_function):
		""" the change in the value of a function from a change in one of its variables """
		""" the discrete version of marginal product/marginal utility, with the discrete unit as an argument """
		if which_function == "Cobb-Douglas":
			new_variables_list = copy.copy(variables_list)
			assert which_variable < len(variables_list), "variable not in list"
			new_variables_list[which_variable] += incremental_quantity
			""" new list of variables with an additional unit of one of the variables """

			value_increment = self.cobb_douglas(new_variables_list, exponents_list) - self.cobb_douglas(variables_list, exponents_list)
			""" new value with additional unit of a variable minus old value """
			return value_increment

	def geometric_brownian_motion_single_value(self, drift, volatility, initial_value):
		dt = 1
		new_value = initial_value * math.exp((drift - ((volatility ** 2) / 2.0) * dt + volatility * random.normalvariate(0, dt * dt)))
		return new_value
