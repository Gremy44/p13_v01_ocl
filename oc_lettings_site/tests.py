def test_dummy():
    """
    A dummy test to ensure the test setup is working.
    """
    assert 1


def test_index_returns_200(client):
    """
    Test whether the index view returns a status code of 200.

    Args:
    client: Django test client.

    Returns:
    None
    """
    response = client.get("/")
    assert response.status_code == 200


def test_admin_returns_302(client):
    """
    Test whether the admin view returns a status code of 302 (redirection).

    Args:
    client: Django test client.

    Returns:
    None
    """
    response = client.get("/admin/")
    assert response.status_code == 302


def test_return_404_for_invalid_request(client):
    """
    Test whether the server returns a status code of 404 for an invalid request.

    Args:
    client: Django test client.

    Returns:
    None
    """
    response = client.get("/invalid/")
    assert response.status_code == 404


# @pytest.mark.xfail(raises=Exception)
def test_internal_server_error(client):
    """
    Test internal server error on a URL that raises an exception.

    Args:
    client: Django test client.

    Returns:
    None
    """
    # raise Exception("500 error test")
    response = client.get('/error500/')
    assert response.status_code == 500
