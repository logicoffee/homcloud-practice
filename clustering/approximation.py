# ModuleNotFoundError: No module named '_swigfaiss'
# というエラーが出たら
# brew install libomp
from faiss import IndexFlatL2
from numpy import random, array, apply_along_axis


def count_neighbors(arr, r):
    """
    r 以下の要素がいくつあるかを数える. ただし arr は単調増加

    Parameters
    ---------
    arr : ndarray of float32
    r : float
    """
    count = 0
    for elm in arr:
        if elm > r:
            return count
        count += 1
    return count


def approximate(pc, r):
    """
    Point Cloud を生成する確率分布の密度関数を f としたとき,
    f の近似　f' に対して f'(pc) を返す

    Parameters
    ----------
    pc : ndarray of float32
        Point Cloud
    r : float

    Returns
    -------
    approximated_values : ndarray of float32
        Point Cloud の各点における近似関数の値
    """

    size = len(pc)
    index = IndexFlatL2(1)
    index.add(pc)
    D = index.search(pc, size)[0]
    return apply_along_axis(count_neighbors, 1, D, r) / (size * 2 * r)
