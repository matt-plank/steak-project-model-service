from pytest import fixture


@fixture
def measurements():
    return [
        {
            "thickness": 0.5,
            "cookTime": 30,
            "doneness": "well",
        },
        {
            "thickness": 1.0,
            "cookTime": 30,
            "doneness": "medium",
        },
        {
            "thickness": 1.5,
            "cookTime": 30,
            "doneness": "rare",
        },
        {
            "thickness": 2.0,
            "cookTime": 30,
            "doneness": "raw",
        },
        {
            "thickness": 0.5,
            "cookTime": 60,
            "doneness": "burnt",
        },
        {
            "thickness": 1.0,
            "cookTime": 60,
            "doneness": "well",
        },
        {
            "thickness": 1.5,
            "cookTime": 60,
            "doneness": "medium",
        },
        {
            "thickness": 2.0,
            "cookTime": 60,
            "doneness": "rare",
        },
    ]
