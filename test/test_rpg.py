import unittest

from source import random_password_generator as rpg

class RpgTestCase(unittest.TestCase):
  def test_generator_success(self):
    result = rpg.generate(20, 5, 5)
    self.assertEqual(result["valid"], True)
    self.assertEqual(len(result["password"]), 20)

  def test_generator_error(self):
    result = rpg.generate(20, 11, 5)
    self.assertEqual(result["valid"], False)

    result = rpg.generate(20, 10, 21)
    self.assertEqual(result["valid"], False)

    result = rpg.generate(53, 10, 10)
    self.assertEqual(result["valid"], False)