from sqlalchemy import Select

from fastapi_zero.models import User


def test_create_user(session):
    new_user = User(
        username='carlos', password='secret', email='email@test.com'
    )
    session.add(new_user)
    session.commit()

    user = session.scalar(Select(User).where(User.username == 'carlos'))

    assert user.username == 'carlos'
