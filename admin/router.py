from fastapi import APIRouter, Request, Form, status, Depends, UploadFile, File
from fastapi.responses import HTMLResponse, RedirectResponse
from .models import *
from passlib.context import CryptContext
from .pydentic_modules import (
    CatergoryItem,
    CatergoryUpdate,
    CatergoryDelete,
    SubcatergoryItem,
    SubcatergoryUpdate,
    SubcatergoryDelete,
)
from fastapi_login import LoginManager
from slugify import slugify

import os

SECRET = "your-secret-key"


router = APIRouter()
manager = LoginManager(SECRET, token_url="/auth/token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


@router.post("/catergory/")
async def create_catergory(
    data: CatergoryItem = Depends(), category_image: UploadFile = File(...)
):
    if await Category.exists(name=data.name):
        return {"status": False, "message": "Category already exists."}
    else:
        FILEPATH = "static/images/catergory/"
        os.makedirs(FILEPATH, exist_ok=True)

        filename = category_image.filename
        extension = filename.split(".")[1]
        imagename = filename.split(".")[0]

        if extension not in ["png", "jpg", "jpeg"]:
            return {"status": False, "message": "Invalid file type"}

        dt = datetime.now()
        dt_timestamp = round(datetime.timestamp(dt))

        modify_image_name = imagename + "_" + str(dt_timestamp) + "." + extension
        generated_name = FILEPATH + modify_image_name
        file_content = await category_image.read()
        with open(generated_name, "wb") as f:
            f.write(file_content)
            f.close()

        catergory_obj = await Category.create(
            category_image=generated_name, description=data.description, name=data.name
        )
        return catergory_obj


@router.get("/catergory/")
async def get_catergory():
    categories = await Category.filter(is_active=True)
    return categories


@router.put("/catergory/")
async def put_catergory(
    data: CatergoryUpdate = Depends(), category_image: UploadFile = File(...)
):
    if await Category.exists(id=data.id):
        FILEPATH = "static/images/catergory/"
        os.makedirs(FILEPATH, exist_ok=True)
        filename = category_image.filename
        extension = filename.split(".")[1]
        imagename = filename.split(".")[0]

        if extension not in ["png", "jpg", "jpeg"]:
            return {"status": False, "message": "Invalid file type"}

        dt = datetime.now()
        dt_timestamp = round(datetime.timestamp(dt))

        modify_image_name = imagename + "_" + str(dt_timestamp) + "." + extension
        generated_name = FILEPATH + modify_image_name
        file_content = await category_image.read()
        with open(generated_name, "wb") as f:
            f.write(file_content)
            f.close()

        catergory_obj = await Category.filter(id=data.id).update(
            category_image=generated_name, description=data.description, name=data.name
        )
        return catergory_obj


@router.delete("/catergory/")
async def delete_catergory(data: CatergoryDelete):
    data = await Category.filter(id=data.id).delete()
    return data


@router.post("/subcatergory/")
async def create_subcatergory(
    data: SubcatergoryItem = Depends(), subcategory_image: UploadFile = File(...)
):
    if await Category.exists(id=data.catergory_id):
        catergory_obj = await Category.get(id=data.catergory_id)

        if await Subcategory.exists(name=data.name):
            return {"status": False, "message": "subcategory already exists."}
        else:
            FILEPATH = "static/images/subcatergory/"
            os.makedirs(FILEPATH, exist_ok=True)

            filename = subcategory_image.filename
            extension = filename.split(".")[1]
            imagename = filename.split(".")[0]

            if extension not in ["png", "jpg", "jpeg"]:
                return {"status": False, "message": "Invalid file type"}

            dt = datetime.now()
            dt_timestamp = round(datetime.timestamp(dt))

            modify_image_name = imagename + "_" + str(dt_timestamp) + "." + extension
            generated_name = FILEPATH + modify_image_name
            file_content = await subcategory_image.read()
            with open(generated_name, "wb") as f:
                f.write(file_content)
                f.close()

            subcatergory_obj = await Subcategory.create(
                category=catergory_obj,
                subcategory_image=generated_name,
                description=data.description,
                name=data.name,
            )
            return subcatergory_obj



@router.get("/subcatergory/")
async def get_subcatergory():
    subcategories = await Subcategory.filter(is_active=True)
    return subcategories


@router.put("/subcatergory/")
async def put_subcatergory(
    data: SubcatergoryUpdate = Depends(), category_image: UploadFile = File(...)
):
    if await Subcategory.exists(id=data.id):
        FILEPATH = "static/images/subcatergory/"
        os.makedirs(FILEPATH, exist_ok=True)
        filename = category_image.filename
        extension = filename.split(".")[1]
        imagename = filename.split(".")[0]

        if extension not in ["png", "jpg", "jpeg"]:
            return {"status": False, "message": "Invalid file type"}

        dt = datetime.now()
        dt_timestamp = round(datetime.timestamp(dt))

        modify_image_name = imagename + "_" + str(dt_timestamp) + "." + extension
        generated_name = FILEPATH + modify_image_name
        file_content = await category_image.read()
        with open(generated_name, "wb") as f:
            f.write(file_content)
            f.close()

        subcatergory_obj = await Subcategory.filter(id=data.id).update(
            subcategory_image=generated_name, description=data.description, name=data.name
        )
        return subcatergory_obj



@router.delete("/subcatergory/")
async def delete_subcatergory(data:SubcatergoryDelete):
    data = await Subcategory.filter(id=data.id).delete()
    return data