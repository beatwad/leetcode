import random


class RandomizedSet:
    def __init__(self):
        self.hash_table = dict()
        self.set = list()

    def insert(self, val: int) -> bool:
        if val not in self.hash_table:
            self.set.append(val)
            self.hash_table[val] = len(self.set) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.hash_table:
            idx = self.hash_table[val]
            self.hash_table[self.set[-1]] = self.hash_table[val]
            self.set[idx], self.set[-1] = self.set[-1], self.set[idx]
            self.set.pop()
            del self.hash_table[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.set)


if __name__ == '__main__':
    # Your RandomizedSet object will be instantiated and called as such:
    val = 42
    obj = RandomizedSet()
    obj.insert(0)
    obj.insert(1)
    obj.remove(0)
    obj.insert(2)
    obj.remove(1)
    param = obj.getRandom()
    print(param)

