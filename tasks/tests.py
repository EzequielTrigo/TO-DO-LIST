from django.test import TestCase
from .models import Todo_task, MiExcepcion
from django.utils import timezone
import datetime
from django.urls import reverse
# Create your tests here.
class TaskModelTests(TestCase):

    def test_is_task_that_will_start_in_future_finished(self):
        task=Todo_task(task_start_date=timezone.now()+datetime.timedelta(days=1))
        exceptionLock=False
        try:
            test=task.task_not_finished_in_time()
        except MiExcepcion:
            exceptionLock=True
        self.assertIs(exceptionLock, True)

    def test_exception_works_rigth(self):
        task=Todo_task(task_start_date=timezone.now()-datetime.timedelta(days=1),
                       task_finished=True, task_expected_finish_date=timezone.now()+datetime.timedelta(days=1),
                       task_finished_date=timezone.now())
        try:
            test=task.task_not_finished_in_time()
        except MiExcepcion:
            self.assertIs(False,True)
        self.assertIs(test,False)

def create_task(task_name,days):
    return Todo_task.objects.create(task_name=task_name, task_comments="", task_start_date=days, task_expected_finish_date=days+datetime.timedelta(days=1))

class TaskIndexViewTests(TestCase):

    def test_no_task(self):
        response = self.client.get(reverse("tasks:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No tasks left.")
        self.assertQuerySetEqual(response.context["latest_task_list"], [])

    def test_past_question(self):
        task = create_task("test", timezone.now())
        response = self.client.get(reverse("tasks:index"))
        self.assertQuerySetEqual(response.context["latest_task_list"], [task])

    def test_past_and_futute_task(self):
        task = create_task("test", timezone.now())
        task_future = create_task("failed", timezone.now() + datetime.timedelta(days=1))
        response = self.client.get(reverse("tasks:index"))
        self.assertQuerySetEqual(response.context["latest_task_list"], [task])

    def test_two_past_question(self):
        task = create_task("test", timezone.now())
        task2 = create_task("test2", timezone.now())
        response = self.client.get(reverse("tasks:index"))
        self.assertQuerySetEqual(response.context["latest_task_list"], [task2, task])