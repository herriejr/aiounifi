"""DPI Restrictions as part of a UniFi network."""


from ..models.dpi_restriction_group import (
    DPIRestrictionGroup,
    DpiRestrictionGroupListRequest,
)
from ..models.message import MessageKey
from .api_handlers import APIHandler


class DPIRestrictionGroups(APIHandler[DPIRestrictionGroup]):
    """Represents DPI Group configurations."""

    obj_id_key = "_id"
    path = ""
    item_cls = DPIRestrictionGroup
    process_messages = (MessageKey.DPI_GROUP_ADDED, MessageKey.DPI_GROUP_UPDATED)
    remove_messages = (MessageKey.DPI_GROUP_REMOVED,)
    api_request = DpiRestrictionGroupListRequest.create()
