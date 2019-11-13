def promedio(_param1, _param2, _param3):
	print("Valor1: " + str(_param1))
	print("Valor1: " + str(_param2))
	print("Valor1: " + str(_param3))
	if _param1 > 100 or _param1 < 0:
		print("1ro fuera de rango")
	elif _param2 > 100 or _param1 < 0:
		print("2ro fuera de rango")
	elif _param3 > 100 or _param1 < 0:
		print("3ro fuera de rango")
	else:
		return (_param1+_param2+_param3)/3
print("Promedio de los 3 valores: " + str(promedio(10,10,10)))