from k_means import *

class my_k_means(k_means):
    @staticmethod
    def create_clever_centers(data, k):
        dim = len(data[0])

        center = [[0 for i in range(dim)]]
        label = [[] for i in range(k)]

# Неслучайный выбор центров
# Первый центр я попробовал 1)выбрать случайно,2)взять среднее по всем точкам,3)взять случайную точку за 1 центр
# Потом выбираем самую далёкую точку - это вторая центроида
# Затем откаждой точки строимся к каждой существующей центроиде и выбираем минимальное расстояние
# из полученных минимумов выбираем максимум -> новая центроида

        # center[0] = data[random.randint(0, len(data))]

        # center[0] = data[random.randint(0, 1000000)]

        # for i in range(dim):
        #    center[0][i] = random.randint(0, 1000000)

        for i in range(dim):
            sum = 0
            for j in range(len(data)):
                sum += data[j][i] / len(data)
                center[0][i] = sum

        for i in range(1, k):
            max_distance = -1
            new_center = 0
            for i in range(len(data)):
                min_distance = float('inf')
                for j in range(len(center)):
                    sq_distance = 0
                    for m in range(dim):
                        sq_distance += (center[j][m] - data[i][m]) ** 2
                    distance = sq_distance ** 1/2
                    if distance < min_distance:
                        min_distance = distance
                if min_distance > max_distance:
                    max_distance = min_distance
                    new_center = data[i]
            center.append(new_center)

        # print(center)
        return center

    @staticmethod
    def m_k_means(data, k, max_iterations):
        dim = len(data[0])

        center = my_k_means.create_clever_centers(data, k)
        # print(center)
        label = [[] for i in range(k)]

        label = my_k_means.data_clusterization(data, center, k)

        privious_center = copy.deepcopy(center)

        count = 0
        while count < max_iterations:
            center = my_k_means.center_update(center, label, dim)
            label = my_k_means.data_clusterization(data, center, k)
            # print(center)
            if center == privious_center:
                # label = list(filter(None, label))
                # print(center)
                break
            privious_center = copy.deepcopy(center)
            count += 1
        # print(list(filter(None, label)))
        # print(label)
        return label

