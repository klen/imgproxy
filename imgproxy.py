"""ImageProxy support."""

import base64
import dataclasses as dc
import hashlib
import hmac
from typing import Literal, Union, Optional
from functools import partial


__version__ = '0.2.2'


@dc.dataclass
class ImgProxy:

    """ImageProxy URL."""

    image_url: str
    proxy_host: Optional[str] = None
    key: Optional[str] = dc.field(default=None, repr=False)
    salt: Optional[str] = dc.field(default=None, repr=False)
    resizing_type: Literal['fit', 'fill', 'auto'] = 'auto'
    width: int = 0
    height: int = 0
    gravity: Union[
        Literal['no', 'so', 'ea', 'we', 'noea', 'nowe', 'soea', 'sowe', 'ce', 'sm'], str] = 'ce'
    enlarge: bool = False
    extension: str = ''

    @classmethod
    def factory(cls, **kwargs):
        """Generate ImgProxy objects."""
        return partial(cls, **kwargs)

    def __post_init__(self):
        """Initialize signature options."""
        try:
            self.key: Union[bytes, Literal[False]] = self.key and bytes.fromhex(self.key)
            self.salt: Union[bytes, Literal[False]] = self.salt and bytes.fromhex(self.salt)
        except ValueError:
            raise ValueError(f"Invalid signature parameters: {self.key}, {self.salt}")

    def __str__(self) -> str:
        """Generate default URL."""
        return self.__call__()

    def __call__(self, *advanced: str, **options) -> str:
        """Generate an URL."""
        b64_url = base64.urlsafe_b64encode(self.image_url.encode()).rstrip(b"=").decode()
        if advanced:
            path = "{advanced}/g:{gravity}/rs:{resizing_type}:{width}:{height}:{enlarge}/{b64_url}{extension}".format(  # noqa
                b64_url=b64_url, advanced='/'.join(advanced), **dict({
                    'resizing_type': self.resizing_type,
                    'width': self.width,
                    'height': self.height,
                    'gravity': self.gravity,
                    'enlarge': self.enlarge and '1' or '0',
                    'extension': self.extension and f".{self.extension}" or '',
                }, **options)
            )

        else:
            path = "{resizing_type}/{width}/{height}/{gravity}/{enlarge}/{b64_url}{extension}".format(  # noqa
                b64_url=b64_url, **dict({
                    'resizing_type': self.resizing_type,
                    'width': self.width,
                    'height': self.height,
                    'gravity': self.gravity,
                    'enlarge': self.enlarge and '1' or '0',
                    'extension': self.extension and f".{self.extension}" or '',
                }, **options)
            )

        signature = 'insecure'
        if self.key and self.salt:
            digest = hmac.new(
                self.key, msg=self.salt + path.encode(),  # type: ignore
                digestmod=hashlib.sha256).digest()
            signature = base64.urlsafe_b64encode(digest).rstrip(b"=").decode()

        path = f"/{signature}/{path}"
        if self.proxy_host:
            return f"{self.proxy_host}{path}"

        return path
