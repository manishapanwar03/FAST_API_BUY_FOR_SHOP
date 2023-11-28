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
    
