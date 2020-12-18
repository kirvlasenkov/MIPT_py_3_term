from scripts.ex_8 import compress_string


def test_compress():
    assert compress_string('1222311') == [(1, 1), (3, 2), (1, 3), (2, 1)]
    assert compress_string('001234') == [(2, 0), (1, 1), (1, 2), (1, 3), (1, 4)]
    assert compress_string('') == []
