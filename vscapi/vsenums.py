from __future__ import annotations

from enum import IntEnum


class VSActivationReason(IntEnum):
    arError = -1
    arInitial = 0
    arAllFramesReady = 1


class VSMessageType(IntEnum):
    mtDebug = 0
    mtInformation = 1
    mtWarning = 2
    mtCritical = 3
    mtFatal = 4


class VSCoreCreationFlags(IntEnum):
    ccfEnableGraphInspection = 1
    ccfDisableAutoLoading = 2
    ccfDisableLibraryUnloading = 4


class VSPluginConfigFlags(IntEnum):
    pcModifiable = 1


class VSDataTypeHint(IntEnum):
    dtUnknown = (-1)
    dtBinary = 0
    dtUtf8 = 1


class VSRequestPattern(IntEnum):
    rpGeneral = 0
    rpNoFrameReuse = 1
    rpStrictSpatial = 2


class VSCacheMode(IntEnum):
    cmAuto = -1
    cmForceDisable = 0
    cmForceEnable = 1


class VSColorFamily(IntEnum):
    cfUndefined = 0
    cfGray = 1
    cfRGB = 2
    cfYUV = 3


class VSSampleType(IntEnum):
    stInteger = 0
    stFloat = 1


class VSPresetFormat(IntEnum):
    pfNone = 0

    pfGray8 = (((((1 << 28) | (0 << 24)) | (8 << 16)) | (0 << 8)) | (0 << 0))
    pfGray9 = (((((1 << 28) | (0 << 24)) | (9 << 16)) | (0 << 8)) | (0 << 0))
    pfGray10 = (((((1 << 28) | (0 << 24)) | (10 << 16)) | (0 << 8)) | (0 << 0))
    pfGray12 = (((((1 << 28) | (0 << 24)) | (12 << 16)) | (0 << 8)) | (0 << 0))
    pfGray14 = (((((1 << 28) | (0 << 24)) | (14 << 16)) | (0 << 8)) | (0 << 0))
    pfGray16 = (((((1 << 28) | (0 << 24)) | (16 << 16)) | (0 << 8)) | (0 << 0))
    pfGray32 = (((((1 << 28) | (0 << 24)) | (32 << 16)) | (0 << 8)) | (0 << 0))
    pfGrayH = (((((1 << 28) | (1 << 24)) | (16 << 16)) | (0 << 8)) | (0 << 0))
    pfGrayS = (((((1 << 28) | (1 << 24)) | (32 << 16)) | (0 << 8)) | (0 << 0))

    pfYUV410P8 = (((((3 << 28) | (0 << 24)) | (8 << 16)) | (2 << 8)) | (2 << 0))
    pfYUV411P8 = (((((3 << 28) | (0 << 24)) | (8 << 16)) | (2 << 8)) | (0 << 0))
    pfYUV440P8 = (((((3 << 28) | (0 << 24)) | (8 << 16)) | (0 << 8)) | (1 << 0))
    pfYUV420P8 = (((((3 << 28) | (0 << 24)) | (8 << 16)) | (1 << 8)) | (1 << 0))
    pfYUV422P8 = (((((3 << 28) | (0 << 24)) | (8 << 16)) | (1 << 8)) | (0 << 0))
    pfYUV444P8 = (((((3 << 28) | (0 << 24)) | (8 << 16)) | (0 << 8)) | (0 << 0))
    pfYUV420P9 = (((((3 << 28) | (0 << 24)) | (9 << 16)) | (1 << 8)) | (1 << 0))
    pfYUV422P9 = (((((3 << 28) | (0 << 24)) | (9 << 16)) | (1 << 8)) | (0 << 0))
    pfYUV444P9 = (((((3 << 28) | (0 << 24)) | (9 << 16)) | (0 << 8)) | (0 << 0))
    pfYUV420P10 = (((((3 << 28) | (0 << 24)) | (10 << 16)) | (1 << 8)) | (1 << 0))
    pfYUV422P10 = (((((3 << 28) | (0 << 24)) | (10 << 16)) | (1 << 8)) | (0 << 0))
    pfYUV444P10 = (((((3 << 28) | (0 << 24)) | (10 << 16)) | (0 << 8)) | (0 << 0))
    pfYUV420P12 = (((((3 << 28) | (0 << 24)) | (12 << 16)) | (1 << 8)) | (1 << 0))
    pfYUV422P12 = (((((3 << 28) | (0 << 24)) | (12 << 16)) | (1 << 8)) | (0 << 0))
    pfYUV444P12 = (((((3 << 28) | (0 << 24)) | (12 << 16)) | (0 << 8)) | (0 << 0))
    pfYUV420P14 = (((((3 << 28) | (0 << 24)) | (14 << 16)) | (1 << 8)) | (1 << 0))
    pfYUV422P14 = (((((3 << 28) | (0 << 24)) | (14 << 16)) | (1 << 8)) | (0 << 0))
    pfYUV444P14 = (((((3 << 28) | (0 << 24)) | (14 << 16)) | (0 << 8)) | (0 << 0))
    pfYUV420P16 = (((((3 << 28) | (0 << 24)) | (16 << 16)) | (1 << 8)) | (1 << 0))
    pfYUV422P16 = (((((3 << 28) | (0 << 24)) | (16 << 16)) | (1 << 8)) | (0 << 0))
    pfYUV444P16 = (((((3 << 28) | (0 << 24)) | (16 << 16)) | (0 << 8)) | (0 << 0))
    pfYUV444PH = (((((3 << 28) | (1 << 24)) | (16 << 16)) | (0 << 8)) | (0 << 0))
    pfYUV444PS = (((((3 << 28) | (1 << 24)) | (32 << 16)) | (0 << 8)) | (0 << 0))

    pfRGB24 = (((((2 << 28) | (0 << 24)) | (8 << 16)) | (0 << 8)) | (0 << 0))
    pfRGB27 = (((((2 << 28) | (0 << 24)) | (9 << 16)) | (0 << 8)) | (0 << 0))
    pfRGB30 = (((((2 << 28) | (0 << 24)) | (10 << 16)) | (0 << 8)) | (0 << 0))
    pfRGB36 = (((((2 << 28) | (0 << 24)) | (12 << 16)) | (0 << 8)) | (0 << 0))
    pfRGB42 = (((((2 << 28) | (0 << 24)) | (14 << 16)) | (0 << 8)) | (0 << 0))
    pfRGB48 = (((((2 << 28) | (0 << 24)) | (16 << 16)) | (0 << 8)) | (0 << 0))
    pfRGBH = (((((2 << 28) | (1 << 24)) | (16 << 16)) | (0 << 8)) | (0 << 0))
    pfRGBS = (((((2 << 28) | (1 << 24)) | (32 << 16)) | (0 << 8)) | (0 << 0))


