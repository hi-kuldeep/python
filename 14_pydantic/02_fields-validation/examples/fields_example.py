from pydantic import BaseModel
from typing import List, Dict, Optional
class User(BaseModel):
    user_id : int
    items : List[str]
    quantities : Dict[str, int]

