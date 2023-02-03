# Stubs for oslo_i18n._factory (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class TranslatorFactory:
    domain: Any = ...
    localedir: Any = ...
    def __init__(self, domain: Any, localedir: Optional[Any] = ...) -> None: ...
    @property
    def primary(self) -> ty.Callable[str]: ...
    @property
    def contextual_form(self): ...
    @property
    def plural_form(self): ...
    @property
    def log_info(self): ...
    @property
    def log_warning(self): ...
    @property
    def log_error(self): ...
    @property
    def log_critical(self): ...
