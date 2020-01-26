from math import pi

def circle_area(r):
	if type(r) not in [int, float]:
		raise TypeError("Le radius doit être un réel positif non nul")
	if r < 0:
		raise ValueError("Le radius ne peut être négatif.")
	
	return pi*(r**2)

# Test Function
#radii = [2, 0, -3, 2 + 5j, True, "raduis"]
#message = "Area of circles with r = {radius} is {area}"

#for r in radii:
#	A = circle_area(r)
#	print(message.format(radius=r, area=A))