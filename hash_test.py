import unittest
from hypothesis import given, strategies
from hash import MonoidHashMap


class TestMonoidHashMap(unittest.TestCase):

    @given(strategies.lists(strategies.tuples(strategies.text(),
                                              strategies.integers())))
    def test_init(self, data):
        hashmap = MonoidHashMap.from_builtin_list(data)
        self.assertEqual(hashmap.size(), len(data))

    @given(strategies.lists(strategies.tuples(strategies.text(),
                                              strategies.integers())))
    def test_add_and_get(self, data):
        hashmap = MonoidHashMap()
        for key, value in data:
            hashmap.add(key, value)
        for key, value in data:
            self.assertEqual(hashmap.get(key), value)

    @given(strategies.lists(strategies.tuples(strategies.text(),
                                              strategies.integers())))
    def test_remove(self, data):
        hashmap = MonoidHashMap.from_builtin_list(data)
        for key, value in data:
            hashmap.remove(key)
            self.assertEqual(hashmap.is_member(key), False)

    @given(strategies.lists(strategies.tuples(strategies.text(),
                                              strategies.integers())))
    def test_map_by_function(self, data):
        hashmap = MonoidHashMap.from_builtin_list(data)

        def square(value):
            return value * value

        squared_map = hashmap.map_by_function(square)
        for key, value in data:
            self.assertEqual(squared_map.get(key), square(value))

    @given(strategies.lists(strategies.tuples(strategies.text(),
                                              strategies.integers())))
    def test_reduce_process_elements(self, data):
        hashmap = MonoidHashMap.from_builtin_list(data)

        def add_values(acc, value):
            return acc + value

        values = [value for _, value in data]
        result = hashmap.reduce_process_elements(add_values)
        self.assertEqual(result, sum(values))

    @given(strategies.lists(strategies.tuples(strategies.text(),
                                              strategies.integers())))
    def test_empty(self, data):
        hashmap_empty = MonoidHashMap.empty()
        self.assertEqual(hashmap_empty.size(), 0)

    @given(strategies.lists(strategies.tuples(strategies.text(),
                                              strategies.integers())),
           strategies.lists(strategies.tuples(strategies.text(),
                                              strategies.integers())))
    def test_concat(self, data1, data2):
        hashmap1 = MonoidHashMap.from_builtin_list(data1)
        hashmap2 = MonoidHashMap.from_builtin_list(data2)
        concatenated_hashmap = MonoidHashMap.concat(hashmap1, hashmap2)
        self.assertEqual(concatenated_hashmap.size(), len(data1) + len(data2))
        for key, value in data1 + data2:
            self.assertEqual(concatenated_hashmap.get(key), value)


if __name__ == '__main__':
    unittest.main()
