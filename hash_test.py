import unittest
from hash import HashMap, MonoidHashMap


class TestHashMap(unittest.TestCase):

    def test_add_and_get(self):
        hashmap = HashMap()
        hashmap.add('key1', 'value1')
        self.assertEqual(hashmap.get('key1'), 'value1')

    def test_remove(self):
        hashmap = HashMap()
        hashmap.add('key1', 'value1')
        hashmap.remove('key1')
        self.assertEqual(hashmap.get('key1'), None)

    def test_size(self):
        hashmap = HashMap()
        hashmap.add('key1', 'value1')
        hashmap.add('key2', 'value2')
        self.assertEqual(hashmap.size(), 2)

    def test_is_member(self):
        hashmap = HashMap()
        hashmap.add('key1', 'value1')
        self.assertTrue(hashmap.is_member('key1'))
        self.assertFalse(hashmap.is_member('key2'))

    def test_from_to_builtin_list(self):
        hashmap = HashMap()
        initial_list = [('key1', 'value1'), ('key2', 'value2')]
        hashmap.from_builtin_list(initial_list)
        self.assertEqual(hashmap.to_builtin_list(), initial_list)


class TestMonoidHashMap(unittest.TestCase):

    def test_empty(self):
        empty_hashmap = MonoidHashMap.empty()
        self.assertEqual(empty_hashmap.size(), 0)

    def test_concat(self):
        hashmap1 = MonoidHashMap()
        hashmap2 = MonoidHashMap()
        hashmap1.add('key1', 'value1')
        hashmap2.add('key2', 'value2')
        concated_hashmap = hashmap1.concat(hashmap2)
        self.assertTrue(concated_hashmap.is_member('key1'))
        self.assertTrue(concated_hashmap.is_member('key2'))
        self.assertEqual(concated_hashmap.size(), 2)

    def test_map_by_function(self):
        hashmap = MonoidHashMap()
        hashmap.add('key1', 1)
        hashmap.add('key2', 2)
        new_map = hashmap.map_by_function(lambda x: x * 2)
        self.assertEqual(new_map.get('key1'), 2)
        self.assertEqual(new_map.get('key2'), 4)

    def test_reduce_process_elements(self):
        hashmap = MonoidHashMap()
        hashmap.add('key1', 1)
        hashmap.add('key2', 2)
        result = hashmap.reduce_process_elements(lambda x, y: x + y)
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
