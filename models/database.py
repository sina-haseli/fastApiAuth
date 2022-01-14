from fastapi.logger import logger
from sqlalchemy.engine.create import create_engine
from sqlalchemy.orm.decl_api import declarative_base
from sqlalchemy.orm.session import sessionmaker

engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost/postgres')
SessionLocal = sessionmaker(autocommit=True, autoflush=False, bind=engine)

Base = declarative_base()

logger.info('Database connected')

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

