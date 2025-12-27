import multiprocessing

import pytest


@pytest.fixture(scope="session", autouse=True)
def set_spawn_context():
    multiprocessing.set_start_method("spawn", force=True)
    yield
