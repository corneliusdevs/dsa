class SimpleHashSet:
    def __init__(self, size:int):
        """This class creates methods and varibales that manage a hash set"""
        self.size = size
        self.buckets = [[] for _ in range(size)]
    
    def hash_function(self, value:any):
        # simple hash function: sum of character codes modulo the number of buckets
        return sum(ord(char) for char in value) % self.size
    
    def add(self, value):
        # add a value if it is not present
        index = self.hash_function(value)
        bucket = self.buckets[index]
        if value not in bucket:
            bucket.append(value)
        
    def contains(self, value):
        # remove a value if present
        index = self.hash_function(value)
        bucket = self.buckets[index]
        return value in bucket
    
    def remove(self, value):
        # remove an item if present
        index = self.hash_function(value)
        bucket = self.buckets[index]
        if value in bucket:
            bucket.remove(value)

    def print_hash(self):
        for index, bucket in enumerate(self.buckets):
            print(f"Bucker: {index} {bucket}")


myHash = SimpleHashSet(100)
myHash.add("Toluene")
myHash.add("juliana")
myHash.add("augustina lopez")
myHash.add("sambizarakana juloiajd")

myHash.print_hash()
print("contains ", myHash.contains("Toluene"))
print("contains ", myHash.contains("juliana"))
print("contains ", myHash.contains("Lop"))

myHash.remove("juliana")
myHash.remove("sambizarakana juloiajd")
myHash.add("angelina jolie")

myHash.print_hash()








                
        


