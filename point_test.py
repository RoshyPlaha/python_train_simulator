import unittest
from point import point

class Testpoint(unittest.TestCase):

    def test_with_two_paths(self):

        head = point()
        p = point(head)

        list1 = [1, 2]
        list2 = [3, 4]
        p.add_paths(list1)
        p.add_paths(list2)

        selected_list = p.switch_path()
        self.assertEqual(list2, selected_list)

        selected_list = p.switch_path()
        self.assertEqual(list1, selected_list)

    def test_with_exceed_max_paths(self):
        head = point()
        p = point(head)

        list1 = [1, 2]
        list2 = [3, 4]
        list3 = [5, 6]
        max_path = [7,8]
        p.add_paths(list1)
        p.add_paths(list2)
        p.add_paths(list3)
        self.assertEqual(p.add_paths(max_path), -1)

    def test_with_three_paths(self):
        head = point()
        p = point(head)

        list1 = [1, 2]
        list2 = [3, 4]
        list3 = [5, 6]
        p.add_paths(list1)
        p.add_paths(list2)
        p.add_paths(list3)

        selected_list = p.switch_path()
        self.assertEqual(list2, selected_list)

        selected_list = p.switch_path()
        self.assertEqual(list3, selected_list)

        selected_list = p.switch_path()
        self.assertEqual(list1, selected_list)

    def test_with_one_path(self):
        head = point()
        p = point(head)

        list1 = [1, 2]
        p.add_paths(list1)

        selected_list = p.switch_path()
        self.assertEqual(list1, selected_list)

    def test_with_no_path(self):
        head = point()
        p = point(head)

        selected_list = p.switch_path()
        self.assertEqual(None, selected_list)


if __name__ == '__main__':
    unittest.main()