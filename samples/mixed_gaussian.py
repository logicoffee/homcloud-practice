from numpy import random, array, append, c_
from homcloud.interface import PDList
from matplotlib.pyplot import savefig, scatter


def sample_from_mixed_gauss(n):
    m1 = 0.0
    m2 = 4.0
    ratio = 1 / 3
    arr = []

    for _ in range(n):
        if random.rand() >= ratio:
            a = random.normal(m1)
            arr.append([a, a])
            # append(arr, array([random.normal(m1), 0]))
        else:
            a = random.normal(m2)
            arr.append([a, a])
            # append(arr, array([random.normal(m2), 0]))
    return array(arr)


data = sample_from_mixed_gauss(30)
# scatter(data.T[0], array([0]*30))
# savefig('scatter.png')
pdlist = PDList.from_alpha_filtration(data)
pdlist.dth_diagram(0).histogram().plot()
savefig('mixed_gaussian.png')
