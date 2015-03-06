from math import sqrt

def fill_tetrahedron(num = raw_input("Enter the length of the tetrahedron: ")):
	volume = (sqrt(2) * ((0.1 * int(num)) ** 3))/12
	print volume
	return volume

fill_tetrahedron()