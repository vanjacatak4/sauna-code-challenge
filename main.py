import json

from path_finder import PathFinder
import exceptions


def main():

    f = open('test_maps.json')
    data = json.load(f)['valid_maps']

    for item in data:
        print("########### MAP ###########")
        for row in item['map']:
            print(row)
        print("###########################")
        try:
            pathfinder = PathFinder(character_matrix=item['map'])
            path, msg = pathfinder.find_path()
            print(f"Path: {path}")
            print(f"MSG: {msg}")
            print("-----------------------")
        except exceptions.PathFinderException as pathFinderException:
            print(pathFinderException)
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
