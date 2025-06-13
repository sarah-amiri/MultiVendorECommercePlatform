from bson import ObjectId
from bson.errors import InvalidId
from src.app.core.exceptions import BadRequestException


def check_id_is_valid_object_id(func):
    async def wrapper(*args, **kwargs):
        _id = kwargs.pop('_id')
        if not ObjectId.is_valid(_id):
            raise BadRequestException('Category id is not a valid object id')
        return await func(*args, **kwargs, category_id=ObjectId(_id))
    return wrapper
