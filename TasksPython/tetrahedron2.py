from math import sqrt

def fill_tetrahedron(num):
	volume = (sqrt(2) * ((0.1 * int(num)) ** 3))/12
	return volume

def tetrahedron_filled(tetrahedrons,water):
	tetrahedrons = sorted(tetrahedrons)
	count = 0
	while water > 0:
		water -= fill_tetrahedron(tetrahedrons[count])
		count += 1
	print count - 1
	return count - 1

tetrahedron_filled([100,20,30],10)