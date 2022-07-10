from cleancode.unittest import merge_req
from cleancode.unittest.merge_req import AcceptanceThreshold, MergeRequestException, MergeRequestStatus, MergeRequestException
import unittest
from unittest.mock import Mock
from cleancode.unittest import MergeRequest, MergeRequestStatus

class TestMergeRequestStatus(unittest.TestCase):
    
    def setUp(self):
        self.merge_request = MergeRequest()
        self.fixture_data = (
            (
                {'downvotes': set(), 'upvotes': set()},
            MergeRequestStatus.PENDING
            ),
            (
                {'downvotes': set(), 'upvotes': {'dev1'}},
            MergeRequestStatus.PENDING
            ),
            (
                {'downvotes': 'dev1', 'upvotes': set()},
            MergeRequestStatus.REJECTED
            ),
            (
                {'downvotes': set(), 'upvotes': {'dev1','dev2'}},
            MergeRequestStatus.APPROVED
            ),
        )

    def test_simple_rejected(self):
        merge_request = MergeRequest()
        merge_request.downvote('maintainer')
        self.assertEqual(merge_request.status, MergeRequestStatus.REJECTED)

    def test_just_created_is_pending(self):
        self.assertEqual(MergeRequest().status, MergeRequestStatus.PENDING)
        
    def test_pending_awaiting_review(self):
        merge_request = MergeRequest()
        merge_request.upvote('core-dev')
        self.assertEqual(merge_request.status, MergeRequestStatus.PENDING)

    def test_approved(self):
        merge_request = MergeRequest()
        merge_request.upvote('dev1')
        merge_request.upvote('dev2')
        self.assertEqual(merge_request.status, MergeRequestStatus.APPROVED)

    def test_cannot_upvote_on_closed_merge_request(self):
        self.merge_request.close()
        self.assertRaises(
            MergeRequestException, self.merge_request.upvote, 'dev1'
        )
        
    def test_cannot_downvote_on_closed_merge_request(self):
        self.merge_request.close()
        self.assertRaisesRegex(
            MergeRequestException,
            "종료된 머지 리퀘스트에 투표할 수 없음",
            self.merge_request.downvote,
            'dev1'
        )

    def test_status_resolution(self):
        for context, expected in self.fixture_data:
            with self.subTest(context = context):
                status = AcceptanceThreshold(context).status()
                self.assertEqual(status, expected)