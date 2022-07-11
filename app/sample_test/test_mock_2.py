from unittest import mock
from cleancode.unittest import BuildStatus

STATUS_ENDPOINT = 'https://reqres.in/api/users'

@mock.patch('cleancode.unittest.requests')
def test_build_notification_sent(mock_requests):
    build_date = '2019-01-01T00:00:01'
    with mock.patch('cleancode.unittest.BuildStatus.build_date', retrun_value = build_date):
        BuildStatus.notify('123','ok')

    expected_payload =     {
        "name": "123",
        "job": "ok",
        "id": "625",
        "createdAt": "2022-07-11T00:49:08.646Z"
    }
    mock_requests.post.assert_called_with(
        STATUS_ENDPOINT, json = expected_payload
    )
