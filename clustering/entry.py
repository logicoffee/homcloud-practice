from numpy import array, append, empty, delete


class Entry:
    def __init__(self, point_index):
        self.point_indices = array([point_index])

    def has(self, point_index):
        return any(self.point_indices == point_index)

    def attach(self, point_index):
        self.point_indices = append(self.point_indices, point_index)
        return self

    def merge(self, entry):
        self.point_indices = append(self.point_indices, entry.point_indices)
        return self

    def root_index(self):
        return self.point_indices[0]


class Entries:
    def __init__(self):
        self.entries = empty(0, dtype=Entry)

    def find_entry_index_by_point(self, point_index):
        for index, entry in enumerate(self.entries):
            if entry.has(point_index):
                return index

    def create(self, entry):
        self.entries = append(self.entries, entry)

    def delete_entry(self, index):
        self.entries = delete(self.entries, index)

    def attach(self, index, point_index):
        entry = self.entries[index]
        self.entries[index] = entry.attach(point_index)

    def merge(self, from_index, to_index):
        from_entry = self.entries[from_index]
        to_entry = self.entries[to_index]
        self.entries[to_index] = to_entry.merge(from_entry)
        self.delete_entry(from_index)
