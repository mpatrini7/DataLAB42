# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    machine.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mpatrini <mpatrini@student.42roma.it>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/05/16 22:48:51 by mpatrini          #+#    #+#              #
#    Updated: 2022/05/18 00:13:35 by mpatrini         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import beverages
class CoffeeMachine:
	def __init__(self):

	empty_cup = beverages.HotBeverage("empty cup", 0.90, "An empty cup?! Gimme my money back!")