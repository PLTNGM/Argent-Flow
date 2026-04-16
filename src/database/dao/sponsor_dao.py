from sqlalchemy import insert, select
from sqlalchemy.dialects.postgresql import insert
from src.database.database import async_session_factory
from src.database.model import SponsorSubOrm

class SponsorDaoOrm:
    @classmethod
    async def select_all_sponsor(cls):
        async with async_session_factory() as session:
            stmt = select(SponsorSubOrm)
            res = await session.execute(stmt)
            return res.scalars().all()