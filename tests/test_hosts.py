import pytest

from app.services.hosts import host_proibido

@pytest.mark.parametrize("host, esperado", [
    ("localhost",  True),
    ("localhost.", True),
    ("LOCALHOST",  True),
    ("127.0.0.1",  True),
    ("127.9.9.9",  True),
    ("0.0.0.0",    True),
    ("[::1]",      True),

    ("python.org",      False),
    ("127.exemple.com", False),
])

def test_host_proibido(host, esperado):
    assert host_proibido(host) is esperado
