from tsdemo.prime import is_prime


def test_is_prime_not_prime_1():
    result = is_prime(n=15)
    assert result is False


def test_is_prime_2_is_prime():
    result = is_prime(n=2)
    assert result is True


def test_is_prime_not_prime():
    result = is_prime(n=4)
    assert result is False


def test_is_prime_is_prime():
    result = is_prime(n=3)
    assert result is True
