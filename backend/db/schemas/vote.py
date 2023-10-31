from pydantic import BaseModel

# Properties to receive on voter creation
class VoteCreate(BaseModel):
    id_voter: int
    id_candidate: int
    id_candidature: int


# Properties to receive on voter update
class VoteUpdate(BaseModel):
    pass


# Properties shared by models stored in DB
class VoteInDBBase(BaseModel):
    id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Vote(VoteInDBBase):
    pass


# Properties properties stored in DB
class VoteInDB(VoteInDBBase):
    pass