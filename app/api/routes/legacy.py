from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from app.api.deps import get_current_admin
from app.api.routes.services import create_service, delete_service, list_services, update_service
from app.core.database import get_db
from app.schemas.service import ServiceCreate, ServiceResponse, ServiceUpdate

router = APIRouter(tags=["legacy"])


@router.get("/posts", response_model=list[ServiceResponse])
def legacy_list_services(db: Session = Depends(get_db)):
    return list_services(db=db)


@router.post("/posts", response_model=ServiceResponse, status_code=status.HTTP_201_CREATED)
def legacy_create_service(
    payload: ServiceCreate,
    db: Session = Depends(get_db),
    admin=Depends(get_current_admin),
):
    return create_service(payload=payload, db=db, _=admin)


@router.put("/post/{service_id}", response_model=ServiceResponse)
def legacy_update_service(
    service_id: int,
    payload: ServiceUpdate,
    db: Session = Depends(get_db),
    admin=Depends(get_current_admin),
):
    return update_service(service_id=service_id, payload=payload, db=db, _=admin)


@router.delete("/post/{service_id}", status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
def legacy_delete_service(
    service_id: int,
    db: Session = Depends(get_db),
    admin=Depends(get_current_admin),
):
    return delete_service(service_id=service_id, db=db, _=admin)
