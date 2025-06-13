import datetime
from src.app.domain import (
    Category,
    Color,
    Currency,
    Price,
    Product,
    ProductVariant,
    VendorProduct
)


class TestCategory:
    def test_valid_category(self):
        category = Category(
            id=1,
            name='category1',
            slug='category1',
            description='category 1 description',
            is_active=True
        )
        assert category.id == 1
        assert category.name == 'category1'
        assert category.slug == 'category1'
        assert category.description == 'category 1 description'
        assert category.is_active is True

    def test_category_with_optional_fields(self):
        category = Category(id=2, name='category2', slug='category2')
        assert category.id == 2
        assert category.slug == 'category2'
        assert category.name == 'category2'
        assert category.description is None
        assert category.is_active is True


class TestProductVariant:
    def test_product_variant_initialization(self):
        product_variant = ProductVariant(
            id=1,
            product_id=100,
            subname='A56',
            size=128,
            color=Color.RED,
        )
        assert product_variant.id == 1
        assert product_variant.product_id == 100
        assert product_variant.subname == 'A56'
        assert product_variant.size == 128
        assert product_variant.color == Color.RED

    def test_product_variant_init_with_optional_fields(self):
        product_variant = ProductVariant(id=1, product_id=10)
        assert product_variant.id == 1
        assert product_variant.product_id == 10
        assert product_variant.subname is None
        assert product_variant.size is None
        assert product_variant.color is None


class TestProduct:
    def test_product_initialization(self):
        variant1 = ProductVariant(id=1, product_id=10, subname='A55', size=128, color=Color.RED)
        variant2 = ProductVariant(id=2, product_id=10, subname='A56', size=256, color=Color.GREEN)
        product = Product(
            id=10,
            name='Samsung',
            description='Samsung mobile phone',
            category_id=1,
            price=Price(value=256),
            currency=Currency.USD,
            is_active=True,
            created_at=datetime.datetime.now(),
            variants=[variant1, variant2],
        )
        assert product.id == 10
        assert product.price.value == 256
        assert len(product.variants) == 2
        assert isinstance(product.variants[0], ProductVariant)
        assert isinstance(product.variants[1], ProductVariant)
        assert product.variants[0].id != product.variants[1].id


class TestVendorProduct:
    def test_vendor_product_initialization(self):
        vendor_product = VendorProduct(product_id=1, vendor_id=1)
        assert vendor_product.product_id == 1
        assert vendor_product.vendor_id == 1
