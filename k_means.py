import numpy as np
import random
import copy

class k_means:
	@staticmethod
	def getmatrix(path):
		f = open(path)
		elements = []
		for line in f:
			elem = line.split()
			for i in range(len(elem)):
				elem[i] = int(elem[i])
			elements.append(elem)
		return elements
		#print(elements)

	@staticmethod
	def data_clusterization(data, center, k):
		n = len(data)
		dim = len(data[0])
		label = [[] for i in range(k)]

		for i in range(n):
			min_distance = float('inf')
			suitable_center = -1
			for j in range(k):
				distance = 0
				for q in range(dim):
					distance += (data[i][q] - center[j][q])**2
				distance = distance**(1/2)
				if distance < min_distance:
					min_distance = distance
					suitable_center = j

			label[suitable_center].append(data[i])

		return label

	@staticmethod
	def center_update(center, label, dim):
		k = len(center)
		for i in range(k): #по i кластерам
			for q in range(dim): #по q параметрам
				updated_parameter = 0
				for j in range(len(label[i])):
					updated_parameter += center[i][q] - label[i][j][q]
					if len(label[i]) != 0:
						updated_parameter = updated_parameter / len(label[i])
					center[i][q] -= updated_parameter
		return center

	@staticmethod
	def k__means (data, k, max_center_value, max_iterations):
		dim = len(data[0])

		center = [[0 for i in range(dim)] for q in range(k)]
		label = [[] for i in range(k)]

		for i in range(dim):
			for q in range(k):
				center[q][i] = random.randint(0, max_center_value)

		label = k_means.data_clusterization(data, center, k)

		privious_center = copy.deepcopy(center)

		count = 0
		while count < max_iterations:
			center = k_means.center_update(center, label, dim)
			label = k_means.data_clusterization(data, center, k)
			if center == privious_center:
				#label = list(filter(None, label))
				#print(center)
				break
			privious_center = copy.deepcopy(center)
			count += 1
		#print(list(filter(None, label)))
		#print(label)
		return label
