import unittest
from app.tester import print_results, load_config_file

class TestTesterModule(unittest.TestCase):
  def test_load_config_file(self):
    automation_list = load_config_file('./tests/test_config_file.yml')
    self.assertEqual(len(automation_list), 1)

  def test_print_results(self):
    test_obj = [
      {
      'name': 'Test',
      'id': '1',
      'execution_status': 'successful',
      },
      {
      'name': 'Test',
      'id': '2',
      'execution_status': 'successful',
      },
    ]
    self.assertRegex(print_results(test_obj), 'results of the critical automation tests')

if __name__ == '__main__':
  unittest.main()