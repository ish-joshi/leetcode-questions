#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.d = []
        self.m = []
        

    def push(self, x: int) -> None:
        if len(self.m) == 0:
            self.m.append(x)
        else:
            if x < self.m[-1]:
                self.m.append(x)
        
        self.d.append(x)
        

    def pop(self) -> None:
        if len(self.d) <= 0:
            raise AssertionError("stack cannot be empty")
        pped = self.d.pop()
        if pped == self.getMin():
            self.m.pop()
        return pped

    def top(self) -> int:
        if len(self.d) <= 0:
            raise AssertionError("stack cannot be empty")
        return self.d[-1]
        

    def getMin(self) -> int:
        if len(self.m) <= 0:
            raise AssertionError("stack cannot be empty")
        return self.m[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

