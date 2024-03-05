class Solution:
    def minimumLength(self, s: str) -> int:
        q = collections.deque(s)

        while len(q) > 1 and q[0] == q[-1]:
            prefix = q[0]

            while len(q) > 0 and q[0] == prefix:
                q.popleft()

            while len(q) > 0 and q[-1] == prefix:
                q.pop()

        return len(q)
