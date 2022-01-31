import pytest

from vacancies.models import Vacancy


@pytest.mark.django_db
def test_vacancy_list(client, vacancy):
    expected_response = {
        'count': 1,
        'next': None,
        'previous': None,
        'results': [{
            "id": vacancy.pk,
            "name": "test",
            "text": "test text",
            "skills": [],
            "username": None,
        }]
    }

    response = client.get(f"/vacancy/")

    assert response.status_code == 200
    assert response.data == expected_response