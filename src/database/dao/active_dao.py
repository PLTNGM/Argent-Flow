from sqlalchemy import insert, select
from sqlalchemy.orm import joinedload
from sqlalchemy.dialects.postgresql import insert
from src.database.database import async_session_factory
from src.database.model import ActiveUserOrm, PortsOrm
from src.database.dao.user_dao import UserDao

class ActiveUserDao:

    @classmethod
    async def assign_port(cls, user_id: int, port_id: int):
        async with async_session_factory() as session:
            stmt = insert(ActiveUserOrm).values(
                user_id=user_id,
                port_id=port_id
            ).on_conflict_do_nothing()
            
            await session.execute(stmt)
            await session.commit()

    @classmethod
    async def get_active_user(cls, user_id: int):
        async with async_session_factory() as session:           
            stmt = (
                select(ActiveUserOrm)
                .options(joinedload(ActiveUserOrm.port))
                .where(ActiveUserOrm.user_id == user_id)
            )
            res = await session.execute(stmt)
            return res.scalar_one_or_none()