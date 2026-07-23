from pydantic import BaseModel, Field, field_validator, computed_field

# TODO: Create Booking model
# Fields:
# - user_id: int
# - room_id: int
# - nights: int (must be >=1)
# - rate_per_night: float
# Also, add computed field: total_amount = nights * rate_per_night

class Booking(BaseModel):
    user_id : int
    room_id: int
    nights : int = Field(
        ...,
        gt = 0,
        description = "Number of nights must be atleast 1"
    )
    rate_per_night : float = Field(
        ...,
        gt = 0,
        description = "Rate per night must be atleast 1"
    )


    @computed_field
    @property
    def total_amount(self) -> float :
        return self.nights * self.rate_per_night
    

room = Booking(
    user_id  = 1,
    room_id = 1,
    nights =2,
    rate_per_night = 10   
)

print(room)
print(room.total_amount)