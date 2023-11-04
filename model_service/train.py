from datetime import datetime

from . import db, modelling, types


def main():
    """Main process of model-service command. Trains a model and saves the coefficients."""
    measurements: list[types.Measurement] = db.all_measurements()

    coefs: types.Model = modelling.from_measurements(
        measurements,
        "rare",
        datetime.now(),
    )

    db.save_model(coefs)
