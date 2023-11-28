# serializer

from pydantic import BaseModel


class CatergoryItem(BaseModel):
     name:str
     description:str

class CatergoryUpdate(CatergoryItem):
     id:int

class CatergoryDelete(BaseModel):
     id:int

class SubcatergoryItem(BaseModel):
     catergory_id:int
     name:str
     description:str

class SubcatergoryUpdate(BaseModel):
     id:int
     name:str
     description:str

class SubcatergoryDelete(BaseModel):
     id:int

class BrandItem(BaseModel):
      brand_name:str

class BrandUpdate(BrandItem):
     id:int

class BrandDelete(BaseModel):
     id:int
   
    
class ProductItem(BaseModel):
     id:int
     catergory_id:int
     subcategory_id:int
     brand_id:int
     product_name:str
     manufacturing:str
     product_code :int
     model_no :str
     description:str
     length :int
     width:int
     height:int
     weight:int
     hsn_code :int
     mrp:int
     base_price:int
     gst:int
     offer_price:int
     