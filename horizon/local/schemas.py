from typing import Dict, Any, Optional, List
from pydantic import BaseModel


class BaseSchema(BaseModel):
    class Config:
        orm_mode = True

class Message(BaseModel):
    detail: str

class SyncedRole(BaseSchema):
    id: str
    name: str
    org_id: Optional[str]
    permissions: Optional[List[str]]


class SyncedUser(BaseSchema):
    id: str
    name: Optional[str]
    email: Optional[str]
    roles: List[SyncedRole]