# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    beverages.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mpatrini <mpatrini@student.42roma.it>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/05/16 22:48:54 by mpatrini          #+#    #+#              #
#    Updated: 2022/05/18 04:10:49 by mpatrini         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class HotBeverage:
	def __init__(self, name, price, descr = "Just some hot water in a cup"):
		self.name = name
		self.price = price
		self.descr = descr
	def description(self):
		return self.descr
	def __str__(self):
		return "name : {}\nprice : {}\ndescription : {}\n".format(self.name, self.price, self.description())

a = HotBeverage("coffe", 0.40, "A coffee, to stay awake.")
print(a)
b = HotBeverage("tea", 0.30)
print(b)
c = HotBeverage("chocolate", 0.50, "Chocolate, sweet chocolate...")
print(c)
d = HotBeverage("cappuccino", 0.45, "Un po' di Italia nella sua tazza!")
print(d)