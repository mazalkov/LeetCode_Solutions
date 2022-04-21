# https://leetcode.com/problems/design-hashset

# Runtime: 172 ms, faster than 88.29% of Python3 online submissions for Design HashSet.
# Good runtime, this is a naive implementation using a list but seems to get good results.

# Memory Usage: 18.3 MB, less than 96.92% of Python3 online submissions for Design HashSet.
# Excellent memory usage, although this could be improved by not storing in a list but as hashed values.


class MyHashSet:

    def __init__(self):
        self.vals = []

    def add(self, key: int) -> None:
        if key not in self.vals:
            self.vals.append(key) 
    
    def remove(self, key: int) -> None:
        if self.contains(key):
            self.vals.remove(key)
        
    def contains(self, key: int) -> bool:
        return key in self.vals


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
