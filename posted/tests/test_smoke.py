"""Smoke test: the package imports."""


def test_import():
    import posted

    assert posted.__name__ == "posted"
