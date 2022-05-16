# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    print_secs.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mpatrini <mpatrini@student.42roma.it>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/05/16 15:39:42 by mpatrini          #+#    #+#              #
#    Updated: 2022/05/16 15:39:44 by mpatrini         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if len(sys.argv) == 4:
	if sys.argv[1].isnumeric() and sys.argv[2].isnumeric() and sys.argv[3].isnumeric():
		print((int(sys.argv[1]) * 3600) + (int(sys.argv[2]) * 60)  + int(sys.argv[3]))
	else:
		print("Numbers only!")
else:
	print("Wrong number of arguments!")
