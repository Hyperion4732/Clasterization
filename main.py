from Visualization_k_means import *
from WCSS import *

if __name__ == '__main__':
    k = 15  # Количество кластеров
    max_center_value = 1000000
    max_iterations = 100 # чтобы посчитать WCSS лучше ~ 10 поставить
    mink = 5
    maxk = 20

    # Обычный k-means:
    # labels = k_means.k__means(k_means.getmatrix('/test1.txt'), k, max_center_value, max_iterations)
    # print(labels)
    # visualisation_2d(labels)

    # Улучшенный мной k-means:
    labels = my_k_means.m_k_means(my_k_means.getmatrix('./Test1.txt'), k, max_iterations)
    visualisation_2d(labels) # в зависимости от данных можно заменить на 3d
    # при k = 15, например, некоторые цвета повторяются. ЭТО НЕ ОДИН КЛАСТЕР!!! Просто у питона цветов не хватило)

    # WCSS(my_k_means.getmatrix('./Test1.txt'), mink, maxk, max_iterations)