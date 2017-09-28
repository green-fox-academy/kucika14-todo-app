from todo_app import Todo
import unittest

test_app = StartScreen()

class TodoAppTest(object):

    def test_get_arguments(self):
        self.assertEqual(test_app.get_arguments(),['Walk the dog', 'Buy milk', 'Do homework'])