import factory

from vacancies.models import Vacancy


class VacancyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Vacancy

    slug = "test"
    name = "test"
    text = "test text"
