from datetime import date, timedelta

from fastapi import HTTPException, status
from pydantic import BaseModel

from app.data.store import store
from app.services.base import CrudService
from app.services.rectifications import rectification_service
from app.schemas.rectifications import RectificationCreate


class InspectionService(CrudService):
    collection = "inspections"

    def update(self, item_id: int, payload: BaseModel) -> dict:
        update_data = payload.model_dump(exclude_unset=True, mode="json")
        item = store.update_item(self.collection, item_id, update_data)
        if item is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource not found")

        result = item.get("result")
        if result in ("整改", "failed"):
            existing_rectifications = rectification_service.list_by_inspection(item_id)
            if len(existing_rectifications) == 0:
                rectification_data = RectificationCreate(
                    project_id=item["project_id"],
                    project_name=item["project_name"],
                    inspection_id=item["id"],
                    title=f"{item['inspection_type']} - Rectification required",
                    description=item.get("issues") or "Issues found during inspection, rectification required.",
                    responsible="Pending assignment",
                    deadline=date.today() + timedelta(days=7),
                    priority="medium",
                    status="pending",
                    progress="",
                )
                rectification_service.create(rectification_data)

        return item


inspection_service = InspectionService()
