from Visualization_k_means import *
import numpy as np

#чё-то не робит, потом надо будет разобраться

##### загрузка из txt-файла в массив numpy (путь к файлу «свой»)
elements = np.loadtxt('/Test1.txt').astype(np.int32)


#####################

def k_means(data, k, max_iterations=100):
    # выбор случайных центров кластеров

    ##### elems - массив индексов; centers - массив центров по индексам elems
    elems = np.random.choice(range(len(data)), size=k, replace=False).reshape(-1, 1)
    centers = np.take_along_axis(data, elems, axis=0)
    ################

    for i in range(max_iterations):
        # вычисление расстояний от каждого объекта до каждого центра кластера

        ##### для верного определения построчной разности двух массивов
        ##### необходимо к уменьшаемому добавить новую ось в начало, вычитаемому - в конец
        distances = np.sqrt(np.abs(((data[np.newaxis, :] - centers[:, np.newaxis]) ** 2).sum(axis=2)))
        ##################

        # определение ближайшего центра кластера для каждого объекта
        labels = np.argmin(distances, axis=0)
        # вычисление новых центров кластеров
        #labels = np.array(list(filter(None, labels)))
        new_centers = np.array([data[labels == j].mean(axis=0) for j in range(k)])
        # проверка на сходимость
        if np.all(centers == new_centers):
            break
        centers = new_centers
    return labels


labels = k_means(elements, 15)
print(labels)
visualisation_2d(labels)

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