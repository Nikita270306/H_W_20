
import pytest
from service.genres_serv import GenreServise
from testy.conftest.genre_conf import genre_dao


class TestGenreService:

    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreServise(dao=genre_dao)

    def test_get_all(self):
        result = self.genre_service.get_all()

        assert len(result) > 0

    def test_get_one(self):
        result = self.genre_service.get_one(1)

        assert result is not None
        assert result.name is not None
