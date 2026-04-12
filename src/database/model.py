from sqlalchemy import Table, Column, Integer, String, BigInteger, ForeignKey, text, CheckConstraint, Index, MetaData
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Annotated
import datetime

from src.database.database import Base

intpk = Annotated[int, mapped_column(primary_key=True)]

class UsersOrm(Base):
    __tablename__ = "users"

    id: Mapped[intpk]
    user_id: Mapped[int] = mapped_column(BigInteger, nullable=False, unique=True)
    username: Mapped[str | None]
    name: Mapped[str]
    registration_date: Mapped[datetime.datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))

    active_connection: Mapped["ActiveUserOrm"] = relationship(back_populates="user")

class ActiveUserOrm(Base):
    __tablename__ = "active_users"

    id: Mapped[intpk]
    user_id: Mapped[int | None] = mapped_column(ForeignKey("users.user_id"))
    port_id: Mapped[int | None] = mapped_column(ForeignKey("ports.id"))

    user: Mapped["UsersOrm"] = relationship(back_populates="active_connection")
    port: Mapped["PortsOrm"] = relationship(back_populates="users")

class PortsOrm(Base):
    __tablename__ = "ports"

    id: Mapped[intpk]
    port: Mapped[int]
    secret: Mapped[str]
    sponsor: Mapped[str | None]

    users: Mapped[list["ActiveUserOrm"]] = relationship(back_populates="port")

    host_id: Mapped[int] = mapped_column(ForeignKey("hosts.id"))
    host: Mapped["HostsOrm"] = relationship(back_populates="ports")

class HostsOrm(Base):
    __tablename__ = "hosts"

    id: Mapped[intpk]
    ip_address: Mapped[str]
    is_active: Mapped[bool] = mapped_column(default=True)

    ports: Mapped[list["PortsOrm"]] = relationship(back_populates="host")

class SponsorSubOrm(Base):
    __tablename__ = "sponsors_sub"

    id: Mapped[intpk]
    name: Mapped[str | None]
    channel_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    url: Mapped[str]