class HashMap:
    def __init__(self, initial_capacity=10):
        self.size = 0
        self.capacity = initial_capacity
        self.buckets = [[] for _ in range(self.capacity)]

    def _hash(self, key):
        """Hash function to map keys to bucket index."""
        return hash(key) % self.capacity

    def insert(self, key, value):
        """Insert a key-value pair into the hashmap."""
        bucket_index = self._hash(key)
        bucket = self.buckets[bucket_index]
        
        # Check if the key already exists
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Update the value
                return
        # If the key doesn't exist, append the new key-value pair
        bucket.append((key, value))
        self.size += 1
        
        # Resize if the load factor exceeds 0.75
        if self.size / self.capacity > 0.75:
            self._resize()

    def get(self, key):
        """Retrieve the value associated with the key."""
        bucket_index = self._hash(key)
        bucket = self.buckets[bucket_index]
        
        for k, v in bucket:
            if k == key:
                return v
        return None  # Key not found

    def delete(self, key):
        """Remove a key-value pair from the hashmap."""
        bucket_index = self._hash(key)
        bucket = self.buckets[bucket_index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                return
        return None  # Key not found

    def _resize(self):
        """Resize the hash map when the load factor exceeds a threshold."""
        new_capacity = self.capacity * 2
        new_buckets = [[] for _ in range(new_capacity)]
        
        for bucket in self.buckets:
            for key, value in bucket:
                new_bucket_index = hash(key) % new_capacity
                new_buckets[new_bucket_index].append((key, value))
        
        self.buckets = new_buckets
        self.capacity = new_capacity

    def __str__(self):
        """Return a string representation of the hashmap."""
        return str(self.buckets)
