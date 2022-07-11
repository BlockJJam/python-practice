from cleancode.unittest import MergeRequestStatus as Status

def evaluate_merge_request(upvote_cnt, downvote_cnt):
    if downvote_cnt > 0:
        return Status.REJECTED
    if upvote_cnt >= 2:
        return Status.APPROVED

    return Status.PENDING
