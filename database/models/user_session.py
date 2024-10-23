from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID as pgUUID
from .model_base_class import Base
from datetime import datetime
import uuid

# Define the UserSession model
class UserSession(Base):
    __tablename__ = 'user_sessions'

    session_id = Column(pgUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(pgUUID(as_uuid=True), ForeignKey('users.user_id', ondelete='CASCADE'), nullable=True)  # Nullable for guests
    last_updated = Column(DateTime, default=datetime.utcnow, nullable=False)  # Automatically sets current timestamp