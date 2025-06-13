import json
from datetime import datetime
import pytest
from bson import ObjectId
import time
from src.app.infrastructure.models import (
    CategoryCreateModel,
    CategoryModel,
    CategoryUpdateModel,
)


def test_valid_init_category_model():
    category = CategoryModel(
        name='category1',
        description='description of category 1',
        is_active=True,
        _id=ObjectId(),
        slug='category-1',
    )
    assert category.name == 'category1'
    assert category.description == 'description of category 1'
    assert category.is_active is True
    assert isinstance(category.id, ObjectId)
    assert category.slug == 'category-1'


def test_invalid_object_id_raises_error():
    with pytest.raises(ValueError) as exc_info:
        _ = CategoryModel(
            name='category1',
            description='description of category 1',
            is_active=True,
            _id='invalid-id',
            slug='category-d'
        )
    assert exc_info.value.error_count() == 1
    error = exc_info.value.errors()[0]
    assert error['loc'][0] == '_id'
    assert 'Invalid ObjectId' in error['msg']


def test_category_model_dict():
    category = CategoryModel(
        name='category1',
        description='description of category 1',
        is_active=True,
        _id=ObjectId(),
        slug='category-1',
    )
    category_dict = category.model_dump()
    assert isinstance(category_dict, dict)
    assert '_id' not in category_dict
    assert isinstance(category_dict['id'], ObjectId)


def test_category_model_json():
    category = CategoryModel(
        name='category1',
        description='description of category 1',
        is_active=True,
        _id=ObjectId(),
        slug='category-1',
    )
    category_json = json.loads(category.model_dump_json())
    assert isinstance(category_json, dict)
    assert '_id' not in category_json
    assert isinstance(category_json['id'], str)


def test_valid_init_create_model():
    category = CategoryCreateModel(
        name='category_1',
        description='description of category_1',
        is_active=True,
    )
    assert hasattr(category, 'created_at')
    assert hasattr(category, 'slug')
    assert isinstance(category.created_at, datetime)
    assert category.slug is not None
    assert category.slug == 'category-1'
    assert not hasattr(category, 'id')


def test_valid_init_update_model():
    category = CategoryUpdateModel(
        name='category_1',
        description='description of category_1',
        is_active=True,
    )
    assert hasattr(category, 'updated_at')
    assert isinstance(category.updated_at, datetime)
    assert not hasattr(category, 'id')
    assert not hasattr(category, 'slug')


def test_update_model_can_be_initialized_with_updated_time():
    now = datetime.now()
    time.sleep(1)
    category = CategoryUpdateModel(
        name='category_1',
        description='description of category_1',
        is_active=True,
        updated_at=now,
    )
    assert category.updated_at == now
