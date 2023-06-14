from task01 import find_occurrences


def test_find_occurrences():
    example_tree = {
        "first": ["RED", "BLUE"],
        "second": {
            "simple_key": ["simple", "list", "of", "RED", "valued"],
        },
        "third": {
            "abc": "BLUE",
            "jhl": "RED",
            "complex_key": {
                "key1": "value1",
                "key2": "RED",
                "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
            }
        },
        "fourth": "RED",
        "fives": {'RED', True, 1, ('RED', False, 8)}
    }
    assert find_occurrences(example_tree, 'RED') == 8

    example_tree = {
        "first": "RED",
        "second": ["RED", "BLUE"],
        "third": {
            "simple_key": ["simple", "list", "of", "RED", "valued"],
            "complex_key": {
                "key1": "value1",
                "key2": "RED",
                "key3": ["a", "lot", "of", "values", {"nested_key": "BLUE"}],
            }
        },
        "fourth": "BLUE",
        "fives": {'BLUE', True, 1, ('RED', False, 8)}
    }
    assert find_occurrences(example_tree, 'RED') == 3
    assert find_occurrences(example_tree, 'BLUE') == 4
