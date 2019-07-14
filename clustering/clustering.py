from numpy import array, column_stack, any, where, delete, append
from faiss import IndexFlatL2
from .approximate import approximate
from .entry import Entry, Entries


def clustering(point_cloud, delta, tau):
    f = approximate(point_cloud, 0.1)

    # f の値が大きい順に point_cloud と f をソート
    z = column_stack((point_cloud, f))
    z = array(sorted(z, key=lambda x: x[-1], reverse=True))
    point_cloud = z[:, :-1]
    f = z[:, -1]

    index = IndexFlatL2(len(point_cloud[0]))
    index.add(point_cloud)

    lims, _, I = index.range_search(point_cloud, delta)

    entries = Entries()

    for i in range(len(f)):
        neighbor_indices = I[lims[i]:lims[i+1]]
        upper_star = neighbor_indices[neighbor_indices < i]
        if upper_star:
            entry_index = entries.find_entry_index_by_point(min(upper_star))
            entries.attach(entry_index, i)
        else:
            entries.create(Entry(i))

    return entries


def merge(f, entries, i, upper_star, tau):
    main_entry_index = entries.find_entry_index_by_point(i)
    for j in upper_star:
        index = entries.find_entry_index_by_point(j)
        entry = entries.entries[index]
        root = entry.root_index()
        if f[root] - f[i] < tau:
            entries.merge(index, main_entry_index)

    highest_entry_index = None
    for j in upper_star:
        index = entries.find_entry_index_by_point(j)
        root = entries.entries[index].root_index()
        if (highest_entry_index is None) or f[highest_entry_index] < f[root]:
            highest_entry_index = j

    if i != highest_entry_index and f[entries.entries[main_entry_index].root_index()] - f[i] < tau:
        entries.merge(main_entry_index, highest_entry_index)

    return entries


def find_entry_index(entries, i):
    return where(any(entries == i, axis=1))[0][0]
