# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    intern.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mpatrini <mpatrini@student.42roma.it>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/05/16 22:18:08 by mpatrini          #+#    #+#              #
#    Updated: 2022/05/16 22:44:24 by mpatrini         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Intern:
	def __init__(self, name):
		if name == "":
			self.name = "My name? I’m nobody, an intern, I have no name."
		else:
			self.name = name

	def __str__(self):
		return self.name

	class Coffe:
		def __str__(self):
			return "This is the worst coffee you ever tasted."
	def work(self):
		raise Exception("I’m just an intern, I can’t do that...")
	def	make_coffee(self):
		return self.Coffe()

a = Intern("")
print(a)
b = Intern("Mark")
print(b)

print(b.make_coffee())

a.work()


		