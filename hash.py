class HashMap:
    def __init__(self):
        self.bucket_size = 10
        self.buckets = [None] * self.bucket_size
        self.keys_order = []

    # use hashfunction to culculate key and bucket
    def _hash_function(self, key):
        return hash(key) % self.bucket_size

    # add function (If there are no special circumstances,
    # simple methods will no longer be commented)
    def add(self, key, value):
        index = self._hash_function(key)
        if self.buckets[index] is None:
            self.buckets[index] = [(key, value)]
            self.keys_order.append(key)
        else:
            for i, (existing_key, _) in enumerate(self.buckets[index]):
                if existing_key == key:
                    self.buckets[index][i] = (key, value)
                    return
            self.buckets[index].append((key, value))
            self.keys_order.append(key)

    def set_element(self, key, value):
        self.add(key, value)

    def get(self, key):
        index = self._hash_function(key)
        if self.buckets[index] is not None:
            for existing_key, value in self.buckets[index]:
                if existing_key == key:
                    return value
        return None  # 或者是其他表示“未找到”的值

    def remove(self, key):
        index = self._hash_function(key)
        if self.buckets[index] is not None:
            for i, (existing_key, _) in enumerate(self.buckets[index]):
                if existing_key == key:
                    del self.buckets[index][i]
                    return

    def size(self):
        count = 0
        for bucket in self.buckets:
            if bucket:
                count += len(bucket)
        return count

    def is_member(self, key):
        index = self._hash_function(key)
        if self.buckets[index] is not None:
            for existing_key, _ in self.buckets[index]:
                if existing_key == key:
                    return True
        return False

    # Reverse method is not applicable for a hash map.
    # def reverse(self):

    # Iterate over the passed list lst, and for each element in the list,
    # it checks if the element's length is 2,
    #  and if not, raises a ValueError.
    # It then extracts the keys and values from the elements and
    # adds them to the hash table using the add method.
    def from_builtin_list(self, lst):
        for item in lst:
            if len(item) != 2:
                raise ValueError("Each item in the list should "
                                 "be a tuple of (key, value).")
            key, value = item
            self.add(key, value)

    def to_builtin_list(self):
        result = []
        for key in self.keys_order:
            for bucket in self.buckets:
                if bucket:
                    for existing_key, value in bucket:
                        if existing_key == key:
                            result.append((existing_key, value))
        return result

    def filter_by_predicate(self, predicate):
        filtered_map = HashMap()
        for bucket in self.buckets:
            if bucket:
                for key, value in bucket:
                    if predicate(key, value):
                        filtered_map.add(key, value)
        return filtered_map

# Define a new MonoidHashMap class that inherits from the HashMap class.
# To implement the empty() and concat() methods


class MonoidHashMap(HashMap):

    @classmethod
    def empty(cls):
        return cls()

    def concat(self, other):
        for key in other.keys_order:
            value = other.get(key)
            self.add(key, value)
        return self  

    def map_by_function(self, func):
        new_map = MonoidHashMap()
        for bucket in self.buckets:
            if bucket:
                for key, value in bucket:
                    new_value = func(value)
                    new_map.add(key, new_value)
        return new_map

    def reduce_process_elements(self, func):
        result = None
        for bucket in self.buckets:
            if bucket:
                for _, value in bucket:
                    if result is None:
                        result = value
                    else:
                        result = func(result, value)
        return result
