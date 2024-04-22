from dataclasses import dataclass, field
from datetime import datetime
import logging
from typing import Union, Callable


@dataclass
class Sender:
    phone_number: str
    name: str
    #country: str = None
    #max_messages: int = 50

