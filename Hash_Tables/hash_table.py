class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def get(self, key):
        index = self.hash(key)
        bucket = self.table[index]

        if len(bucket) > 0:
            for i in range(len(bucket)):
                k = bucket[i]["key"]

                if k == key:
                    return bucket[i]["value"]

            return None

        return None

    def insert(self, key, value):
        index = self.hash(key)
        current_value = self.get(key)

        if current_value != None:
            bucket = self.table[index]

            for i in range(len(bucket)):
                if bucket[i]["key"] == key:
                    bucket[i]["value"] = value
        else:
            self.table[index].append({ "key": key, "value": value })

    def remove(self, key):
        value = self.get(key)
        self.insert(key, None)

        return value

    def hash(self, key):
        hash = 0

        key = str(key)
        for i in range(len(key)):
            hash = (hash + ord(key[i])) % self.size

        return hash