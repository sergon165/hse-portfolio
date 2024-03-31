from django.test import TestCase

from jobs.models import Job


class JobTestCase(TestCase):
    """
    Тестирование функций портфолио.
    """

    def setUp(self) -> None:
        """
        Настройка перед тестированием.

        :return:
        """

        Job.objects.create(
            description="Job №1 description" * 2,
            full_text="Job №1 full_text. " * 100,
            image="Job №1 image path",
        )

    def test_job_creation(self) -> None:
        """
        Тестирование моделей работ для портфолио.

        :return:
        """

        job = Job.objects.get(description="Job №1 description" * 2)

        full_text = "Job №1 full_text. " * 100
        self.assertEqual(job.summary(), full_text[:100] + "...")
        self.assertEqual(str(job), f'Объект "Выполненная работа" (id={job.pk})')
