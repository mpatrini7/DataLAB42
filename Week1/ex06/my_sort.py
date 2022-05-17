# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    my_sort.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mpatrini <mpatrini@student.42roma.it>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/05/16 18:30:35 by mpatrini          #+#    #+#              #
#    Updated: 2022/05/17 23:33:21 by mpatrini         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

d={
'Hendrix' : '1942', 'Allman' : '1946', 'King' : '1925', 'Clapton' : '1945', 'Johnson' : '1911', 'Berry' : '1926', 'Vaughan' : '1954', 'Cooder' : '1947', 'Page' : '1944', 'Richards' : '1943', 'Hammett' : '1962', 'Cobain' : '1967', 'Garcia' : '1942', 'Beck' : '1944', 'Santana' : '1947', 'Ramone' : '1948', 'White' : '1975', 'Frusciante': '1970', 'Thompson' : '1949', 'Burton' : '1939',
}
d = dict(sorted(d.items()))
d = dict(sorted(d.items(), key=lambda item: item[1]))

for key, value in d.items():
    print(key, ' : ', value)