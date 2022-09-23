from unittest.mock import patch
from tsdemo.patch_string import get_db_name


def test_get_db_name():
    with patch('tsdemo.patch_string.DB_NAME', 'test'):
        result = get_db_name()
    assert result == 'test'
