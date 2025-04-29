class Logger:

    def __init__(self):
        self.hashMap = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.hashMap:
            self.hashMap[message] = timestamp
            return True
        else:
            if timestamp >= self.hashMap[message] + 10:
                self.hashMap[message] = timestamp
                return True
            else:
                return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)