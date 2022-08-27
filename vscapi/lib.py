from __future__ import annotations

from ctypedffi import Library, Pointer

from .vsapi import VSAPI

__all__ = [
    'VapourSynthLib'
]


class VapourSynthLib(Library, lib='vapoursynth'):
    @staticmethod
    def getVapourSynthAPI(version: int, /) -> Pointer[VSAPI]:
        ...
