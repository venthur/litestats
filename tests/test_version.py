def test_version():
    from litestats import __VERSION__
    assert isinstance(__VERSION__, str)