class VSFilterMode(IntEnum):
    fmParallel = 0
    fmParallelRequests = 1
    fmUnordered = 2
    fmFrameState = 3


class VSMediaType(IntEnum):
    mtVideo = 1
    mtAudio = 2


class VSAudioChannels(IntEnum):
    acFrontLeft = 0
    acFrontRight = 1
    acFrontCenter = 2
    acLowFrequency = 3
    acBackLeft = 4
    acBackRight = 5
    acFrontLeftOFCenter = 6
    acFrontRightOFCenter = 7
    acBackCenter = 8
    acSideLeft = 9
    acSideRight = 10
    acTopCenter = 11
    acTopFrontLeft = 12
    acTopFrontCenter = 13
    acTopFrontRight = 14
    acTopBackLeft = 15
    acTopBackCenter = 16
    acTopBackRight = 17
    acStereoLeft = 29
    acStereoRight = 30
    acWideLeft = 31
    acWideRight = 32
    acSurroundDirectLeft = 33
    acSurroundDirectRight = 34
    acLowFrequency2 = 35


class VSPropertyType(IntEnum):
    ptUnset = 0
    ptInt = 1
    ptFloat = 2
    ptData = 3
    ptFunction = 4
    ptVideoNode = 5
    ptAudioNode = 6
    ptVideoFrame = 7
    ptAudioFrame = 8


class VSMapPropertyError(IntEnum):
    peSuccess = 0
    peUnset = 1
    peType = 2
    peIndex = 4
    peError = 3


class VSMapAppendMode(IntEnum):
    maReplace = 0
    maAppend = 1
