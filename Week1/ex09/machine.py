# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    machine.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mpatrini <mpatrini@student.42roma.it>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/05/16 22:48:51 by mpatrini          #+#    #+#              #
#    Updated: 2022/05/18 04:56:30 by mpatrini         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import beverages
from random import randint
class CoffeeMachine:
	def __init__(self):
		self.used = 0
	a = beverages.HotBeverage("empty cup", 0.90, "An empty cup?! Gimme my money back!")
	def BrokenMachineException(self):
		raise Exception("\033[0;31mThis coffee machine has to be repaired.\033[0m")
	def repair(self):
		self.used = 0
	def serve(self, drink):
		if self.used == 10:
			self.BrokenMachineException()
		self.used += 1
		if (randint(0, 1000) % 7) == 0:
			return "You got a cup of {} for {}!".format(self.a.name, self.a.price)
		else:
			return "You got a cup of {} for {}!".format(drink.name, drink.price)

a = beverages.HotBeverage("coffe", 0.40, "A coffee, to stay awake.")
b = beverages.HotBeverage("tea", 0.30)
c = beverages.HotBeverage("chocolate", 0.50, "Chocolate, sweet chocolate...")
d = beverages.HotBeverage("cappuccino", 0.45, "Un po' di Italia nella sua tazza!")
m = CoffeeMachine()
list = [a, b, c, d]

for _ in range(22):
	num = randint(0, 3)
	try:
		print(m.serve(list[num]))
	except Exception as e:
		print(e)
		m.repair()
		print("\033[0;32mThe machine has been repaired.\033[0m")
