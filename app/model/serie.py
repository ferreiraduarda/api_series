from sqlalchemy import Column, Integer, String
from app.database import Base

class SerieModel(Base):
    __tablename__ = "series"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(255), nullable=False)
    descricao = Column(String(255), nullable=False)
    ano_lancamento = Column(Integer, nullable=False)