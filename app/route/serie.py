from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.serie import SerieModel
from app.schema.serie import SerieSchema

serie = APIRouter()

@serie.post("/")
async def criar_serie(dados: SerieSchema, db: Session = Depends(get_db)):
    nova_serie = SerieModel(**dados.model_dump())
    db.add(nova_serie)
    db.commit()
    db.refresh(nova_serie)
    return nova_serie

@serie.get("/series")
async def listar_series(db: Session = Depends(get_db)):
    return db.query(SerieModel).all()

@serie.put("/update/{id}")
async def atualizar_serie(id: int, dados: SerieSchema, db: Session = Depends(get_db)):
    serie_api = db.query(SerieModel).filter(SerieModel.id == id).first()
    if not serie_api:
        raise HTTPException(status_code=404, detail="Série não encontrada")
    update_data = dados.dict(exclude_unset=True)
    
    for chave, valor in update_data.items():
        setattr(serie_api, chave, valor)
    db.add(serie_api)
    db.commit()
    db.refresh(serie_api)
    return {"message": "Série atualizada com sucesso", "serie": serie_api}

@serie.delete("/series/{id}")
async def deletar_serie(id: int, db: Session = Depends(get_db)):
    serie_api = db.query(SerieModel).filter(SerieModel.id == id).first()
    if not serie_api:
        raise HTTPException(status_code=404, detail="Série não encontrada")
    db.delete(serie_api)
    db.commit()
    return {"message": "Série removida!"}