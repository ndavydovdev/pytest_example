from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List, Optional


@dataclass
class AnyDataModelName:
    b: List[str]
    a: Optional[int] = None
    c: Optional[datetime] = None

    def do_some_stuff(self, any_param: int) -> bool:
        if self.a is not None:
            return self.a == any_param
        return False

    def do_any_other_stuff(self, days_timedelta: int) -> bool:
        if self.c is None:
            return False
        if self.c + timedelta(days=days_timedelta) <= datetime(2020, 1, 1):
            return True
        return False

    def do_some_extra_stuff(self) -> str:
        if self.a is None:
            raise ValueError('a is None')
        for index, item in enumerate(self.b):
            self.b[index] = f'{item}_{index}_{self.a}'
        return ','.join(self.b)
