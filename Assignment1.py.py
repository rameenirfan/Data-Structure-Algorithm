class SharpSearch:
    def __init__(self, data):
        self.data = data

    def Class_member(self):
        l = self.data
        return l

    def SearchFirst(self, n):
        for i in range(len(self.data)):
            if self.data[i] == n:
                return i
        return -1

    def SearchLast(self, n):
        for i in reversed(range(len(self.data))):
            if self.data[i] == n:
                return i
        return -1

    def SearchAll(self, n):

        t_lst = []
        for i in range(len(self.data)):
            if self.data[i] == n:
                t_lst.append(i)
        return t_lst


s = SharpSearch([5, 4, 7, 1, 4, 9])
a = s.Class_member()
print("list: ", a)
print("Element from first : ", s.SearchFirst(4))
print("Element from last : ", s.SearchLast(4))
print("Element from last: ", s.SearchLast(5))
print("Element from last : ", s.SearchLast(15))
print("Search from all : ", s.SearchAll(4))
