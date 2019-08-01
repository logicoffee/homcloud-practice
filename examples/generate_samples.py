from numpy import random, empty, append, column_stack, array
from clustering.clustering import clustering
from clustering.approximate import approximate
from matplotlib.pyplot import scatter, show


def cluster():
    if random.rand() > 1/3:
        return 0
    return 1


def mixed_2_normal(n):
    samples = empty((0, 2), dtype='float32')
    for _ in range(n):
        if cluster() == 0:
            sample = random.multivariate_normal(
                [0, 0],
                [[2, 0], [0, 2]]
            )
        else:
            sample = random.multivariate_normal(
                [4, 4],
                [[1, 0], [0, 1]]
            )
        samples = append(samples, [sample], axis=0)
    return samples


samples = mixed_2_normal(100)
x = samples[:, 0]
y = samples[:, 1]

f = approximate(samples, 0.1)

# f の値が大きい順に point_cloud と f をソート
z = column_stack((samples, f))
z = array(sorted(z, key=lambda x: x[-1], reverse=True))
samples = z[:, :-1]
f = z[:, -1]

entries = clustering(samples, f, 1, 1)
print(len(entries.entries))


for entry in entries.entries:
    points = samples[entry.point_indices]
    x = points[:, 0]
    y = points[:, 1]
    scatter(x, y)

show()
