from typing import List

from fastapi import Depends
from sqlalchemy.orm import Session

from .. import tables

from ..db import get_session


class OperationsService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_list(self) -> List[tables.Operation]:
        operations = (
            self.session
                .query(tables.Operation)
                .all()
        )
        return operations
