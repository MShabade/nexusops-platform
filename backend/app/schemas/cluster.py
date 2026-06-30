from datetime import datetime

from pydantic import BaseModel


class ClusterCreate(BaseModel):
    name: str
    provider: str
    region: str = ""
    api_endpoint: str


class ClusterOut(BaseModel):
    id: int
    name: str
    provider: str
    region: str
    api_endpoint: str
    status: str
    created_at: datetime

    model_config = {"from_attributes": True}
