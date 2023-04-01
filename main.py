from Visualization_k_means import *

if __name__ == '__main__':
    k = 5   #Количество кластеров
    max_center_value = 1000000

    labels = k__means(getmatrix('/test1.txt'), k, max_center_value)
    #print(labels)
    visualisation_2d(labels)