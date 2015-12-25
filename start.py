""" 
Please feel free to use the code without citing or crediting the author(s) mentioned below. Cheers to science :-)
I'd be happy to hear from you about how to improve this code, and as to how the code may have been useful to you.
	
Author: Vipin P. Veetil
Contact: vipin.veetil@gmail.com

Paper title: Out-of-equilibrium dynamics with heterogeneous capital goods
Paper URL: http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2600648

Language: Python

Module name: start
Module description: starts the simulation process
"""

from __future__ import division
import simulations as sim

class Start(object):
	def __init__(self):
		self.variable = 1
		self.simulation = sim.Simulation()

	def begin_simulations(self):
		self.simulation.run_simulation()

start_instance = Start()
start_instance.begin_simulations()
print "done"
