import pytest

from tests.factories import VacancyFactory
from vacancies.serializers import VacancyListSerializer


@pytest.mark.django_db
def test_list_view(client):
    vacancies = VacancyFactory.create_batch(10)

    response = client.get("/vacancy/")

    expected_response = {
        'count': 10,
        'next': None,
        'previous': None,
        'results': VacancyListSerializer(vacancies, many=True).data
    }

    assert response.status_code == 200
    assert response.data == expected_response