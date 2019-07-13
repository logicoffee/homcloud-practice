from approximate import approximate
from matplotlib.pyplot import plot, show
from numpy import random, array, reshape

x = random.randn(10000).astype('float32')
x = reshape(x, (len(x), 1))
y = approximate(x, 0.1)
plot(x, y, 'k.')

show()
