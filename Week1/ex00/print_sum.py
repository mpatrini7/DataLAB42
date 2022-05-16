# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    print_sum.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mpatrini <mpatrini@student.42roma.it>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/05/16 15:39:49 by mpatrini          #+#    #+#              #
#    Updated: 2022/05/16 15:39:51 by mpatrini         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if len(sys.argv) == 3:
	if sys.argv[1].isnumeric() and sys.argv[2].isnumeric():
		print(int(sys.argv[1]) + int(sys.argv[2]))
	else:
		print("Numbers only!")
else:
	print("Wrong number of arguments!")
