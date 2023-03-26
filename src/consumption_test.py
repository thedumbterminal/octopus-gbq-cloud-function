from .consumption import consumption_from_response


def test_consumption_from_response_no_data():
    response = {"count": 0, "results": []}
    output = consumption_from_response(response)
    assert output == None


def test_consumption_from_response_with_data():
    response = {"count": 1, "results": [{"consumption": 123}]}
    output = consumption_from_response(response)
    assert output == 123
