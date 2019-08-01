from numpy import array, column_stack, any, where, delete, append
from faiss import IndexFlatL2
from .approximate import approximate
from .entry import Entry, Entries


def clustering(point_cloud, f, delta, tau):
    index = IndexFlatL2(len(point_cloud[0]))
    point_cloud = point_cloud.astype('float32')
    index.add(point_cloud)

    lims, _, I = index.range_search(point_cloud, delta)

    entries = Entries()

    for i in range(len(f)):
        neighbor_idxs = I[lims[i]:lims[i+1]]
        upper_star = neighbor_idxs[neighbor_idxs < i]
        if len(upper_star) > 0:
            entry_index = entries.find_entry_index_by_point(min(upper_star))
            entries.attach(entry_index, i)
            entries = merge(f, entries, i, upper_star, tau)
        else:
            entries.create(Entry(i))

    return entries


def merge(f, entries, i, upper_star, tau):
    for j in upper_star:
        main_entry_idx = entries.find_entry_index_by_point(i)
        entry_idx = entries.find_entry_index_by_point(j)
        entry = entries.entries[entry_idx]
        root = entry.root_index()
        if entry_idx != main_entry_idx and f[root] - f[i] < tau:
            entries.merge(entry_idx, main_entry_idx)

    main_entry_idx = entries.find_entry_index_by_point(i)
    highest_entry_idx = None
    for j in upper_star:
        entry_idx = entries.find_entry_index_by_point(j)
        root = entries.entries[entry_idx].root_index()
        if (highest_entry_idx is None) or f[entries.entries[highest_entry_idx].root_index()] < f[root]:
            highest_entry_idx = entry_idx

    if main_entry_idx != highest_entry_idx and f[entries.entries[highest_entry_idx].root_index()] - f[i] < tau:
        entries.merge(main_entry_idx, highest_entry_idx)

    return entries


def find_entry_index(entries, i):
    return where(any(entries == i, axis=1))[0][0]
