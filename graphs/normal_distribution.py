from matplotlib.pyplot import figure, subplot, bar, scatter, suptitle, show, plot
from numpy import arange, sin, pi, sqrt, exp


def norm(t):
    """正規分布の確率密度関数"""
    return sqrt(2*pi) * exp(-t*t/2)


def mixed_norm(t):
    """混合正規分布"""
    return 1/3 * norm(t+3) + 2/3 * norm(t-2)


x = arange(-6, 6, 0.1)
y = mixed_norm(x)

plot(x, y)
show()
