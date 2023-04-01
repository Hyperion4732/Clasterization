import numpy as np
import random
import copy

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
				distance += (data[i][q] - center[j][q]) ** 2

			distance = distance ** (1 / 2)
			if distance < min_distance:
				min_distance = distance
				suitable_center = j

		label[suitable_center].append(data[i])

	return label

def center_update(center, label, dim):
	k = len(center)
	for i in range(k): #по i кластерам
		for q in range(dim): #по q параметрам
			updated_parameter = 0
			for j in range(len(label[i])):
				updated_parameter += label[i][j][q]
			if len(label[i]) != 0:
				updated_parameter = updated_parameter / len(label[i])
			center[i][q] = updated_parameter
	return center

def k__means (data, k, max_center_value):
	dim = len(data[0])

	center = [[0 for i in range(dim)] for q in range(k)]
	label = [[] for i in range(k)]

	for i in range(dim):
		for q in range(k):
			center[q][i] = random.randint(0, max_center_value)

	label = data_clusterization(data, center, k)

	privious_center = copy.deepcopy(center)
	while 1:
		center = center_update(center, label, dim)
		label = data_clusterization(data, center, k)
		if center == privious_center:
			#label = list(filter(None, label))
			print(center)
			break
		privious_center = copy.deepcopy(center)
	#print(list(filter(None, label)))
	#print(label)
	return label

'''def k_means(data, k, max_iterations=100):
    # выбор случайных центров кластеров
    elems = np.random.choice(range(len(data)), size=min(k, len(data)), replace=False)
    centers = np.array(elems)[elems.astype(int)]
    for i in range(max_iterations):
        # вычисление расстояний от каждого объекта до каждого центра кластера
        distances = np.sqrt(((data - centers[:, np.newaxis])**2).sum(axis=2))
        # определение ближайшего центра кластера для каждого объекта
        labels = np.argmin(distances, axis=0)
        # вычисление новых центров кластеров
        new_centers = np.array([data[labels == j].mean(axis=0) for j in range(k)])
        # проверка на сходимость
        if np.all(centers == new_centers):
            break
        centers = new_centers
    return labels'''
