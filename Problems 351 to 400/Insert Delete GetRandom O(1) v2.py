import random

class RandomizedSet:
    def __init__(self):
        # Maps value to its index in the list
        self.value_to_index = {}
        # Stores the elements of the set
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.value_to_index:
            return False
        
        self.value_to_index[val] = len(self.values)
        self.values.append(val)
        return True
        
    def remove(self, val: int) -> bool:
        if val not in self.value_to_index:
            return False

        # Swap the element with the last one and pop it
        last_element = self.values[-1]
        index_to_remove = self.value_to_index[val]
        self.values[index_to_remove], self.values[-1] = self.values[-1], self.values[index_to_remove]
        self.values.pop()
        self.value_to_index[last_element] = index_to_remove
        del self.value_to_index[val]
        return True

    def getRandom(self) -> int:
        if not self.values:
            raise Exception("RandomizedSet is empty")
        return random.choice(self.values)

# Example usage
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
