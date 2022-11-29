# https://leetcode.com/problems/insert-delete-getrandom-o1

# Runtime: 397 ms, faster than 97.89% of Python3 online submissions for Insert Delete GetRandom O(1).
# Near perfect runtime, a fairly naive implementation which just uses hashmaps anyways, albeit fast.

# Memory Usage: 61.5 MB, less than 22.58% of Python3 online submissions for Insert Delete GetRandom O(1).
# Very poor memory usage, which is sacrified in favour of much better speeds, better implementations possible.


class RandomizedSet:

    def __init__(self):
        self.to_index = dict()
        self.to_list = []

    def insert(self, val: int) -> bool:
        if val in self.to_index:
            return False
        
        self.to_index[val] = len(self.to_list)
        self.to_list.append(val)
        return True
        
    def remove(self, val: int) -> bool:
        if val not in self.to_index:
            return False

        last_val = self.to_list[-1]
        val_i = self.to_index[val]
        if last_val != val:
            self.to_index[last_val] = val_i
            self.to_list[val_i] = last_val

        self.to_list.pop()
        self.to_index.pop(val)
        return True

    def getRandom(self) -> int:
        return random.choice(self.to_list)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
