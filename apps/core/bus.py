from collections import defaultdict
from typing import Callable, Any


class EventBus:
    def __init__(self):
        self._handlers: dict[str, list[Callable]] = defaultdict(list)

    def subscribe(self, event: str, handler: Callable[..., Any]) -> None:
        self._handlers[event].append(handler)

    def publish(self, event: str, **payload: Any) -> None:
        for handler in self._handlers.get(event, []):
            handler(**payload)


event_bus = EventBus()
