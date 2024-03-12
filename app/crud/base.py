from typing import Any

from sqlalchemy.orm import Session


class CRUDBase:
    def __init__(self, table):
        
        """
        CRUD object with default methods to Create, Read, Update (CRU).

        **Parameters**

        * `table`: A SQLModel table model class
        """

        self.table = table
        
    def create(self, db: Session, obj_in: dict):
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        db_obj = self.table(**update_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(self, db: Session, db_obj: int, obj_in: dict):

        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in update_data:
            if hasattr(db_obj, field):
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    def get(self, db: Session, id: Any):
        statement = db.query(self.table).filter(self.table.id == id).first()
        return statement
    
    def delete(self, db: Session, obj_id: Any):
        obj = self.get(db, obj_id)
        if obj:
            db.delete(obj)
            db.commit()
            return obj
        else:
            return None

