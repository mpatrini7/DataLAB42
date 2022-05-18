# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    print_sum.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mpatrini <mpatrini@student.42roma.it>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/05/16 15:39:49 by mpatrini          #+#    #+#              #
#    Updated: 2022/05/18 03:59:59 by mpatrini         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if len(sys.argv) == 3:
	try:
		a = float(sys.argv[1])
		b = float(sys.argv[2])
		c = a + b
		if c.is_integer():
			print(int(c))
		else:
			print("{:.2f}".format(a + b))		
	except ValueError:
		if sys.argv[1].isnumeric() and sys.argv[2].isnumeric():
			print(int(sys.argv[1]) + int(sys.argv[2]))
		else:
			print("Numbers only!")
else:
	print("Wrong number of arguments! Use 'num + num' or 'float + float' 🤯")
