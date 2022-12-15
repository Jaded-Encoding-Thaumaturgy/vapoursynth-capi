from __future__ import annotations

from typing import TYPE_CHECKING

from ctypedffi import OpaqueStruct, Pointer, String, Struct, as_cfunc, get_string_buff
from ctypedffi.ctypes import VoidReturn, py_object, c_int64, c_uint64, c_void_p
from vapoursynth import Core, _CoreProxy

if TYPE_CHECKING:
    from .vsapi import VSAPI
else:
    VSAPI = None


__all__ = [
    'VSFrame',
    'VSNode',
    'VSCore',
    'VSPlugin',
    'VSPluginFunction',
    'VSFunction',
    'VSMap',
    'VSLogHandle',
    'VSFrameContext',

    'VSCoreInfo',
    'VSVideoInfo',
    'VSAudioInfo',

    'VSFilterDependency',

    'VSGetVapourSynthAPI',
    'VSPublicFunction',
    'VSFreeFunctionData',
    'VSFilterGetFrame',
    'VSFilterFree',
    'VSFrameDoneCallback',
    'VSLogHandler',
    'VSLogHandlerFree',

    'VSPLUGINAPI',
    'VSInitPlugin',

    'VSSCRIPTAPI',
    'VSScript'
]


@Struct.annotate
class VSFrame(OpaqueStruct):
    ...


@Struct.annotate
class VSNode(OpaqueStruct):
    @staticmethod
    def from_map(
        outmap: VSMap | Pointer[VSMap], vsapi: VSAPI,
        key: str = 'clip', idx: int = 0, err_length: int = 1024
    ) -> Pointer[VSNode]:
        if isinstance(outmap, VSMap):
            outmap = Pointer(outmap)

        errorMsg, _ = get_string_buff(err_length)

        invokeError = vsapi.mapGetError(outmap)
        if invokeError:
            raise ValueError(invokeError)

        error = Pointer[int]()
        clip = vsapi.mapGetNode(outmap, key, idx, error)

        if errorMsg.value or error:
            raise ValueError(errorMsg.value or 'An error occured!')

        return clip


@Struct.annotate
class VSCore(OpaqueStruct):
    @staticmethod
    def from_cythonlib(vsapi: VSAPI | Pointer[VSAPI], core: Core | _CoreProxy | None = None) -> Pointer[VSCore]:
        from .vsapi import VSAPI

        if not isinstance(vsapi, VSAPI):
            vsapi = vsapi.contents

        if isinstance(core, _CoreProxy):
            core = core.core  # type: ignore
        elif not core:
            from vapoursynth import core as _core
            core = _core.core

        try:
            from vapoursynth import get_current_environment
            core_ptr = get_current_environment().env().get_core_ptr().value  # type: ignore
        except NameError:
            core_ptr = id(core)

            while True:
                try:
                    t_core = Pointer[VSCore].from_address(core_ptr)
                    vsapi.getPluginByNamespace('std', t_core)
                    break
                except OSError:
                    core_ptr += 8

        return Pointer[VSCore].from_address(core_ptr)


@Struct.annotate
class VSPlugin(OpaqueStruct):
    ...


@Struct.annotate
class VSPluginFunction(OpaqueStruct):
    ...


@Struct.annotate
class VSFunction(OpaqueStruct):
    ...


@Struct.annotate
class VSMap(OpaqueStruct):
    ...


@Struct.annotate
class VSLogHandle(OpaqueStruct):
    ...


@Struct.annotate
class VSFrameContext(OpaqueStruct):
    ...


@Struct.annotate
class VSVideoFormat(Struct):
    colorFamily: int
    sampleType: int
    bitsPerSample: int
    bytesPerSample: int
    subSamplingW: int
    subSamplingH: int
    numPlanes: int


@Struct.annotate
class VSAudioFormat(Struct):
    sampleType: int
    bitsPerSample: int
    bytesPerSample: int
    numChannels: int
    channelLayout: c_uint64


@Struct.annotate
class VSCoreInfo(Struct):
    versionString: String
    core: int
    api: int
    numThreads: int
    maxFramebufferSize: c_int64
    usedFramebufferSize: c_int64


@Struct.annotate
class VSVideoInfo(Struct):
    format: VSVideoFormat
    fpsNum: c_int64
    fpsDen: c_int64
    width: int
    height: int
    numFrames: int


