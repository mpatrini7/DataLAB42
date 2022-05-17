# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    intern.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mpatrini <mpatrini@student.42roma.it>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/05/16 22:18:08 by mpatrini          #+#    #+#              #
#    Updated: 2022/05/17 23:36:15 by mpatrini         ###   ########.fr        #
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
		raise Exception("I’m just an intern, I can’t do that...")
	def	make_coffee(self):
		return self.Coffe()

a = Intern()
print("No name Intern class:\n", a, "\n")
b = Intern("Mark")
print("Mark named Intern class:\n", b, "\n")

print("Intern Class 'Mark' making coffe\n", b.make_coffee(), "\n")

print("No name Intern Class work Exception\n")
a.work()


		