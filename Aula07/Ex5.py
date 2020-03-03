import math
def floatInput(prompt, mini, maxi):
	try:
		num = float(input(prompt))
		if not(mini<=num and num<=maxi):
			raise Exception(num)
	except ValueError:
		print("Not a float!")
		floatInput(prompt, mini, maxi)
	except Exception:
		print("Value should be in: [",mini,",",maxi,"]")
		floatInput(prompt, mini, maxi)
	else:
		print(num)

mini = input("minimo? ")
if mini == "":
	mini = -math.inf
maxi = input("maximo? ")
if maxi == "":
	maxi = math.inf



floatInput("val? ", float(mini), float(maxi))
