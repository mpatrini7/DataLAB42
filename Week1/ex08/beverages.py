# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    beverages.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mpatrini <mpatrini@student.42roma.it>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/05/16 22:48:54 by mpatrini          #+#    #+#              #
#    Updated: 2022/05/23 06:38:52 by mpatrini         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class HotBeverage:
	def __init__(self, name = "hot beverage", price = 0.30, descr = "Just some hot water in a cup"):
		self.name = name
		self.price = price
		self.descr = descr
	def description(self):
		return self.descr
	def __str__(self):
		return "name : {}\nprice : {:.2f}\ndescription : {}\n".format(self.name, self.price, self.description())

class Coffe(HotBeverage):
	def __init__(self, name = "coffee", price =0.40, descr = "A coffee, to stay awake."):
		super().__init__(name, price, descr)

class Tea(HotBeverage):
	def __init__(self, name = "tea", price =0.30):
		super().__init__(name, price)

class Chocolate(HotBeverage):
	def __init__(self, name = "chocolate", price =0.50, descr = "Chocolate, sweet chocolate..."):
		super().__init__(name, price, descr)

class Cappuccino(HotBeverage):
	def __init__(self, name = "cappuccino", price =0.45, descr = "Un po' di Italia nella sua tazza!"):
		super().__init__(name, price, descr)

if __name__ == "__main__":
	print(HotBeverage())
	print(Coffe())
	print(Tea())
	print(Chocolate())
	print(Cappuccino())