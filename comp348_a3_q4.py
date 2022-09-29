class Multiset(list):

    def __init__(self, data):
        super().__init__()
        if data is not None:
            self._list = list(data)
        else:
            self._list = list()

    def get_list(self):
        return self._list

    def set_list(self, data):
        self._list = list(data)

    def __repr__(self):
        return self._list.__repr__()

    def __add__(self, other):
        self._list.append(other)
        return self._list

    def __truediv__(self, other):
        while other in self._list:
            self._list.remove(other)
        return self._list

    def m(self, other):
        return self._list.count(other)

    def union(self, other):
        new_list = self._list
        other_list = other.get_list()
        for num in other_list:
            if num is None:
                continue
            if num not in new_list:
                new_list.append(num)
            else:
                max_count = max(new_list.count(num), other_list.count(num))
                while num in new_list:
                    new_list.remove(num)
                while num in other_list:
                    other_list[other_list.index(num)] = None
                for i in range(max_count):
                    new_list.append(num)
        return Multiset(new_list)

    def intersection(self, other):
        other_list = other.get_list()
        new_list = [num for num in self._list if num in other_list]
        for num in other_list:
            if num is None:
                continue
            if num not in self._list:
                continue
            else:
                min_count = min(new_list.count(num), other_list.count(num))
                while num in new_list:
                    new_list.remove(num)
                for i in range(min_count):
                    new_list.append(num)
        return Multiset(new_list)

    def __sub__(self, other):
        other_list = other.get_list()
        for num in other_list:
            if num in self._list:
                self._list.remove(num)
        return self._list


if __name__ == '__main__':
    set1 = Multiset([1, 2, 3, 4, 5, 1, 5])
    print(set1)
    print(set1 + 1)
    print(set1 / 1)
    print(set1.m(5))
    print(set1)
    #set2 = Multiset([1, 2])
    #set3 = Multiset([2, 2, 3, 4])
    set2 = Multiset([5, 6, 7])
    set3 = Multiset([7, 7])
    set4 = set2.union(set3)
    print(set4)
    print(set3)
    set5 = Multiset([1, 1, 2, 2, 3])
    set6 = Multiset([2, 2, 2, 3, 4])
    set7 = set6.intersection(set5)
    print(set7)
    set8 = Multiset([1, 1, 2, 2, 3, 1])
    set9 = Multiset([1, 2, 2, 2])
    set10 = set8 - set9
    print(set10)
    print(set8 - set9)
    print(set8)

