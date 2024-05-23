from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, Callable

from ctypedffi import CythonModule, Library, Pointer, with_signature
from ctypedffi.ctypes import c_void_p

from .structs import (
    VSSCRIPTAPI, VSCore, VSCoreT, VSFilterDependency, VSFilterFree, VSFilterGetFrame, VSFrame, VSNode, VSScript
)
from .vsapi import VSAPI
from .vsenums import VSFilterMode

try:
    import vapoursynth
    from vapoursynth import AudioNode, Core, Plugin, RawNode, VideoNode
    from vapoursynth import _CoreProxy as CoreProxy
except ModuleNotFoundError:
    if not TYPE_CHECKING:
        vapoursynth = Plugin = VideoNode = AudioNode = RawNode = Core = CoreProxy = None


__all__ = [
    'VapourSynthLib',
    'VSScriptLib',
    'VSBridge',
    'VPyCythonLib',

    'Plugin',
    'RawNode', 'AudioNode', 'VideoNode',
    'Core', 'CoreProxy'
]


class VapourSynthLib(Library, lib='vapoursynth'):
    @staticmethod
    def getVapourSynthAPI(version: int, /) -> Pointer[VSAPI]:
        ...


class VSScriptLib(Library, lib='vsscript'):
    @staticmethod
    def getVSScriptAPI(version: int, /) -> Pointer[VSSCRIPTAPI]:
        ...


class VSBridge:
    @staticmethod
    def ensure_vscapi(core: Core | CoreProxy | None = None) -> Plugin:
        if vapoursynth is None:
            raise RuntimeError('You are missing the vapoursynth package!')

        if isinstance(core, CoreProxy):
            core = core.core  # type: ignore
        elif not core:
            core = vapoursynth.core.core

        if not hasattr(core, 'vscapi'):
            # core.add_log_handler(lambda t, m: print(f'log type: {t} ({m})'))
            from vapoursynth import Error

            try:
                core.std.LoadPlugin(str((Path(__file__).parent / 'vscapi').resolve()))
            except Error:
                core.std.LoadPlugin(str((Path(__file__).parent.parent / 'lib' / 'vscapi').resolve()))

        return core.vscapi  # type: ignore

    @classmethod
    def getBitBltPtr(cls, core: Core | CoreProxy | None = None) -> int:
        return cls.ensure_vscapi(core).getBitBltPtr()  # type: ignore

    @classmethod
    def getVSCApiPtr(cls, core: Core | CoreProxy | None = None) -> int:
        return cls.ensure_vscapi(core).getVSCApiPtr()  # type: ignore

    @staticmethod
    def as_node(
        node: Pointer[VSNode], vsapi: VSAPI, vscore: Pointer[VSCore], filter_mode: VSFilterMode, video: bool
    ) -> Callable[[VSFilterGetFrame], RawNode]:
        def _wrapper(func: Callable[..., Pointer[VSFrame]]) -> RawNode:
            # we need this so it doesn't get garbage collected
            func.__vscapigetframe = VSFilterGetFrame(func)  # type: ignore

            func.__clip = vsapi.createVideoFilter2(  # type: ignore
                func.__name__, vsapi.getVideoInfo(node), func.__vscapigetframe, VSFilterFree(),  # type: ignore
                filter_mode, Pointer(VSFilterDependency()), 0, c_void_p(), vscore
            )

            func.__cref = vsapi.addNodeRef(func.__clip)  # type: ignore
            # func.__cref = vsapi.addNodeRef(node)

            if video:
                return VSNode.to_cythonlib_vnode(func.__cref)  # type: ignore

            return VSNode.to_cythonlib_anode(func.__cref)  # type: ignore

        return _wrapper

    @classmethod
    def as_vnode(
        cls, node: Pointer[VSNode] | VideoNode,
        vsapi: VSAPI | None = None, vscore: VSCoreT = None,
        filter_mode: VSFilterMode = VSFilterMode.fmParallel
    ) -> Callable[[VSFilterGetFrame], VideoNode]:
        from .lib import RawNode

        if isinstance(node, RawNode):
            node = VSNode.from_cythonlib(node)  # type: ignore

        return cls.as_node(
            node,  # type: ignore
            vsapi if isinstance(vscore, Pointer[VSCore]) else VSAPI.from_cythonlib(),  # type: ignore
            vscore if isinstance(vscore, Pointer[VSCore]) else VSCore.from_cythonlib(vscore),  # type: ignore
            filter_mode, True
        )

    @classmethod
    def as_anode(
        cls, node: Pointer[VSNode] | AudioNode,
        vsapi: VSAPI | None = None, vscore: VSCoreT = None,
        filter_mode: VSFilterMode = VSFilterMode.fmParallel
    ) -> Callable[[VSFilterGetFrame], AudioNode]:
        from .lib import RawNode

        if isinstance(node, RawNode):
            node = VSNode.from_cythonlib(node)  # type: ignore

        return cls.as_node(
            node,  # type: ignore
            vsapi if isinstance(vscore, Pointer[VSCore]) else VSAPI.from_cythonlib(),  # type: ignore
            vscore if isinstance(vscore, Pointer[VSCore]) else VSCore.from_cythonlib(vscore),  # type: ignore
            filter_mode, False
        )


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
