from model_service import modelling


def test_fit(measurements):
    coefs = modelling.coefficients(measurements, "rare")

    assert coefs["thickness"] >= 0.0
    assert coefs["bias"] >= 0.0
