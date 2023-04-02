from myversionof_k_means import *
import matplotlib.pyplot as plt

def WCSS(data, mink, maxk, max_iterations):
    sum_sq_len_allcenters_arr = []

    for i in range(mink, maxk + 1):
        labels = my_k_means.m_k_means(my_k_means.getmatrix('./Test1.txt'), i, max_iterations)
        centers = my_k_means.create_clever_centers(data, i)

        privious_center = copy.deepcopy(centers)
        count = 0

        while count < max_iterations:
            centers = k_means.center_update(centers, labels, len(data[0]))
            labels = k_means.data_clusterization(data, centers, i)
            if centers == privious_center:
                # label = list(filter(None, label))
                # print(center)
                break
            privious_center = copy.deepcopy(centers)
            count += 1

        sum_sq_len = 0
        for j in range(i):
            all_distance = 0
            for m in range(len(labels[j])):
                distance = 0
                distance += np.linalg.norm(np.array(centers[j]) - np.array(labels[j][m]))
                all_distance += distance ** 2
            sum_sq_len += all_distance
        sum_sq_len_allcenters_arr.append(sum_sq_len)

    plt.grid()
    plt.xlabel("number of clusters")
    plt.ylabel("sum of squared distances")

    x_coordinates = np.arange(mink, maxk + 1)
    plt.plot(x_coordinates, sum_sq_len_allcenters_arr)

    plt.show()
