from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase
from sqlalchemy import URL, create_engine, String
from src.config import settings
 
sync_engine = create_engine(
    url=settings.DABASE_URL_SYNC,
    pool_size=5,
    max_overflow=10
)

async_engine = create_async_engine(
    url=settings.DABASE_URL_ASYNC,
    pool_size=5,
    max_overflow=10
)

sync_session_factory = sessionmaker(sync_engine)
async_session_factory = async_sessionmaker(async_engine)

class Base(DeclarativeBase):
    repr_col_num = 3
    repr_col = tuple()
    def __repr__(self):
        cols = []
        for idx, col in enumerate(self.__table__.columns.keys()):
            if col in self.repr_col or idx < self.repr_col_num:
                cols.append(f"{col} = {getattr(self, col)}")

        return f"<{self.__class__.__name__} {','.join(cols)}>"   