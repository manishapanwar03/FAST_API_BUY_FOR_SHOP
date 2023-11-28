# to install tortoise : pip install tortoise

from tortoise.models import Model
from tortoise import Tortoise, fields
from datetime import datetime


class Category(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(200, unique=True)
    category_image = fields.TextField()
    description = fields.TextField()
    is_active = fields.BooleanField(default=True)
    updated_at = fields.DatetimeField(auto_now=True)
    created_at = fields.DatetimeField(auto_now_add=True)


class Subcategory(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(200, unique=True)
    subcategory_image = fields.TextField()
    description = fields.TextField()
    category = fields.ForeignKeyField(
        "models.Category", related_name="subcatergory", on_delete="CASCADE"
    )
    is_active = fields.BooleanField(default=True)
    updated_at = fields.DatetimeField(auto_now=True)
    created_at = fields.DatetimeField(auto_now_add=True)


class Brand(Model):
    id = fields.IntField(pk=True)
    brand_name = fields.CharField(200, unique=True)
    is_active = fields.BooleanField(default=True)
    updated_at = fields.DatetimeField(auto_now=True)
    created_at = fields.DatetimeField(auto_now_add=True)





class Product(Model):
    id = fields.IntField(pk=True)
    product_name = fields.CharField(150)
    manufacturing = fields.CharField(30)
    product_image = fields.TextField()
    video = fields.TextField()
    product_code = fields.IntField()
    model_no = fields.CharField(200)
    description = fields.TextField()
    length = fields.IntField()
    width = fields.IntField()
    height = fields.IntField()
    weight = fields.FloatField()
    hsn_code = fields.IntField()
    mrp = fields.IntField()
    base_price = fields.IntField()
    gst = fields.IntField()
    offer_price = fields.IntField()
    catergory = fields.ForeignKeyField(
        "models.Category", related_name="catergory", on_delete="CASCADE"
    )
    subcatergory = fields.ForeignKeyField(
        "models.Subcategory", related_name="subcatergory", on_delete="CASCADE"
    )
    brand = fields.ForeignKeyField(
        "models.Brand", related_name="brand", on_delete="CASCADE"
    )
    is_active = fields.BooleanField(default=True)
    updated_at = fields.DatetimeField(auto_now=True)
    created_at = fields.DatetimeField(auto_now_add=True)
