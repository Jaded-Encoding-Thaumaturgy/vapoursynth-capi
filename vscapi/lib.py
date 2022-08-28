from __future__ import annotations

try:
    import vapoursynth
except ModuleNotFoundError:
    vapoursynth = None  # type: ignore

from ctypedffi import CythonModule, Library, Pointer, with_signature

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
    @with_signature(name='vpy4_createScript')
    def createScript(se: Pointer[VSScript]) -> int:
        ...

    @staticmethod
    @with_signature(name='vpy_evaluateScript')
    def evaluateScript(se: Pointer[VSScript], script: str, scriptFilename: str, flags: int) -> int:
        ...

    @staticmethod
    @with_signature(name='vpy_evaluateFile')
    def evaluateFileAPI3(se: Pointer[VSScript], scriptFilename: str, flags: int) -> int:
        ...

    @staticmethod
    @with_signature(name='vpy4_evaluateBuffer')
    def evaluateBuffer(se: Pointer[VSScript], buffer: str, scriptFilename: str) -> int:
        ...

    @staticmethod
    @with_signature(name='vpy4_evaluateFile')
    def evaluateFile(se: Pointer[VSScript], scriptFilename: str) -> int:
        ...

    @staticmethod
    @with_signature(name='vpy4_freeScript')
    def freeScript(se: Pointer[VSScript]) -> None:
        ...

    @staticmethod
    @with_signature(name='vpy4_getError')
    def getError(se: Pointer[VSScript]) -> str:
        ...

    @staticmethod
    @with_signature(name='vpy4_getOutput')
    def getOutput(se: Pointer[VSScript], index: int) -> Pointer[VSNode]:
        ...

    @staticmethod
    @with_signature(name='vpy4_getAlphaOutput')
    def getAlphaOutput(se: Pointer[VSScript], index: int) -> Pointer[VSNode]:
        ...

    @staticmethod
    @with_signature(name='vpy4_getAltOutputMode')
    def getAltOutputMode(se: Pointer[VSScript], index: int) -> int:
        ...

    @staticmethod
    @with_signature(name='vpy_clearOutput')
    def clearOutput(se: Pointer[VSScript], index: int) -> int:
        ...

    @staticmethod
    @with_signature(name='vpy4_getCore')
    def getCore(se: Pointer[VSScript]) -> Pointer[VSCore]:
        ...

    @staticmethod
    @with_signature(name='vpy4_getVSAPI')
    def getVSAPI(version: int, /) -> Pointer[VSAPI]:
        ...

    @staticmethod
    @with_signature(name='vpy4_getVariable')
    def getVariable() -> int:
        ...

    @staticmethod
    @with_signature(name='vpy4_setVariables')
    def setVariables() -> int:
        ...

    @staticmethod
    @with_signature(name='vpy_clearVariable')
    def clearVariable() -> int:
        ...

    @staticmethod
    @with_signature(name='vpy_clearEnvironment')
    def clearEnvironment() -> None:
        ...

    @staticmethod
    @with_signature(name='vpy4_initVSScript')
    def initVSScript() -> int:
        ...
