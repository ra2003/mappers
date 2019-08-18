from typing import Any, Tuple

from .._types import EntityFactory, Fields
from . import attrs, dataclasses, pydantic


def entity_fields_factory(entity):
    # type: (Any) -> Tuple[Fields, EntityFactory]
    if attrs.is_attrs(entity):
        fields = attrs.get_fields(entity)
        factory = attrs.get_factory(fields, entity)
        return fields, factory
    elif dataclasses.is_dataclass(entity):
        fields = dataclasses.get_fields(entity)
        factory = dataclasses.get_factory(fields, entity)
        return fields, factory
    elif pydantic.is_pydantic(entity):
        fields = pydantic.get_fields(entity)
        factory = pydantic.get_factory(fields, entity)
        return fields, factory
    else:
        raise Exception