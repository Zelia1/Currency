from currency import choices
from currency.models import Banks, Rate

import pytest # noqa


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
    rate_initial_count = Rate.objects.count()
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
    assert Rate.objects.count() == rate_initial_count


def test_create_rate_success(client):
    rate_initial_count = Rate.objects.count()
    bank = Banks.objects.last()
    form_data = {
        'type': choices.RATE_TYPE_USD,
        'sale': 26,
        'buy': 27,
        'bank': bank.id,
    }
    response = client.post('/currency/rate/create/', data=form_data)
    assert response.status_code == 302
    assert response.url == '/currency/rate/'
    assert Rate.objects.count() == rate_initial_count + 1


@pytest.mark.skip
def test_create_contact_us(client, mailoutbox, settings):
    form_data = {
        'email_from': 'PavelTest1990@gmail.com',
        'subject': 'hello from test',
        'message': 'I`m test!',
    }
    response = client.post('/currency/contactus/create/', data=form_data)
    assert response.status_code == 302
    assert response.url == '/currency/contactus/'
    assert len(mailoutbox) == 1
    mail = mailoutbox[0]
    assert mail.to == ['zelenskiy.zelia@gmail.com']
    assert mail.cc == []
    assert mail.bcc == []
    assert mail.reply_to == []
    assert mail.from_email == settings.EMAIL_HOST_USER
