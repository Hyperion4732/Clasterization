from myversionof_k_means import *
from Visualization_k_means import *

if __name__ == '__main__':
    k = 15  #Количество кластеров
    max_center_value = 1000000
    max_iterations =100

    #labels = k_means.k__means(k_means.getmatrix('/test1.txt'), k, max_center_value, max_iterations)
    #print(labels)
    #visualisation_2d(labels)

    labels = my_k_means.m_k_means(my_k_means.getmatrix('/test1.txt'), k, max_center_value, max_iterations)
    visualisation_2d(labels)