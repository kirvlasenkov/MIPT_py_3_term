def test_min(prepared_tree_for_minimax):
    assert prepared_tree_for_minimax[0][0] == 2
    assert prepared_tree_for_minimax[0][1] == 1
    assert prepared_tree_for_minimax[0][2] == -1


def test_max(prepared_tree_for_minimax):
    assert prepared_tree_for_minimax[1][0] == 100
    assert prepared_tree_for_minimax[1][1] == 5
    assert prepared_tree_for_minimax[1][2] == 10
