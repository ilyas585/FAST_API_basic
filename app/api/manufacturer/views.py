from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.manufacturer import crud
from app.api.manufacturer.schemas import ManufacturerIn, ManufacturerOut
from app.db.session import db_session

router_manufacturer = APIRouter(prefix="/manufacturer", tags=["manufacturer"])


@router_manufacturer.post("", response_model=ManufacturerOut)
def create_manufacturer(manufacturer_in: ManufacturerIn, db: Session = Depends(db_session)) -> ManufacturerOut:
    return crud.Manufacturer(db).create_manufacturer(manufacturer_in)


@router_manufacturer.get("/{manufacturer_id}", response_model=ManufacturerOut)
def get_manufacturer_by_id(manufacturer_id: int, db: Session = Depends(db_session)) -> ManufacturerOut:
    return crud.Manufacturer(db).get_manufacturer_by_id(manufacturer_id)


@router_manufacturer.get("s", response_model=List[ManufacturerOut])
def get_manufacturers(db: Session = Depends(db_session)) -> List[ManufacturerOut]:
    return crud.Manufacturer(db).get_manufacturers()


@router_manufacturer.delete("/{manufacturer_id}")
def delete_manufacturer(manufacturer_id: int, db: Session = Depends(db_session)) -> None:
    return crud.Manufacturer(db).delete_manufacturer(manufacturer_id)


@router_manufacturer.put("/{manufacturer_id}")
def put_manufacturer(manufacturer_id: int, manufacturer_in: ManufacturerIn, db: Session = Depends(db_session)) -> ManufacturerOut:
    return crud.Manufacturer(db).put_manufacturer(manufacturer_id, manufacturer_in)
