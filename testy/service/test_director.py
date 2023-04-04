
import pytest
from service.directors_serv import DirectorServise
from testy.conftest.director_conf import director_dao


class TestDirectorService:

    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorServise(dao=director_dao)

    def test_get_all(self):
        result = self.director_service.get_all()
        assert len(result) > 0

    def test_get_one(self):
        result = self.director_service.get_one(1)

        assert result is not None
        assert result.name is not None
