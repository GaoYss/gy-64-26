from fastapi import APIRouter

from app.schemas.rectifications import Rectification, RectificationCreate, RectificationUpdate
from app.services.rectifications import rectification_service

router = APIRouter(prefix="/api/rectifications", tags=["rectifications"])


@router.get("", response_model=list[Rectification])
def list_rectifications(inspection_id: int | None = None, project_id: int | None = None) -> list[dict]:
    if inspection_id is not None:
        return rectification_service.list_by_inspection(inspection_id)
    if project_id is not None:
        return rectification_service.list_by_project(project_id)
    return rectification_service.list()


@router.post("", response_model=Rectification, status_code=201)
def create_rectification(payload: RectificationCreate) -> dict:
    return rectification_service.create(payload)


@router.patch("/{rectification_id}", response_model=Rectification)
def update_rectification(rectification_id: int, payload: RectificationUpdate) -> dict:
    return rectification_service.update(rectification_id, payload)
