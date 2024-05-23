#include "VSHelper4.h"
#include "VapourSynth4.h"

static void VS_CC returnPtr(const VSMap *in, VSMap *out, void *userData, VSCore *core, const VSAPI *vsapi) {
    int64_t ptr = (int64_t) userData;

    if (ptr == 1)
        ptr = (int64_t) core;
    else if (ptr == 2)
        ptr = (int64_t) vsapi;

    vsapi->mapSetInt(out, "ptr", ptr, maReplace);
}

static void VS_CC getNodePtr(const VSMap *in, VSMap *out, void *userData, VSCore *core, const VSAPI *vsapi) {
    returnPtr(in, out, vsapi->mapGetNode(in, "clip", 0, 0), core, vsapi);
}

static void VS_CC getNodePtr(const VSMap *in, VSMap *out, void *userData, VSCore *core, const VSAPI *vsapi) {
    returnPtr(in, out, vsapi->mapGetFrame(in, "frame", 0, 0), core, vsapi);
}

static void VS_CC getNodeFromPtr(const VSMap *in, VSMap *out, void *userData, VSCore *core, const VSAPI *vsapi) {
    vsapi->mapConsumeNode(out, "clip", (VSNode *) vsapi->mapGetInt(in, "ptr", 0, 0), maReplace);
}

static void VS_CC getFrameFromPtr(const VSMap *in, VSMap *out, void *userData, VSCore *core, const VSAPI *vsapi) {
    vsapi->mapConsumeFrame(out, "frame", (VSFrame *) vsapi->mapGetInt(in, "ptr", 0, 0), maReplace);
}

VS_EXTERNAL_API(void) VapourSynthPluginInit2(VSPlugin *plugin, const VSPLUGINAPI *vspapi) {
    vspapi->configPlugin(
        "dev.setsugen.vscapi", "vscapi", "Helper plugin for vapoursynth-capi.", VS_MAKE_VERSION(1, 0),
        vspapi->getAPIVersion(), pcModifiable, plugin
    );

    char *vnode = "clip:vnode;";
    char *anode = "clip:anode;";
    char *vframe = "frame:vframe;";
    char *aframe = "frame:aframe;";
    char *ptr = "ptr:int;";

    vspapi->registerFunction("getVSCApiPtr", "", ptr, returnPtr, (void *) plugin, plugin);
    vspapi->registerFunction("getVSPApiPtr", "", ptr, returnPtr, (void *) vspapi, plugin);

    vspapi->registerFunction("getCorePtr", "", ptr, returnPtr, (void *) 1, plugin);
    vspapi->registerFunction("getVSApiPtr", "", ptr, returnPtr, (void *) 2, plugin);

    vspapi->registerFunction("getBitBltPtr", "", ptr, returnPtr, (void *) &vsh_bitblt, plugin);

    vspapi->registerFunction("getVNodePtr", vnode, ptr, getNodePtr, NULL, plugin);
    vspapi->registerFunction("getANodePtr", anode, ptr, getNodePtr, NULL, plugin);

    vspapi->registerFunction("getVFramePtr", vframe, ptr, getFramePtr, NULL, plugin);
    vspapi->registerFunction("getAFramePtr", aframe, ptr, getFramePtr, NULL, plugin);

    vspapi->registerFunction("getVNodeFromPtr", ptr, vnode, getNodeFromPtr, NULL, plugin);
    vspapi->registerFunction("getANodeFromPtr", ptr, anode, getNodeFromPtr, NULL, plugin);

    vspapi->registerFunction("getVFrameFromPtr", ptr, vframe, getFrameFromPtr, NULL, plugin);
    vspapi->registerFunction("getAFrameFromPtr", ptr, aframe, getFrameFromPtr, NULL, plugin);
}
