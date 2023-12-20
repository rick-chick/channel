from sqlalchemy import (
    String,
    Column,
    DateTime,
    Integer,
    Float
)
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
)
from sqlalchemy.ext.declarative import declared_attr
from datetime import datetime


class Base(DeclarativeBase):
    pass


class TimestampMixin(object):
    @declared_attr
    def created_at(cls):
        return Column(DateTime, default=datetime.now(), nullable=False)

    @declared_attr
    def updated_at(cls):
        return Column(
            DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False
        )

    @declared_attr
    def created_by(cls):
        return Column(String(36), nullable=False)

    @declared_attr
    def updated_by(cls):
        return Column(String(36), nullable=False)


class UserDataSource(Base, TimestampMixin):
    __tablename__ = 'users'

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    email: Mapped[str] = mapped_column(String(255))
    password_hash: Mapped[str] = mapped_column(String(255))


class DeviceDataSource(Base, TimestampMixin):
    __tablename__ = 'devices'

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    user_id: Mapped[str] = mapped_column(String(36))
    api_key: Mapped[str] = mapped_column(String(36))


class ChannelDataSource(Base, TimestampMixin):
    __tablename__ = 'channels'

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    device_id: Mapped[int] = mapped_column(Integer)
    name: Mapped[str] = mapped_column(String(255))
    unit: Mapped[str] = mapped_column(String(32))


class RecordDataSource(Base):
    __tablename__ = 'records'

    channel_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    time: Mapped[datetime] = mapped_column(DateTime, primary_key=True)
    value: Mapped[float] = mapped_column(Float, nullable=False)
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now(), nullable=False)
