from datetime import datetime

from sklearn.linear_model import LogisticRegression

from .types import Coefs, Doneness, Measurement, Model


def decision_boundary(xs: list[list[float]], ys: list[bool]) -> Coefs:
    """The coefficients of the decision boundary for a logistic regression model."""
    model = LogisticRegression()
    model.fit(xs, ys)

    thickness = -model.coef_[0][0] / model.coef_[0][1]
    bias = -model.intercept_[0] / model.coef_[0][1]

    return {"thickness": thickness, "bias": bias}


def from_measurements(
    measurements: list[Measurement], doneness: Doneness, created_time: datetime
) -> Model:
    """The coefficients of the model that predicts the cook-time according to thickness."""
    xs = [[m["thickness"], m["cookTime"]] for m in measurements]

    donenesses = ["raw", "rare", "medium", "well", "burnt"]

    ys_overdone = [
        donenesses.index(m["doneness"]) >= donenesses.index(doneness)
        for m in measurements
    ]

    ys_underdone = [
        donenesses.index(m["doneness"]) <= donenesses.index(doneness)
        for m in measurements
    ]

    overcooked_boundary = decision_boundary(xs, ys_overdone)
    undercooked_boundary = decision_boundary(xs, ys_underdone)

    return {
        "created": created_time,
        "doneness": doneness,
        "coefficients": {
            "thickness": (
                undercooked_boundary["thickness"] + overcooked_boundary["thickness"]
            )
            / 2,
            "bias": (undercooked_boundary["bias"] + overcooked_boundary["bias"]) / 2,
        },
    }
