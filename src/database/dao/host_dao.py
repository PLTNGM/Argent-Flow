from sqlalchemy import insert, select
from src.database.database import Base, async_session_factory
from src.database.model import HostsOrm

class HostDao:

    @classmethod
    async def select_all_hosts(cls):
        async with async_session_factory() as session:
            stmt = select(HostsOrm)
            res = await session.execute(stmt)
            return res.scalars().all()
        
    @classmethod
    async def add_host(cls, ip: str):
        async with async_session_factory() as session:
            stmt = insert(HostsOrm).values(
                ip = ip
            )
            await session.execute(stmt)
            await session.commit()