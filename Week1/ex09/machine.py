# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    machine.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mpatrini <mpatrini@student.42roma.it>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/05/16 22:48:51 by mpatrini          #+#    #+#              #
#    Updated: 2022/05/23 06:47:48 by mpatrini         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import beverages
from random import randint
class CoffeeMachine:
	def __init__(self):
			self.used = 0
	class EmptyCup(beverages.HotBeverage):
		def __init__(self, name = "empty cup", price = 0.30, descr = "AAn empty cup?! Gimme my money back!"):
			super().__init__(name, price, descr)
	class BrokenMachineException(Exception):
		def __init__(self, *args: object) -> None:
			super().__init__("\033[0;31mThis coffee machine has to be repaired.\033[0m")

	def repair(self):
		self.used = 0
		
	def serve(self, drink):
		if self.used == 10:
			raise self.BrokenMachineException()
		self.used += 1
		if (randint(0, 1000) % 7) == 0:
			return self.EmptyCup()
		else:
			return drink()

if __name__ == "__main__":
	m = CoffeeMachine()
	list = [beverages.HotBeverage, beverages.Coffe, beverages.Tea, beverages.Chocolate, beverages.Cappuccino]

	for _ in range(22):
		num = randint(0, 3)
		try:
			print("\033[0;32mYou got:\033[0m\n{}".format(m.serve(list[num])))
		except m.BrokenMachineException as ex:
			print(ex)
			m.repair()
			print("\033[0;32mThe machine has been repaired.\033[0m")
