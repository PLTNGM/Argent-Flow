from sqlalchemy import insert, select
from sqlalchemy.dialects.postgresql import insert
from src.database.database import sync_session_factory, Base, async_session_factory
from src.database.model import UsersOrm, ActiveUserOrm, HostsOrm, PortsOrm, SponsorSubOrm

class UserDao:

    @classmethod
    async def register_user(cls, user_id: int, username: str, name:str):
        async with async_session_factory() as session:
            stmt = insert(UsersOrm).values(
                user_id = user_id,
                username = username,
                name = name
            ).on_conflict_do_update(
                index_elements=['user_id'],
                set_={
                    'username': username,
                    'name': name
                }
            )
            await session.execute(stmt)
            await session.commit()

    @classmethod
    async def select_all_users(cls):
        async with async_session_factory() as session:
            stmt = select(UsersOrm)
            res = await session.execute(stmt)
            return res.scalars().all()
