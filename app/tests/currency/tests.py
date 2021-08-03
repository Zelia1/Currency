import pytest

from currency import choices


@pytest.mark.skip
def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert [t.name for t in response.templates] == [
        'index.html',
        'base.html',
        'includes/navbar.html',
        'includes/footer.html']


def test_rate_list(client):
    response = client.get('/currency/rate/')
    assert response.status_code == 200


def test_create_rate_get_form(client):
    response = client.get('/currency/rate/create/')
    assert response.status_code == 200


def test_create_rate_empty_form_data(client):
    response = client.post('/currency/rate/create/')
    assert response.status_code == 200
    assert response.context['form'].errors == {
        'type': ['This field is required.'],
        'sale': ['This field is required.'],
        'buy': ['This field is required.'],
        'bank': ['This field is required.']
    }


def test_create_rate_invalid_form_data(client):
    form_data = {
        'type': choices.RATE_TYPE_USD,
        'sale': 26,
        'buy': 27,
        'bank': 999999,
    }
    response = client.post('/currency/rate/create/', data=form_data)
    assert response.status_code == 200
    assert response.context['form'].errors == {
        'bank': ['Select a valid choice. That choice is not one of the available choices.'],
    }



