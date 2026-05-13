from dummy.run import runny


def test_runny() -> None:
    out = runny()
    assert "Hello world" in out
