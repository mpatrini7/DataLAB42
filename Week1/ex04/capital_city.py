# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    capitals.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mpatrini <mpatrini@student.42roma.it>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/05/16 18:08:25 by mpatrini          #+#    #+#              #
#    Updated: 2022/05/16 18:29:08 by mpatrini         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

states = {
"Oregon" : "OR",
"Alabama" : "AL",
"New Jersey": "NJ",
"Colorado" : "CO"
}
capital_cities = {
"OR": "Salem",
"AL": "Montgomery",
"NJ": "Trenton",
"CO": "Denver"
}

if len(sys.argv) == 2:
	if sys.argv[1] in states.keys():
		for x in states:
			if (x == sys.argv[1]):
				for y in capital_cities:
					if (y == states[x]):
						print(capital_cities[y])
	else:
		print("Unknown state")
			