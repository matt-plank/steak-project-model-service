from . import db, modelling, types


def main():
    """Main process of model-service command. Trains a model and saves the coefficients."""
    measurements: list[types.Measurement] = db.all_measurements()
    coefs: types.Coefs = modelling.coefficients(measurements, "rare")
    db.save_model_coefficients(coefs)
