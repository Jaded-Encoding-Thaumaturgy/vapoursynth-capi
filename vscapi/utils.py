from __future__ import annotations


def VS_MAKE_VERSION(major: int, minor: int) -> int:
    return (major << 16) | minor
