import json
from typing import Any, Optional
from uuid import uuid4

from wkflws.events import Event
from wkflws.http import http_method, Request, Response
from wkflws.triggers.webhook import WebhookTrigger

from .. import __identifier__, __version__


async def process_webhook_request(
    request: Request, response: Response
) -> Optional[Event]:
    """Accept and process an HTTP request returning a event for the bus."""

    identifier = str(uuid4())
    data = json.loads(request.body)

    return Event(identifier, request.headers, data)


async def accept_event(event: Event) -> tuple[Optional[str], dict[str, Any]]:
    """Accept and process data from the event bus."""
    return "wkflws_passthru.triggers.passthru", event.data


webhook = WebhookTrigger(
    client_identifier=__identifier__,
    client_version=__version__,
    process_func=accept_event,
    routes=(
        (
            (http_method.POST,),
            "/webhook/passthru/",
            process_webhook_request,
        ),
    ),
)
