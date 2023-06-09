import matplotlib.pyplot as plt

def visualisation_2d(label):
	plt.grid()
	plt.xlabel("x")
	plt.ylabel("y")

	for i in range(len(label)):
		x_coordinates = []
		y_coordinates = []
		for q in range(len(label[i])):
			x_coordinates.append(label[i][q][0])
			y_coordinates.append(label[i][q][1])
		plt.scatter(x_coordinates, y_coordinates)
	plt.show()


def visualisation_3d(label):
	ax = plt.axes(projection="3d")
	plt.xlabel("x")
	plt.ylabel("y")

	k = len(label)

	for i in range(k):
		x_coordinates = []
		y_coordinates = []
		z_coordinates = []
		for q in range(len(label[i])):
			x_coordinates.append(label[i][q][0])
			y_coordinates.append(label[i][q][1])
			z_coordinates.append(label[i][q][2])
		ax.scatter(x_coordinates, y_coordinates, z_coordinates)
	plt.show()
