# https://leetcode.com/problems/implement-stack-using-queues

# Runtime: 39 ms, faster than 56.04% of Python3 online submissions for Implement Stack using Queues.
# Average performance, the Python deque() is likely a good choice, but the pop method could use shortcuts.

# Memory Usage: 13.9 MB, less than 76.44% of Python3 online submissions for Implement Stack using Queues.
# Good memory usage, no defining of unnecessary variables, some methods use existing methods for calling.


class MyStack:
    # thanks to: https://youtu.be/rW4vm0-DLYc
    
    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        for _ in range(len(self.queue)-1):
            self.push(self.queue.popleft())
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return not self.queue


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
