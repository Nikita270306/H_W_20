
from unittest.mock import MagicMock
import pytest

from dao.model.director_model import Director
from dao.directors_dao import DirectorDao


@pytest.fixture
def director_dao():
    director_dao = DirectorDao(None)

    nikita = Director(id=1, name='Nikita')
    egor = Director(id=2, name='Egor')
    kolya = Director(id=3, name='Kolya')

    director_dao.get_one = MagicMock(return_value=nikita)
    director_dao.get_all = MagicMock(return_value=[nikita, egor, kolya])

    return director_dao
