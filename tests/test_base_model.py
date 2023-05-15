from unittest import TestCase
from models.base_model import BaseModel


class TestBaseModel(TestCase):
    def test_base(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model.save()

        self.assertEqual(my_model.my_number, 89)
