from numpy import random, c_
from homcloud.interface import PDList
from matplotlib.pyplot import savefig

data = c_[
    random.rand(100),
    random.rand(100)
]

pdlist = PDList.from_alpha_filtration(data)
pdlist.dth_diagram(0).histogram().plot()
savefig('uniform-pd-0.png')
