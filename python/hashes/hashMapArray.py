# this is an array or list implementation of a hash map

class HashMapArray:
    def __init__(self, size:int):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def hash_function(self, key):
        numeric_sum = sum(int(char) for char in key if char.isdigit())
        return numeric_sum % 100
    
    def put(self, key, value):
        index = self.hash_function(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value) # update key
                return
        bucket.append((key, value)) # add a new key, value pair

    def remove(self, key):
       index = self.hash_function(key)
       bucket = self.buckets[index]
       for i, (k, v) in enumerate(bucket):
           if k == key:
               del bucket[i]  # Remove the key value pair
               return
        
    def print_map(self):
        # print all the elements in the hash
        print("Hash Map Contents")
        for index, bucket in enumerate(self.buckets):
            print(f"Bucket {index}: {bucket}")


hash_map = HashMapArray(100)

hash_map.put("123-4567", "charlotte")
hash_map.put("123-4678", "Nicole")
hash_map.put("123-4569", "brandon")
hash_map.put("123-4560", "charlotte")
hash_map.put("123-4561", "excel")
hash_map.put("123-4562", "melon")
hash_map.put("123-4563", "lisa")
hash_map.put("123-4564", "adele")
hash_map.put("123-4565", "charlotte")
hash_map.put("123-4566", "charlotte")

hash_map.print_map()

hash_map.remove("123-4560")
hash_map.remove("123-4561")
hash_map.remove("123-4562")
hash_map.remove("123-4563")
hash_map.remove("123-4564")
hash_map.remove("123-4565")

hash_map.print_map()









