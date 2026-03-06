def pytest_configure(config):
    config.addinivalue_line(
        "markers", "api: tests related to API endpoints"
    )
    config.addinivalue_line(
        "markers", "ui: tests related to user interface"
    )
