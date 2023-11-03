from pytest import fixture


@fixture
def db(set_env_vars):
    from model_service import db

    db.measurements.insert_many(
        [
            {
                "thickness": "2.5",
                "cookTime": 90,
                "doneness": "rare",
            },
            {
                "thickness": "3.5",
                "cookTime": 120,
                "doneness": "rare",
            },
        ]
    )

    yield db

    db.measurements.drop()


@fixture
def set_env_vars(monkeypatch):
    monkeypatch.setenv("MONGO_DATABASE", "test_steak_project")
