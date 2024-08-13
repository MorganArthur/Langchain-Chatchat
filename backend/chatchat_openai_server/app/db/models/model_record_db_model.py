import json

from sqlalchemy import Column, String, JSON, DateTime
from sqlalchemy.sql.functions import now

from app.core.base.base_db_model import BaseDbModelMixin
from app.depends.depend_database import Base
from app._types.model_object import ModelObject


class ModelRecordDbModel(Base, BaseDbModelMixin):
    __tablename__ = "model_record"

    model_id = Column(String, index=True)
    model_name = Column(String)
    model_platform = Column(String)
    created = Column(DateTime, default=now())
    metadata_ = Column('metadata', JSON, default={})

    def to_object(self) -> ModelObject:
        if isinstance(self.metadata_, str):
            _metadata = json.loads(self.metadata_)
        else:
            _metadata = self.metadata_
        return ModelObject(
            org_id=self.org_id,
            id=self.model_id,
            created=self.created,
            owned_by=self.owned_by,
            metadata=_metadata,
        )
