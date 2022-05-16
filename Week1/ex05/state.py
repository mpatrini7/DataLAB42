# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    value_search.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mpatrini <mpatrini@student.42roma.it>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/05/16 18:08:25 by mpatrini          #+#    #+#              #
#    Updated: 2022/05/16 18:29:18 by mpatrini         ###   ########.fr        #
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
	if sys.argv[1] in capital_cities.values():
		for x in capital_cities:
			if (capital_cities[x] == sys.argv[1]):
				for y in states:
					if (x == states[y]):
						print(y)
	else:
		print("Unknown capital city")
			