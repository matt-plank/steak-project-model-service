from datetime import datetime

from model_service import modelling


def test_fit(measurements):
    model = modelling.from_measurements(
        measurements,
        "rare",
        datetime(2023, 1, 1),
    )

    assert model["created"] == datetime(2023, 1, 1)
    assert model["doneness"] == "rare"
    assert model["coefficients"]["thickness"] >= 0.0
    assert model["coefficients"]["bias"] >= 0.0
