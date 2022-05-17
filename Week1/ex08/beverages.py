# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    beverages.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mpatrini <mpatrini@student.42roma.it>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/05/16 22:48:54 by mpatrini          #+#    #+#              #
#    Updated: 2022/05/17 19:18:54 by mpatrini         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class HotBeverage:
	def __init__(self, name, price, descr = "Just some hot water in a cup"):
		self.name = name
		self.price = price
		self.descr = descr
	def description(self, desc):
		if desc != "":
			self.descr = desc
		return self.descr
	def __str__(self):
		return "name : {}\nprice : {}\ndescription : {}\n".format(self.name, self.price, self.descr)

a = HotBeverage("coffe", 0.40)
a.description("A coffee, to stay awake.")
print(a)
b = HotBeverage("tea", 0.30)
print(b)
c = HotBeverage("chocolate", 0.50)
c.description("Chocolate, sweet chocolate...")
print(c)
d = HotBeverage("cappuccino", 0.45)
d.description("Un po' di Italia nella sua tazza!")
print(d)