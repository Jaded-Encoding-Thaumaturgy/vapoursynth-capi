from __future__ import annotations

import sys
from ctypes import memmove
from math import inf

from ctypedffi import Pointer
from ctypedffi.ctypes import c_ptrdiff_t, c_void_p

from .structs import VSAudioFormat, VSAudioInfo, VSCore, VSVideoFormat, VSVideoInfo
from .vsapi import VSAPI
from .vsenums import VSColorFamily, VSPresetFormat

__all__ = [
    'INT_MAX', 'INT_MIN',
    'FLT_MAX', 'FLT_MIN',

    'VSH_STD_PLUGIN_ID',
    'VSH_RESIZE_PLUGIN_ID',
    'VSH_TEXT_PLUGIN_ID',

    'isConstantVideoFormat',

    'isSameVideoFormat',
    'isSameVideoPresetFormat',
    'isSameVideoInfo',

    'isSameAudioFormat',
    'isSameAudioInfo',

    'int64ToIntS'
]

INT_MAX = sys.maxsize
INT_MIN = -INT_MAX - 1

FLT_MAX = sys.float_info.max
FLT_MIN = sys.float_info.min

VSH_STD_PLUGIN_ID = 'com.vapoursynth.std'
VSH_RESIZE_PLUGIN_ID = 'com.vapoursynth.resize'
VSH_TEXT_PLUGIN_ID = 'com.vapoursynth.text'


def isConstantVideoFormat(vi: VSVideoInfo) -> bool:
    return vi.height > 0 and vi.width > 0 and vi.format.colorFamily != VSColorFamily.cfUndefined


def isSameVideoFormat(v1: VSVideoFormat, v2: VSVideoFormat) -> bool:
    return (
        v1.colorFamily == v2.colorFamily
        and v1.sampleType == v2.sampleType
        and v1.bitsPerSample == v2.bitsPerSample
        and v1.subSamplingW == v2.subSamplingW
        and v1.subSamplingH == v2.subSamplingH
    )


def isSameVideoPresetFormat(
    presetFormat: VSPresetFormat, v: VSVideoFormat, core: Pointer[VSCore], vsapi: VSAPI
) -> bool:
    return vsapi.queryVideoFormatID(
        v.colorFamily, v.sampleType, v.bitsPerSample, v.subSamplingW, v.subSamplingH, core
    ).value == presetFormat


def isSameVideoInfo(v1: VSVideoInfo, v2: VSVideoInfo) -> bool:
    return v1.height == v2.height and v1.width == v2.width and isSameVideoFormat(v1.format, v2.format)


def isSameAudioFormat(a1: VSAudioFormat, a2: VSAudioFormat) -> bool:
    return (
        a1.bitsPerSample == a2.bitsPerSample
        and a1.sampleType == a2.sampleType
        and a1.channelLayout == a2.channelLayout
    )


def isSameAudioInfo(a1: VSAudioInfo, a2: VSAudioInfo) -> bool:
    return a1.sampleRate == a2.sampleRate and isSameAudioFormat(a1.format, a2.format)


def int64ToIntS(i: int) -> int:
    if i > INT_MAX:
        return INT_MAX
    elif i < INT_MIN:
        return INT_MIN

    return i


def doubleToFloatS(d: float) -> float:
    if d is inf:
        return d
    elif d > FLT_MAX:
        return FLT_MAX
    elif d < FLT_MIN:
        return FLT_MIN

    return d


def bitblt(
    dstp: c_void_p, dst_stride: c_ptrdiff_t, srcp: c_void_p, src_stride: c_ptrdiff_t, row_size: int, height: int
) -> None:
    if not height:
        return

    if src_stride == dst_stride and src_stride == row_size:  # type: ignore
        memmove(dstp, srcp, row_size * height)
        return

    srcp8 = srcp.value
    dstp8 = dstp.value

    assert srcp8 and dstp8

    for _ in range(height):
        memmove(dstp8, srcp8, row_size)
        srcp8 += src_stride
        dstp8 += dst_stride


def areValidDimensions(fi: VSVideoFormat, width: int, height: int) -> bool:
    return not (width % (1 << fi.subSamplingW) or height % (1 << fi.subSamplingH))
