from __future__ import annotations

try:
    import vapoursynth
except ModuleNotFoundError:
    vapoursynth = None  # type: ignore

from ctypedffi import CythonModule, Library, Pointer

from .structs import VSSCRIPTAPI, VSCore, VSNode, VSScript
from .vsapi import VSAPI


__all__ = [
    'VapourSynthLib', 'VSScriptLib', 'VPyCythonLib'
]


class VapourSynthLib(Library, lib='vapoursynth'):
    @staticmethod
    def getVapourSynthAPI(version: int, /) -> Pointer[VSAPI]:
        ...


class VSScriptLib(Library, lib='vsscript'):
    @staticmethod
    def getVSScriptAPI(version: int, /) -> Pointer[VSSCRIPTAPI]:
        ...


class VPyCythonLib(CythonModule, module=vapoursynth):
    @staticmethod
    def vpy4_createScript(se: Pointer[VSScript]) -> int:
        ...

    @staticmethod
    def vpy_evaluateScript(se: Pointer[VSScript], script: str, scriptFilename: str, flags: int) -> int:
        ...

    @staticmethod
    def vpy_evaluateFile(se: Pointer[VSScript], scriptFilename: str, flags: int) -> int:
        ...

    @staticmethod
    def vpy4_evaluateBuffer(se: Pointer[VSScript], buffer: str, scriptFilename: str) -> int:
        ...

    @staticmethod
    def vpy4_evaluateFile(se: Pointer[VSScript], scriptFilename: str) -> int:
        ...

    @staticmethod
    def vpy4_freeScript(se: Pointer[VSScript]) -> None:
        ...

    @staticmethod
    def vpy4_getError(se: Pointer[VSScript]) -> str:
        ...

    @staticmethod
    def vpy4_getOutput(se: Pointer[VSScript], index: int) -> Pointer[VSNode]:
        ...

    @staticmethod
    def vpy4_getAlphaOutput(se: Pointer[VSScript], index: int) -> Pointer[VSNode]:
        ...

    @staticmethod
    def vpy4_getAltOutputMode(se: Pointer[VSScript], index: int) -> int:
        ...

    @staticmethod
    def vpy_clearOutput(se: Pointer[VSScript], index: int) -> int:
        ...

    @staticmethod
    def vpy4_getCore(se: Pointer[VSScript]) -> Pointer[VSCore]:
        ...

    @staticmethod
    def vpy4_getVSAPI(version: int, /) -> Pointer[VSAPI]:
        ...

    @staticmethod
    def vpy4_getVariable() -> int:
        ...

    @staticmethod
    def vpy4_setVariables() -> int:
        ...

    @staticmethod
    def vpy_clearVariable() -> int:
        ...

    @staticmethod
    def vpy_clearEnvironment() -> None:
        ...

    @staticmethod
    def vpy4_initVSScript() -> int:
        ...
