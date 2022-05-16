# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    var.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mpatrini <mpatrini@student.42roma.it>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/05/16 15:40:45 by mpatrini          #+#    #+#              #
#    Updated: 2022/05/16 21:18:34 by mpatrini         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from concurrent.futures.process import _global_shutdown


def my_var():
	a = 42
	b = "42"
	c = "quarante-deux"
	d = 4.0
	e = True
	f = [42]
	g = {42: 42}
	h = (42, )
	i = set()
	
	print("%i has a type %s" % (a, type(a)))
	print(str(b) + " has a type " + str(type(b)))
	print(c, " has a type ", type(c))
	print(str(d) + " has a type " + str(type(d)))
	print(str(e) + " has a type " + str(type(e)))
	print(str(f) + " has a type " + str(type(f)))
	print(str(g) + " has a type " + str(type(g)))
	print(str(h) + " has a type " + str(type(h)))
	print(str(i) + " has a type " + str(type(i)))
	
my_var()