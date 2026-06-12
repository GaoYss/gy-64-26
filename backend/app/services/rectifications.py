from datetime import date

from pydantic import BaseModel

from app.data.store import store
from app.services.base import CrudService


class RectificationService(CrudService):
    collection = "rectifications"

    def create(self, payload: BaseModel) -> dict:
        data = payload.model_dump(mode="json")
        data["created_at"] = str(date.today())
        return store.add_item(self.collection, data)

    def list_by_inspection(self, inspection_id: int) -> list[dict]:
        items = store.list_items(self.collection)
        return [item for item in items if item.get("inspection_id") == inspection_id]

    def list_by_project(self, project_id: int) -> list[dict]:
        items = store.list_items(self.collection)
        return [item for item in items if item.get("project_id") == project_id]


rectification_service = RectificationService()
