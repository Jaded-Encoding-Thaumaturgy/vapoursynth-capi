from __future__ import annotations

from ctypedffi import Pointer, Struct, with_signature
from ctypedffi.ctypes import StrType, c_char_p, c_float, c_int64, c_ptrdiff_t, c_uint8, c_uint32, c_uint64, c_void_p

from .structs import (
    VSAudioFormat, VSAudioInfo, VSCore, VSCoreInfo, VSFilterDependency, VSFilterFree, VSFilterGetFrame, VSFrame,
    VSFrameContext, VSFrameDoneCallback, VSFreeFunctionData, VSFunction, VSLogHandle, VSLogHandler, VSLogHandlerFree,
    VSMap, VSNode, VSPlugin, VSPluginFunction, VSPublicFunction, VSVideoFormat, VSVideoInfo
)

__all__ = [
    'VSAPI'
]


class VSAPI(Struct):
    @staticmethod
    def createVideoFilter(
        out: Pointer[VSMap], name: StrType, vi: Pointer[VSVideoInfo], getFrame: VSFilterGetFrame, free: VSFilterFree,
        filterMode: int, dependencies: Pointer[VSFilterDependency], numDeps: int, instanceData: c_void_p,
        core: Pointer[VSCore], /,
    ) -> c_void_p:
        ...

    @staticmethod
    def createVideoFilter2(
        name: StrType, vi: Pointer[VSVideoInfo], getFrame: VSFilterGetFrame, free: VSFilterFree, filterMode: int,
        dependencies: Pointer[VSFilterDependency], numDeps: int, instanceData: c_void_p, core: Pointer[VSCore], /,
    ) -> Pointer[VSNode]:
        ...

    @staticmethod
    def createAudioFilter(
        out: Pointer[VSMap], name: StrType, ai: Pointer[VSAudioInfo], getFrame: VSFilterGetFrame, free: VSFilterFree,
        filterMode: int, dependencies: Pointer[VSFilterDependency], numDeps: int, instanceData: c_void_p,
        core: Pointer[VSCore], /,
    ) -> c_void_p:
        ...

    @staticmethod
    def createAudioFilter2(
        name: StrType, ai: Pointer[VSAudioInfo], getFrame: VSFilterGetFrame, free: VSFilterFree, filterMode: int,
        dependencies: Pointer[VSFilterDependency], numDeps: int, instanceData: c_void_p, core: Pointer[VSCore], /,
    ) -> Pointer[VSNode]:
        ...

    @staticmethod
    def setLinearFilter(node: Pointer[VSNode], /) -> int:
        ...

    @staticmethod
    def setCacheMode(node: Pointer[VSNode], mode: int, /) -> c_void_p:
        ...

    @staticmethod
    def setCacheOptions(node: Pointer[VSNode], fixedSize: int, maxSixe: int, maxHistorySize: int, /) -> c_void_p:
        ...

    @staticmethod
    def freeNode(node: Pointer[VSNode], /) -> c_void_p:
        ...

    @staticmethod
    def addNodeRef(node: Pointer[VSNode], /) -> Pointer[VSNode]:
        ...

    @staticmethod
    def getNodeType(node: Pointer[VSNode], /) -> int:  # returns VSMediaType
        ...

    @staticmethod
    def getVideoInfo(node: Pointer[VSNode], /) -> Pointer[VSVideoInfo]:
        ...

    @staticmethod
    def getAudioInfo(node: Pointer[VSNode], /) -> Pointer[VSAudioInfo]:
        ...

    @staticmethod
    def newVideoFrame(
        format: Pointer[VSVideoFormat], width: int, height: int, propSrc: Pointer[VSFrame], core: Pointer[VSCore], /,
    ) -> Pointer[VSFrame]:
        ...

    @staticmethod
    def newVideoFrame2(
        format: Pointer[VSVideoFormat], width: int, height: int, planeSrc: Pointer[Pointer[VSFrame]],
        planes: Pointer[int], propSrc: Pointer[VSFrame], core: Pointer[VSCore], /,
    ) -> Pointer[VSFrame]:
        ...

    @staticmethod
    def newAudioFrame(
        format: Pointer[VSAudioFormat], numSamples: int, propSrc: Pointer[VSFrame], core: Pointer[VSCore], /,
    ) -> Pointer[VSFrame]:
        ...

    @staticmethod
    def newAudioFrame2(
        format: Pointer[VSAudioFormat], numSamples: int, channelSrc: Pointer[Pointer[VSFrame]],
        channels: Pointer[int], propSrc: Pointer[VSFrame], core: Pointer[VSCore], /,
    ) -> Pointer[VSFrame]:
        ...

    @staticmethod
    def freeFrame(f: Pointer[VSFrame], /) -> c_void_p:
        ...

    @staticmethod
    def addFrameRef(f: Pointer[VSFrame], /) -> Pointer[VSFrame]:
        ...

    @staticmethod
    def copyFrame(f: Pointer[VSFrame], core: Pointer[VSCore], /) -> Pointer[VSFrame]:
        ...

    @staticmethod
    def getFramePropertiesRO(f: Pointer[VSFrame], /) -> Pointer[VSMap]:
        ...

    @staticmethod
    def getFramePropertiesRW(f: Pointer[VSFrame], /) -> Pointer[VSMap]:
        ...

    @staticmethod
    def getStride(f: Pointer[VSFrame], plane: int, /) -> c_ptrdiff_t:
        ...

    @staticmethod
    def getReadPtr(f: Pointer[VSFrame], plane: int, /) -> Pointer[c_uint8]:
        ...

    @staticmethod
    def getWritePtr(f: Pointer[VSFrame], plane: int, /) -> Pointer[c_uint8]:
        ...

    @staticmethod
    def getVideoFrameFormat(f: Pointer[VSFrame], /) -> Pointer[VSVideoFormat]:
        ...

    @staticmethod
    def getAudioFrameFormat(f: Pointer[VSFrame], /) -> Pointer[VSAudioFormat]:
        ...

    @staticmethod
    def getFrameType(f: Pointer[VSFrame], /) -> int:  # returns VSMediaType
        ...

    @staticmethod
    def getFrameWidth(f: Pointer[VSFrame], plane: int, /) -> int:
        ...

    @staticmethod
    def getFrameHeight(f: Pointer[VSFrame], plane: int, /) -> int:
        ...

    @staticmethod
    def getFrameLength(f: Pointer[VSFrame], /) -> int:
        ...

    @staticmethod
    def getVideoFormatName(format: Pointer[VSVideoFormat], buffer: StrType, /) -> int:
        ...

    @staticmethod
    def getAudioFormatName(format: Pointer[VSAudioFormat], buffer: StrType, /) -> int:
        ...

    @staticmethod
    def queryVideoFormat(
        format: Pointer[VSVideoFormat], colorFamily: int, sampleType: int, bitsPerSample: int,
        subSamplingW: int, subSamplingH: int, core: Pointer[VSCore], /,
    ) -> int:
        ...

    @staticmethod
    def queryAudioFormat(
        format: Pointer[VSAudioFormat], sampleType: int, bitsPerSample: int,
        channelLayout: c_uint64, core: Pointer[VSCore], /,
    ) -> int:
        ...

    @staticmethod
    def queryVideoFormatID(
        colorFamily: int, sampleType: int, bitsPerSample: int,
        subSamplingW: int, subSamplingH: int, core: Pointer[VSCore], /,
    ) -> c_uint32:
        ...

    @staticmethod
    def getVideoFormatByID(format: Pointer[VSVideoFormat], id: c_uint32, core: Pointer[VSCore], /) -> int:
        ...

    @staticmethod
    def getFrame(n: int, node: Pointer[VSNode], errorMsg: StrType, bugSize: int, /) -> Pointer[VSFrame]:
        ...

    @staticmethod
    def getFrameAsync(
        n: int, node: Pointer[VSNode], callback: VSFrameDoneCallback, userData: c_void_p, /,
    ) -> c_void_p:
        ...

    @staticmethod
    def getFrameFilter(n: int, node: Pointer[VSNode], frameCtx: Pointer[VSFrameContext], /) -> Pointer[VSFrame]:
        ...

    @staticmethod
    def requestFrameFilter(n: int, node: Pointer[VSNode], frameCtx: Pointer[VSFrameContext], /) -> c_void_p:
        ...

    @staticmethod
    def releaseFrameEarly(node: Pointer[VSNode], n: int, frameCtx: Pointer[VSFrameContext], /) -> c_void_p:
        ...

    @staticmethod
    def cacheFrame(frame: Pointer[VSFrame], n: int, frameCtx: Pointer[VSFrameContext], /) -> c_void_p:
        ...

    @staticmethod
    def setFilterError(errorMessage: StrType, frameCtx: Pointer[VSFrameContext], /) -> c_void_p:
        ...

    @staticmethod
    def createFunction(
        func: VSPublicFunction, userData: c_void_p, free: VSFreeFunctionData, core: Pointer[VSCore], /,
    ) -> Pointer[VSFunction]:
        ...

    @staticmethod
    def freeFunction(f: Pointer[VSFunction], /) -> c_void_p:
        ...

    @staticmethod
    def addFunctionRef(f: Pointer[VSFunction], /) -> Pointer[VSFunction]:
        ...

    @staticmethod
    def callFunction(func: Pointer[VSFunction], inmap: Pointer[VSMap], outmap: Pointer[VSMap], /) -> c_void_p:
        ...

    @staticmethod
    def createMap() -> Pointer[VSMap]:
        ...

    @staticmethod
    def freeMap(map: Pointer[VSMap], /) -> c_void_p:
        ...

    @staticmethod
    def clearMap(map: Pointer[VSMap], /) -> c_void_p:
        ...

    @staticmethod
    def copyMap(src: Pointer[VSMap], dst: Pointer[VSMap], /) -> c_void_p:
        ...

    @staticmethod
    def mapSetError(map: Pointer[VSMap], errorMessage: StrType, /) -> c_void_p:
        ...

    @staticmethod
    def mapGetError(map: Pointer[VSMap], /) -> c_char_p:
        ...

    @staticmethod
    def mapNumKeys(map: Pointer[VSMap], /) -> int:
        ...

    @staticmethod
    def mapGetKey(map: Pointer[VSMap], index: int, /) -> c_char_p:
        ...

    @staticmethod
    def mapDeleteKey(map: Pointer[VSMap], key: StrType, /) -> int:
        ...

    @staticmethod
    def mapNumElements(map: Pointer[VSMap], key: StrType, /) -> int:
        ...

    @staticmethod
    def mapGetType(map: Pointer[VSMap], key: StrType, /) -> int:
        ...

    @staticmethod
    def mapSetEmpty(map: Pointer[VSMap], key: StrType, type: int, /) -> int:
        ...

    @staticmethod
    @with_signature(res_type=c_int64)
    def mapGetInt(map: Pointer[VSMap], key: StrType, index: int, error: Pointer[int], /) -> int:
        ...

    @staticmethod
    def mapGetIntSaturated(map: Pointer[VSMap], key: StrType, index: int, error: Pointer[int], /) -> int:
        ...

    @staticmethod
    @with_signature(res_type=c_int64)
    def mapGetIntArray(map: Pointer[VSMap], key: StrType, error: Pointer[int], /) -> Pointer[int]:
        ...

    @staticmethod
    @with_signature(i=c_int64)
    def mapSetInt(map: Pointer[VSMap], key: StrType, i: int, append: int, /) -> int:
        ...

    @staticmethod
    @with_signature(i=Pointer[c_int64])
    def mapSetIntArray(map: Pointer[VSMap], key: StrType, i: Pointer[int], size: int, /) -> int:
        ...

    @staticmethod
    def mapGetFloat(map: Pointer[VSMap], key: StrType, index: int, error: Pointer[int], /) -> float:
        ...

    @staticmethod
    def mapGetFloatSaturated(map: Pointer[VSMap], key: StrType, index: int, error: Pointer[int], /) -> c_float:
        ...

    @staticmethod
    def mapGetFloatArray(map: Pointer[VSMap], key: StrType, error: Pointer[int], /) -> Pointer[float]:
        ...

    @staticmethod
    def mapSetFloat(map: Pointer[VSMap], key: StrType, d: float, append: int, /) -> int:
        ...

    @staticmethod
    def mapSetFloatArray(map: Pointer[VSMap], key: StrType, d: Pointer[float], size: int, /) -> int:
        ...

    @staticmethod
    def mapGetData(map: Pointer[VSMap], key: StrType, index: int, error: Pointer[int], /) -> c_char_p:
        ...

    @staticmethod
    def mapGetDataSize(map: Pointer[VSMap], key: StrType, index: int, error: Pointer[int], /) -> int:
        ...

    @staticmethod
    def mapGetDataTypeHint(map: Pointer[VSMap], key: StrType, index: int, error: Pointer[int], /) -> int:
        ...

    @staticmethod
    def mapSetData(map: Pointer[VSMap], key: StrType, data: StrType, size: int, type: int, append: int, /) -> int:
        ...

    @staticmethod
    def mapGetNode(map: Pointer[VSMap], key: StrType, index: int, error: Pointer[int], /) -> Pointer[VSNode]:
        ...

    @staticmethod
    def mapSetNode(map: Pointer[VSMap], key: StrType, node: Pointer[VSNode], append: int, /) -> int:
        ...

    @staticmethod
    def mapConsumeNode(map: Pointer[VSMap], key: StrType, node: Pointer[VSNode], append: int, /) -> int:
        ...

    @staticmethod
    def mapGetFrame(map: Pointer[VSMap], key: StrType, index: int, error: Pointer[int], /) -> Pointer[VSFrame]:
        ...

    @staticmethod
    def mapSetFrame(map: Pointer[VSMap], key: StrType, f: Pointer[VSFrame], append: int, /) -> int:
        ...

    @staticmethod
    def mapConsumeFrame(map: Pointer[VSMap], key: StrType, f: Pointer[VSFrame], append: int, /) -> int:
        ...

    @staticmethod
    def mapGetFunction(map: Pointer[VSMap], key: StrType, index: int, error: Pointer[int], /) -> Pointer[VSFunction]:
        ...

    @staticmethod
    def mapSetFunction(map: Pointer[VSMap], key: StrType, func: Pointer[VSFunction], append: int, /) -> int:
        ...

    @staticmethod
    def mapConsumeFunction(map: Pointer[VSMap], key: StrType, func: Pointer[VSFunction], append: int, /) -> int:
        ...

    @staticmethod
    def registerFunction(
        name: StrType, args: StrType, returnType: StrType, argsFunc: VSPublicFunction,
        functionData: c_void_p, plugin: Pointer[VSPlugin], /,
    ) -> int:
        ...

    @staticmethod
    def getPluginByID(identifier: StrType, core: Pointer[VSCore], /) -> Pointer[VSPlugin]:
        ...

    @staticmethod
    def getPluginByNamespace(ns: StrType, core: Pointer[VSCore], /) -> Pointer[VSPlugin]:
        ...

    @staticmethod
    def getNextPlugin(plugin: Pointer[VSPlugin], core: Pointer[VSCore], /) -> Pointer[VSPlugin]:
        ...

    @staticmethod
    def getPluginName(plugin: Pointer[VSPlugin], /) -> c_char_p:
        ...

    @staticmethod
    def getPluginID(plugin: Pointer[VSPlugin], /) -> c_char_p:
        ...

    @staticmethod
    def getPluginNamespace(plugin: Pointer[VSPlugin], /) -> c_char_p:
        ...

    @staticmethod
    def getNextPluginFunction(
        func: Pointer[VSPluginFunction], plugin: Pointer[VSPlugin], /,
    ) -> Pointer[VSPluginFunction]:
        ...

    @staticmethod
    def getPluginFunctionByName(name: StrType, plugin: Pointer[VSPlugin], /) -> Pointer[VSPluginFunction]:
        ...

    @staticmethod
    def getPluginFunctionName(func: Pointer[VSPluginFunction], /) -> c_char_p:
        ...

    @staticmethod
    def getPluginFunctionArguments(func: Pointer[VSPluginFunction], /) -> c_char_p:
        ...

    @staticmethod
    def getPluginFunctionReturnType(func: Pointer[VSPluginFunction], /) -> c_char_p:
        ...

    @staticmethod
    def getPluginPath(plugin: Pointer[VSPlugin], /) -> c_char_p:
        ...

    @staticmethod
    def getPluginVersion(plugin: Pointer[VSPlugin], /) -> int:
        ...

    @staticmethod
    def invoke(plugin: Pointer[VSPlugin], name: StrType, args: Pointer[VSMap], /) -> Pointer[VSMap]:
        ...

    @staticmethod
    def createCore(flags: int, /) -> Pointer[VSCore]:
        ...

    @staticmethod
    def freeCore(core: Pointer[VSCore], /) -> c_void_p:
        ...

    @staticmethod
    @with_signature(bytes=c_int64, res_type=c_int64)
    def setMaxCacheSize(bytes: int, core: Pointer[VSCore], /) -> int:
        ...

    @staticmethod
    def setThreadCount(threads: int, core: Pointer[VSCore], /) -> int:
        ...

    @staticmethod
    def getCoreInfo(core: Pointer[VSCore], info: Pointer[VSCoreInfo], /) -> c_void_p:
        ...

    @staticmethod
    def getAPIVersion() -> int:
        ...

    @staticmethod
    def logMessage(msgType: int, msg: StrType, core: Pointer[VSCore], /) -> c_void_p:
        ...

    @staticmethod
    def addLogHandler(
        handler: VSLogHandler, free: VSLogHandlerFree, userData: c_void_p, core: Pointer[VSCore], /,
    ) -> Pointer[VSLogHandle]:
        ...

    @staticmethod
    def removeLogHandler(handle: Pointer[VSLogHandle], core: Pointer[VSCore], /) -> int:
        ...

    # UNSTABLE API

    @staticmethod
    def getNodeCreationFunctionName(node: Pointer[VSNode], level: int, /) -> str:
        ...

    @staticmethod
    def getNodeCreationFunctionArguments(node: Pointer[VSNode], level: int, /) -> Pointer[VSMap]:
        ...

    @staticmethod
    def getNodeName(node: Pointer[VSNode], /) -> str:
        ...

    @staticmethod
    def getNodeFilterMode(node: Pointer[VSNode], /) -> int:
        ...

    @staticmethod
    def getNodeFilterTime(node: Pointer[VSNode], /) -> int:
        ...

    @staticmethod
    def getNodeDependencies(node: Pointer[VSNode], /) -> Pointer[VSFilterDependency]:
        ...

    @staticmethod
    def getNumNodeDependencies(node: Pointer[VSNode], /) -> int:
        ...
