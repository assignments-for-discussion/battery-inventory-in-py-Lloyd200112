def classify_batteries(present_capacities):
    healthy_count = 0
    exchange_count = 0
    failed_count = 0

    for present_capacity in present_capacities:
        rated_capacity = 120  
        soh = (present_capacity / rated_capacity) * 100

        if soh > 80:
            healthy_count += 1
        elif soh >= 62:
            exchange_count += 1
        else:
            failed_count += 1

    return healthy_count, exchange_count, failed_count

def test_classify_batteries():
    present_capacities_1 = [110, 115, 118, 120]
    assert classify_batteries(present_capacities_1) == (4, 0, 0)

    present_capacities_2 = [105, 98, 75, 80, 90]
    assert classify_batteries(present_capacities_2) == (3, 1, 1)

    present_capacities_3 = [55, 60, 58, 50]
    assert classify_batteries(present_capacities_3) == (0, 0, 4)

    present_capacities_4 = []
    assert classify_batteries(present_capacities_4) == (0, 0, 0)

test_classify_batteries()
