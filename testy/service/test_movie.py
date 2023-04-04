
import pytest
from testy.conftest.movie_conf import movie_dao
from service.movies_serv import MovieServise


class TestMovieService:

    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieServise(dao=movie_dao)

    def test_get_all(self):
        result = self.movie_service.get_all()

        assert len(result) > 0

    def test_get_one(self):
        result = self.movie_service.get_one(1)

        assert result is not None
        assert result.title is not None
        assert result.title == "Silicon Valley"

    def test_creat(self):
        result = {
            "title": "Silicon Valley",
            "description": "Сериал 'Кремниевая долина', это любопытное повествование, посвященное влиянию новых технологий на жизнь планеты.",
            "trailer": "https://lordserial.fun/144-kremnievaya-dolina-72.html",
            "year": 2014,
            "rating": 9.3
        }

        movie = self.movie_service.create(result)

        assert movie == "Game of Thrones"
        assert movie is not None

    def test_delete(self):
        self.movie_service.delete(1)

    def test_update(self):
        result = {
            "id": 4,
            "title": "Silicon Valley",
            "description": "Сериал 'Кремниевая долина', это любопытное повествование, посвященное влиянию новых технологий на жизнь планеты.",
            "trailer": "https://lordserial.fun/144-kremnievaya-dolina-72.html",
            "year": 2014,
            "rating": 9.3,
            "genre_id": 2,
            "director_id": 1
        }

        movie = self.movie_service.update(result)
