from .lib import *  # noqa: F401, F403
from .structs import *  # noqa: F401, F403
from .vsenums import *  # noqa: F401, F403
from .utils import VS_MAKE_VERSION
from .vsapi import *  # noqa: F401, F403

VAPOURSYNTH_API_MAJOR = 4
VAPOURSYNTH_API_MINOR = 0
VAPOURSYNTH_API_VERSION = VS_MAKE_VERSION(VAPOURSYNTH_API_MAJOR, VAPOURSYNTH_API_MINOR)

VS_AUDIO_FRAME_SAMPLES = 3072
