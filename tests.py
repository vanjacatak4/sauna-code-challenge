import unittest
import exceptions
import json
from path_finder import PathFinder


class TestPathFinder(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        with open('test_maps.json', 'r') as f:
            cls.maps = json.load(f)

    def test_initialize_map(self):
        for matrix in self.maps['valid_maps']:
            self.finder = PathFinder(character_matrix=matrix['map'])
            self.assertEqual(self.finder._character_matrix, matrix['map'])
            self.assertIsNotNone(self.finder._starting_position)

    def test_initialize_exceptions(self):
        for typeof_map, data in self.maps.items():
            with self.subTest():
                error = None

                if typeof_map == 'multiple_start_character_maps':
                    error = exceptions.MultipleStartingCharacterException

                if typeof_map == 'missing_start_character_maps':
                    error = exceptions.MissingStartingCharacterException

                elif typeof_map == 'missing_end_character_maps':
                    error = exceptions.MissingEndingCharacterException

                elif typeof_map == 'invalid_character_maps':
                    error = exceptions.InvalidCharacterException

                if error:
                    for matrix in data:
                        with self.assertRaises(error):
                            self.finder = PathFinder(matrix['map'])

    def test_find_path(self):
        for matrix in self.maps['valid_maps']:
            self.finder = PathFinder(character_matrix=matrix['map'])
            path, msg = self.finder.find_path()
            self.assertEqual(path, matrix['path'])
            self.assertEqual(msg, matrix['msg'])

    def test_find_path_exceptions(self):
        for typeof_map, data in self.maps.items():
            with self.subTest():
                error = None

                if typeof_map == 'broken_path_maps':
                    error = exceptions.BrokenPathException

                elif typeof_map == 'fork_in_path_maps':
                    error = exceptions.ForkInPathException

                elif typeof_map == 'fake_turn_maps':
                    error = exceptions.FakeTurnException

                if error:
                    for matrix in data:
                        with self.assertRaises(error):
                            self.finder = PathFinder(matrix['map'])
                            self.finder.find_path()


if __name__ == '__main__':
    unittest.main()
