from datetime import datetime

from . import db, modelling, types


def main():
    """Main process of model-service command. Trains a model and saves the coefficients."""
    print("Retrieving measurements...")
    measurements: list[types.Measurement] = db.all_measurements()

    print("Fitting model on measurements...")
    model: types.Model = modelling.from_measurements(
        measurements,
        "rare",
        datetime.now(),
    )

    print("Saving model...")
    db.save_model(model)

    print("Done!")
