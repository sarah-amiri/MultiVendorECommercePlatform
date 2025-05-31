from src.app.core.hashers import BCryptSHA25PasswordHasher, make_hash_password

password_hash = 'bcrypt_sha256$$2b$12$e.g.Ogv.WNrWHYEc7eXspuSDc6XGFdin2J15ssWzlBInpv4nljuRW'
salt = '$2b$12$e.g.Ogv.WNrWHYEc7eXspu'
raw_password = 'password'


def test_make_password():
    hasher = BCryptSHA25PasswordHasher(raw_password, salt)
    hashed_password = hasher.make_password()
    assert hashed_password == password_hash


def test_make_password_without_salt():
    hasher = BCryptSHA25PasswordHasher(raw_password)
    hashed_password = hasher.make_password()
    assert hashed_password != password_hash


def test_verify():
    hasher = BCryptSHA25PasswordHasher(raw_password, salt)
    assert hasher.verify(password_hash) is True


def test_make_hash_password():
    _raw = 'test_this_password'
    _hashed, _salt = make_hash_password(_raw)
    hasher = BCryptSHA25PasswordHasher(_raw, _salt)
    assert hasher.verify(_hashed) is True
