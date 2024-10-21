from pydantic import BaseModel


class DocumentsIn(BaseModel):
    shipment_id: int
    document_type: str
    file_path: str
    uploaded_at: str


class Documents(DocumentsIn):
    id: int
