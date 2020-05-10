from Stack.StackUsingArrays import Stack1


class Towers:
    newStack = []
    obj = Stack1()
    obj.push(12)
    obj.push(100)
    obj.push(40)
    obj.push(60)
    obj.push(120)
    obj.push(90)

    def __init__(self):
        self.count = 0

    def towerSignal(self):
        self.newStack.append(1)
        for i in range(1, self.obj.tos+1):
            self.count = 1
            j = i - 1
            while j >= 0:
                if self.obj.stack[i] <= self.obj.stack[j]:
                    break
                else:
                    self.count += 1
                j -= 1
            self.newStack.append(self.count)
        return


t = Towers()
t.towerSignal()
print(t.newStack)