def test_measurements(db):
    measurements = list(db.all_measurements())

    assert len(measurements) == 2
