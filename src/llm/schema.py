from pydantic import BaseModel, Field
from typing import List, Dict, Any

class passport_info(BaseModel):
    name: str = Field(..., description="The name of the passport"),
    passport_number: str = Field(..., description="The passport number"),
    nationality: str = Field(..., description="The nationality of the passport"),
    date_of_birth: str = Field(..., description="The date of birth of the passport holder"),
    place_of_birth: str = Field(..., description="The place of birth of the passport holder"),
    expiration_date: str = Field(..., description="The expiration date of the passport"),
    issuing_country: str | None = Field(None, description="The country that issued the passport"),
    spouse_name: str | None = Field(None, description="The name of the spouse of the passport holder"),
    father_name: str | None = Field(None, description="The name of the father of the passport holder"),
    mother_name: str | None = Field(None, description="The name of the mother of the passport holder"),