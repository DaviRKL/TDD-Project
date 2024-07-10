from datetime import datetime
import uuid
from pydantic import Field, BaseModel, UUID4


class BaseSchemaMixin(BaseModel):
    id: UUID4 = Field(default_factory=uuid.uuid4)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