@Struct.annotate
class VSAudioInfo(Struct):
    format: VSAudioFormat
    sampleRate: int
    numSamples: c_int64
    numFrames: int


@Struct.annotate
class VSFilterDependency(Struct):
    source: Pointer[VSNode]
    requestPattern: int


@as_cfunc
def VSGetVapourSynthAPI(version: int, /) -> Pointer[VSAPI]:
    ...


@as_cfunc
def VSPublicFunction(
    inmap: Pointer[VSMap], outmap: Pointer[VSMap], userData: c_void_p, core: Pointer[VSCore], vsapi: Pointer[VSAPI], /,
) -> VoidReturn:
    ...


@as_cfunc
def VSFreeFunctionData(userData: c_void_p, /) -> VoidReturn:
    ...


@as_cfunc
def VSFilterGetFrame(
    n: int, activationReason: int, instanceData: c_void_p, frameData: Pointer[c_void_p],
    frameCtx: Pointer[VSFrameContext], core: Pointer[VSCore], vsapi: Pointer[VSAPI], /,
) -> Pointer[VSFrame]:
    ...


@as_cfunc
def VSFilterFree(instanceData: c_void_p, core: Pointer[VSCore], vsapi: Pointer[VSAPI], /) -> VoidReturn:
    ...


@as_cfunc
def VSFrameDoneCallback(
    userData: c_void_p, f: Pointer[VSFrame], n: int, node: Pointer[VSNode], errorMsg: String, /,
) -> VoidReturn:
    ...


@as_cfunc
def VSLogHandler(msgType: int, msg: String, userData: c_void_p, /) -> VoidReturn:
    ...


@as_cfunc
def VSLogHandlerFree(userData: c_void_p, /) -> VoidReturn:
    ...


class VSPLUGINAPI(Struct):
    @staticmethod
    def getAPIVersion() -> int:
        ...

    @staticmethod
    def configPlugin(
        identifier: String, pluginNamespace: String, name: String, pluginVersion: int,
        apiVersion: int, flags: int, plugin: Pointer[VSPlugin], /,
    ) -> int:
        ...

    @staticmethod
    def registerFunction(
        name: String, args: String, returnType: String, argsFunc: VSPublicFunction,
        functionData: c_void_p, plugin: Pointer[VSPlugin], /,
    ) -> int:
        ...


@as_cfunc
def VSInitPlugin(plugin: Pointer[VSPlugin], vspapi: Pointer[VSPLUGINAPI], /) -> VoidReturn:
    ...


class VSScript(Struct):
    pyenvdict: py_object
    errstr: c_void_p
    core: VSCore
    id: int
    exitCode: int
    setCWD: int


class VSSCRIPTAPI(Struct):
    @staticmethod
    def getAPIVersion() -> int:
        ...

    @staticmethod
    def getVSAPI(version: int, /) -> Pointer[VSAPI]:
        ...

    @staticmethod
    def createScript(core: Pointer[VSCore], /) -> Pointer[VSScript]:
        ...

    @staticmethod
    def getCore(handle: Pointer[VSScript], /) -> Pointer[VSCore]:
        ...

    @staticmethod
    def evaluateBuffer(handle: Pointer[VSScript], buffer: str, scriptFilename: str, /) -> int:
        ...

    @staticmethod
    def evaluateFile(handle: Pointer[VSScript], scriptFilename: str, /) -> int:
        ...

    @staticmethod
    def getError(handle: Pointer[VSScript], /) -> str:
        ...

    @staticmethod
    def getExitCode(handle: Pointer[VSScript], /) -> int:
        ...

    @staticmethod
    def getVariable(handle: Pointer[VSScript], name: str, dst: Pointer[VSMap], /) -> int:
        ...

    @staticmethod
    def setVariables(handle: Pointer[VSScript], vars: Pointer[VSMap], /) -> int:
        ...

    @staticmethod
    def getOutputNode(handle: Pointer[VSScript], index: int, /) -> Pointer[VSNode]:
        ...

    @staticmethod
    def getOutputAlphaNode(handle: Pointer[VSScript], index: int, /) -> Pointer[VSNode]:
        ...

    @staticmethod
    def getAltOutputMode(handle: Pointer[VSScript], index: int, /) -> int:
        ...

    @staticmethod
    def freeScript(handle: Pointer[VSScript], /) -> None:
        ...

    @staticmethod
    def evalSetWorkingDir(handle: Pointer[VSScript], setCWD: int, /) -> None:
        ...
