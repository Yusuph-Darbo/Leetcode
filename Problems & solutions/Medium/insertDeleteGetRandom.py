# Approach:
# Use a list to store values for O(1) random access and a hashmap to map
# each value to its index in the list. To remove an element in O(1), swap it
# with the last element, update the swapped element's index in the hashmap,
# and then remove the last element from the list.
#
# Time: O(1)
# Space: O(n)


class RandomizedSet:

    def __init__(self):
        self.numList = []
        self.numMap = {}

    def insert(self, val: int) -> bool:
        if val in self.numMap:
            return False

        self.numMap[val] = len(self.numList)
        self.numList.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self.numMap:
            return False

        index = self.numMap[val]
        lastVal = self.numList[-1]
        self.numList[index] = lastVal
        self.numMap[lastVal] = index
        self.numList.pop()
        del self.numMap[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.numList)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
