# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    intern.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mpatrini <mpatrini@student.42roma.it>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/05/16 22:18:08 by mpatrini          #+#    #+#              #
#    Updated: 2022/05/18 04:48:51 by mpatrini         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Intern:
	def __init__(self, name = "My name? I’m nobody, an intern, I have no name."):
			self.name = name

	def __str__(self):
		return self.name

	class Coffe:
		def __str__(self):
			return "This is the worst coffee you ever tasted."

	def work(self):
		raise Exception("\033[0;31mI’m just an intern, I can’t do that...\033[0m")
	def	make_coffee(self):
		return self.Coffe()

a = Intern()
print("No named Intern class:\n{}\n".format(a))
b = Intern("Mark")
print("Mark named Intern class:\n{}\n".format(b))

print("Intern Class 'Mark' making coffe\n{}\n".format(b.make_coffee()))

print("No name Intern Class work Exception")
try:
	a.work()
except Exception as ex:
	print(ex)