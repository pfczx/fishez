from sqlmodel import SQLModel, Field

class Flashcards(SQLModel, table=True):
    id: int = Field(primary_key=True)
    title: str = Field(max_length=100)
    flashcards_set : dict[str, str] = Field(max_items=999)