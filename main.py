def test_classify_batteries():
    present_capacities_1 = [110, 115, 118, 120]
    assert classify_batteries(present_capacities_1) == (4, 0, 0)

    present_capacities_2 = [105, 98, 75, 80, 90]
    assert classify_batteries(present_capacities_2) == (2, 2, 1)  # Corrected expected output

    present_capacities_3 = [55, 60, 58, 50]
    assert classify_batteries(present_capacities_3) == (0, 0, 4)

    present_capacities_4 = []
    assert classify_batteries(present_capacities_4) == (0, 0, 0)

    present_capacities_5 = [125, -10, 60, 121]
    try:
        classify_batteries(present_capacities_5)
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError for out-of-range present capacity")

    present_capacities_6 = [130, 135]
    assert classify_batteries(present_capacities_6) == (2, 0, 0)

test_classify_batteries()
