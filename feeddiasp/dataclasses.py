from typing import List

from dataclasses import dataclass, field


@dataclass
class Post:
    """ Dataclass to store a post.
    """
    title: str = ""
    content: str = ""
    link: str = ""
    id: str = None
    tags: List[str] = field(default_factory=list)
