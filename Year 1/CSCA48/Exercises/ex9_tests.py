import unittest
import ex9_code


class HeapTest(unittest.TestCase):
    def test_heap_form_empty_heap(self):
        empty_heap = ex9_code.Heap()
        self.assertTrue(type(empty_heap) is ex9_code.Heap, "Heap __init__"
                        "does not form a object of type Heap")
        self.assertEqual(empty_heap._heap, [], "Heap does not contain"
                         "assigned value")

    def test_is_empty(self):
        empty_heap = ex9_code.Heap()
        self.assertTrue(empty_heap.is_empty(), "Empty heap not detected")

    def test_form_one_item_heap(self):
        one_item_heap = ex9_code.Heap([1])
        self.assertEqual(one_item_heap._heap, [1], "Heap does not contain"
                         "assigned value")

    def test_form_multi_item_heap_inorder(self):
        test_heap = ex9_code.Heap([1, 2, 3, 4])
        self.assertEqual(test_heap._heap, [4, 3, 2, 1], "Heap does not "
                         "contain assigned values")

    def test_form_multi_item_heap_reverse_order(self):
        test_heap = ex9_code.Heap([4, 3, 2, 1])
        self.assertEqual(test_heap._heap, [4, 3, 2, 1], "Heap does not "
                         "contain assigned values")

    def test_form_multi_item_heap_mix_order(self):
        test_heap = ex9_code.Heap([2, 3, 4, 1])
        self.assertEqual(test_heap._heap, [4, 2, 3, 1], "Heap does not"
                         " contain assigned values")

    def test_insert_into_empty_heap(self):
        test_heap = ex9_code.Heap()
        test_heap.insert(1)
        self.assertEqual(test_heap._heap, [1], "Heap does not contain"
                         "assigned value")

    def test_insert_into_nonempty_heap(self):
        test_heap = ex9_code.Heap([0])
        test_heap.insert(1)
        self.assertEqual(test_heap._heap, [1, 0], "Heap does not contain"
                         "assigned value")
        test_heap.insert(2)
        self.assertEqual(test_heap._heap, [2, 0, 1], "Heap does not contain"
                         "assigned value")
        test_heap.insert(1)
        self.assertEqual(test_heap._heap, [2, 1, 1, 0], "Heap does not contain"
                         "assigned value")

    def test_remove_from_empty(self):
        test_heap = ex9_code.Heap([])
        with self.assertRaises(ex9_code.HeapEmptyException):
            test_heap.remove_top()

    def test_remove_from_one_element_heap(self):
        test_heap = ex9_code.Heap([1])
        ret = test_heap.remove_top()
        self.assertEqual(ret, 1, "Heap did not return top value")
        self.assertEqual(test_heap._heap, [], "Heap container was not "
                         " properly not modified following extraction")

    def test_remove_from_multi_element_heap(self):
        test_heap = ex9_code.Heap([1, 2, 3])
        ret = test_heap.remove_top()
        self.assertEqual(ret, 3, "Heap did not return top value")
        self.assertEqual(test_heap._heap, [2, 1], "Heap container was not "
                         "properly modified following extraction")
        ret_1 = test_heap.remove_top()
        self.assertEqual(ret_1, 2, "Heap did not return top value")
        self.assertEqual(test_heap._heap, [1], "Heap container was not "
                         "properly modified following extraction")

    def test_bubble_down(self):
        test_heap = ex9_code.Heap([])
        test_heap._heap = [1, 2, 3]
        test_heap._bubble_down(1)
        self.assertEqual(test_heap._heap, [1, 2, 3], "Heap was not properly"
                         " bubbled down.")
        test_heap._bubble_down(0)
        self.assertEqual(test_heap._heap, [2, 1, 3], "Heap was not properly"
                         " bubbled down.")

    def test_bubble_up(self):
        test_heap = ex9_code.Heap([])
        test_heap._heap = [3, 2, 5]
        test_heap._bubble_up(1)
        self.assertEqual(test_heap._heap, [3, 2, 5], "Heap was not properly"
                         " bubbled up.")
        test_heap._bubble_up(2)
        self.assertEqual(test_heap._heap, [5, 2, 3], "Heap was not properly"
                         " bubbled up.")

    def test_violates(self):
        test_heap = ex9_code.Heap([])
        test_heap._heap = [3, 2, 5]
        self.assertFalse(test_heap._violates(1), "False positive violation")
        self.assertTrue(test_heap._violates(0), "Violation not detected.")

if __name__ == '__main__':
    unittest.main(exit=False)
