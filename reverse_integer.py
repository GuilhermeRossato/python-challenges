class Solution:
	def reverse(self, x: int) -> int:
		print(-2**32, 2**32-1)
		# quebra string em caracteres individuais
		charList = list(str(x))
		isNegative = False
		if (charList[0] == "-"):
			# reverte depois do negativo
			isNegative = True
			digitList = list(reversed(charList[1:]))
		else:
			# reverte a lista de caracteres
			digitList = list(reversed(charList))

		# retorna o valor concatenado se tiver menos que 10 caracteres
		if (len(digitList) < 10):
			return ("-" if isNegative else "") + "".join(digitList)

		# verifica se for maior do que a quantidade de caracteres permitida
		if (len(digitList) > 10):
			# print("O numero de caracteres foi maior que o limite (", len(digitList), ")")
			return "0"

		# converte os digito para inteiros individuais

		numberList = list(map(lambda digit: int(digit), digitList))

		# define os limites de acordo com o sinal do numero
		limits = list(map(lambda digit: int(digit), list("4294967296" if isNegative else "4294967295")))

		print(numberList)
		print(limits)

		# verifica cada par de digitos com os limites
		checks = list(map(lambda a,b: a <= b, numberList, limits))

		print(checks)

		if True in checks:
			return "0"

		return ("-" if isNegative else "") + "".join(
			str(digit) for digit in numberList
		)