class HashLinearProbe:
    def __init__(self):
        self.hashtable_size = 10
        self.hashtable = [0] * self.hashtable_size

    def hashcode(self, key):
        return key % self.hashtable_size

    def lprobe(self, element):
        i = self.hashcode(element)
        j = 0
        while self.hashtable[(i+j) % self.hashtable_size] != 0:
            j = j + 1
        return (i + j) % self.hashtable_size

    def insert(self, element):
        i = self.hashcode(element)
        if self.hashtable[i] == 0:
            self.hashtable[i] = element
        else:
            i = self.lprobe(element)
            self.hashtable[i] = element

    def search(self, key):
        i = self.hashcode(key)
        j = 0
        while self.hashtable[(i+j) % self.hashtable_size] != key:
            if self.hashtable[(i+j) % self.hashtable_size] == 0:
                return False
            j = j + 1
        return True

    def display(self):
        print(self.hashtable)

HC = HashLinearProbe()
#HC.display()
HC.insert(54)
HC.insert(78)
HC.insert(64)
HC.insert(92)
HC.insert(34)
HC.insert(86)
HC.insert(28)
HC.display()
print(HC.search(34))