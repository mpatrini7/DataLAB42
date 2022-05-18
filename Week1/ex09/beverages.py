# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    beverages.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mpatrini <mpatrini@student.42roma.it>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/05/16 22:48:54 by mpatrini          #+#    #+#              #
#    Updated: 2022/05/18 04:17:16 by mpatrini         ###   ########.fr        #
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