class Difference:
    maximumDifference = 0

    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    def computeDifference(self):
        global maximumDifference
        self.maximumDifference = abs(max(self.__elements)-min(self.__elements))


# End of Difference class

a = [8, 19, 3, 2, 7]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)