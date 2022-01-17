from typing import List, Optional

from fastapi import APIRouter, Depends
from ..models.operations import Operation, OperationKind
from ..services.operations import OperationsService

router = APIRouter(
    prefix='/operations'
)


@router.get('/', response_model=List[Operation])
def get_operations(
        kind: Optional[OperationKind] = None,
        service: OperationsService = Depends()
):
    return service.get_list()
