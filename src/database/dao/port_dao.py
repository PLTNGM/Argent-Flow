from sqlalchemy import insert, select, outerjoin, func
from src.database.database import async_session_factory
from src.database.model import PortsOrm, ActiveUserOrm

class PortDao:

    @classmethod
    async def add_port(cls, port: int, secret: str, sponsor: str, host_id: int):
        async with async_session_factory() as session:
            stmt = insert(PortsOrm).values(
                port = port,
                secret = secret,
                sponsor = sponsor,
                host_id = host_id
            )
            await session.execute(stmt)
            await session.commit()

    @classmethod
    async def get_balanced_port(cls):
        async with async_session_factory() as session:
            stmt = (select(PortsOrm).outerjoin(ActiveUserOrm, ActiveUserOrm.port_id == PortsOrm.id)
            .group_by(PortsOrm.id)
            .order_by(func.count(ActiveUserOrm.user_id))
            .limit(1)
            )
            res = await session.execute(stmt)
            return res.scalar_one_or_none()