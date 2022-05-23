# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    capital_city.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mpatrini <mpatrini@student.42roma.it>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/05/16 18:08:25 by mpatrini          #+#    #+#              #
#    Updated: 2022/05/23 06:28:44 by mpatrini         ###   ########.fr        #
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
		if states[sys.argv[1]] in capital_cities.keys():
			print(capital_cities[states[sys.argv[1]]])
	else:
		print("Unknown state")
else:
	print("Argument Error!")
			