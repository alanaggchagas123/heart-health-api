from app.utils.security import create_access_token

token = create_access_token({
    "sub": "teste@email.com",
    "id": 1
})

print(token)