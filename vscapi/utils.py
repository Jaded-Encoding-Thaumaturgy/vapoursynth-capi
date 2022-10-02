from __future__ import annotations

__all__ = [
    'VS_MAKE_VERSION'
]


def VS_MAKE_VERSION(major: int, minor: int) -> int:
    return (major << 16) | minor
