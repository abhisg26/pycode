## Immediately Invoked Function Expression

from datetime import datetime


@lambda _: _()
def func() -> str:
    time_text: str = f'Started at : {datetime.now():%H:%M:%S}'
    print(time_text)
    return time_text


print(func)