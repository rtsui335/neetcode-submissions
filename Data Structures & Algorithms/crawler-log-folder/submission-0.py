class Solution:
    def minOperations(self, logs: List[str]) -> int:
        #uses a stack in O(n) time and space complexity
        stack = []
        for i in logs:
            if i == "../":
                if stack:
                    stack.pop()
            elif i != "./":
                stack.append(i)
        return len(stack)