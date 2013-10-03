from mock import Mock

from django.test import TestCase

from pycon.wines.models import FarmHouse


class FarmTestCase(TestCase):

    def setUp(self):
        self.farm_house = FarmHouse()
        self.farm_house.get_contents = Mock(return_value=['farmer', 'farmesss', 'dog', 'cat'])

    def test_contents(self):
        contents = self.farm_house.get_contents()
        self.assertEqual('farmer', contents[0])