class MyCircularQueue:
    def __init__(self, k: int):
        self._queue = [0] * k
        self.length = k
        self.start_pos = 0
        self.num_elements = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self._queue[(self.start_pos + self.num_elements) % self.length] = value
            self.num_elements += 1
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.start_pos = (self.start_pos + 1) % self.length
            self.num_elements -= 1
            return True

    def Front(self) -> int:
        return self._queue[self.start_pos] if not self.isEmpty() else -1
        
    def Rear(self) -> int:
        return self._queue[(self.start_pos + self.num_elements - 1) % self.length]\
            if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return self.num_elements == 0

    def isFull(self) -> bool:
        return self.num_elements == self.length


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()


