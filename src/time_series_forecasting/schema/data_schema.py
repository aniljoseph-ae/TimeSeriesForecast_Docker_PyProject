from pydantic import BaseModel, Field
from typing import List 

class DataFinalModel(BaseModel):
    date: List[str] = Field(..., description="List of dates in YYYY-MM-DD format")
    item: List[str] = Field(..., description="List of sales figures corresponding to the dates")
    quantity: List[int] = Field(..., description="List of product IDs corresponding to the sales data")
    market: List[str] = Field(..., description="List of regions corresponding to the sales data")