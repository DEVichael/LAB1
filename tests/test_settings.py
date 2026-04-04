from settings import Settings


def test_settings_load():
    s = Settings()

    assert s.ENVIRONMENT == "test"
    assert s.APP_NAME == "TestApp"
    assert s.api_key == "fake-test-key"
    assert s.password == "fake-test-password"
