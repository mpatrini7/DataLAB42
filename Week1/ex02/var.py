# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    var.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mpatrini <mpatrini@student.42roma.it>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/05/16 15:40:45 by mpatrini          #+#    #+#              #
#    Updated: 2022/05/18 04:51:53 by mpatrini         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

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
	
	print("{} has a type {}".format( a, type(a)))
	print("{} has a type {}".format( b, type(b)))
	print("{} has a type {}".format( c, type(c)))
	print("{} has a type {}".format( d, type(d)))
	print("{} has a type {}".format( e, type(e)))
	print("{} has a type {}".format( f, type(f)))
	print("{} has a type {}".format( g, type(g)))
	print("{} has a type {}".format( h, type(h)))
	print("{} has a type {}".format( i, type(i)))

	
my_var()