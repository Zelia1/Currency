from currency import choices


def test_rates_list(client_api_auth):
    response = client_api_auth.get('/api/rates/')
    assert response.status_code == 200
    assert 'results' in response.json()


def test_rates_create_invalid(client_api_auth):
    response = client_api_auth.post('/api/rates/', data={})
    assert response.status_code == 400
    assert response.json() == {
        'type': ['This field is required.'],
        'sale': ['This field is required.'],
        'buy': ['This field is required.'],
        'bank': ['This field is required.']
    }


def test_rates_create_success(client_api_auth, bank):
    data = {
        'type': choices.RATE_TYPE_USD,
        'sale': 26,
        'buy': 27,
        'bank': bank.id
    }
    response = client_api_auth.post('/api/rates/', data=data)
    assert response.status_code == 201
    assert response.json()['id'] == 4
    assert response.json()['type'] == 0
    assert response.json()['sale'] == '26.00'
    assert response.json()['buy'] == '27.00'
    assert response.json()['bank'] == 2


def test_rates_update_invalid(client_api_auth, rate):
    response = client_api_auth.put(f'/api/rates/{rate.id}/')

    assert response.status_code == 400
    assert response.json() == {
        'type': ['This field is required.'],
        'sale': ['This field is required.'],
        'buy': ['This field is required.'],
        'bank': ['This field is required.']
    }


def test_rates_update_success(client_api_auth, rate, bank):

    data = {
        'type': choices.RATE_TYPE_USD,
        'sale': 26.45,
        'buy': 27.80,
        'bank': bank.id
    }
    response = client_api_auth.put(f'/api/rates/{rate.id}/', data=data)
    assert response.status_code == 200
    assert response.json()['id'] == 3
    assert response.json()['type'] == 0
    assert response.json()['sale'] == '26.45'
    assert response.json()['buy'] == '27.80'
    assert response.json()['bank'] == 2


def test_rates_parts_update_invalid(client_api_auth, rate, bank):
    data = {
        'sale': 27.45,
        'buy': 28.80,
        'bank': bank.id
    }

    response = client_api_auth.patch(f'/api/rates/{rate.id}/', data=data)
    assert response.status_code == 200
    assert response.request['REQUEST_METHOD'] == 'PATCH'
    assert response.json()['sale'] != str(rate.sale)
    assert response.json()['buy'] != str(rate.buy)
    assert response.json()['bank'] == rate.bank.id


def test_rates_delete(client_api_auth, rate):

    response = client_api_auth.delete(f'/api/rates/{rate.id}/')
    assert response.status_code == 204
    assert response.request['REQUEST_METHOD'] == 'DELETE'
