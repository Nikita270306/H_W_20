
from unittest.mock import MagicMock
import pytest

from dao.genres_dao import GenreDao
from dao.model.genre_model import Genre


@pytest.fixture
def genre_dao():
    genre_dao = GenreDao(None)

    horror = Genre(name='horror')
    drama = Genre(name='drama')
    comedy = Genre(name='comedy')

    genre_dao.get_all = MagicMock(return_value=[horror, drama, comedy])
    genre_dao.get_one = MagicMock(return_value=horror)
    return genre_dao
