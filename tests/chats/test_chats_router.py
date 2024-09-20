import pytest

@pytest.mark.asyncio
async def test_get_chats_returns_list(client_test):
    response = await client_test.get('/chats', headers={'authorization': 'test'})
    assert response.status_code == 200
    result = response.json()
    assert isinstance(result, list)

@pytest.mark.asyncio
async def test_post_chat_returns_list(client_test):
    response = await client_test.post('/chats', headers={'authorization': 'test'})
    assert response.status_code == 200
    result = response.json()
    assert isinstance(result, dict)


@pytest.mark.asyncio
async def test_post_chat_returns_list(client_test):
    response = await client_test.post('/chats', headers={'authorization': 'test'})
    assert response.status_code == 200
    result = response.json()
    print(result)
    assert isinstance(result, dict)