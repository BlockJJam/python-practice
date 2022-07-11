import unittest

from cleancode.unittest import MergeRequestStatus as Status
from sample_test.mutation_testing_1 import evaluate_merge_request

class TestMergeRequestEvalutation(unittest.TestCase):
    def test_approved(self):
        result = evaluate_merge_request(3,0)
        self.assertEqual(result, Status.APPROVED)