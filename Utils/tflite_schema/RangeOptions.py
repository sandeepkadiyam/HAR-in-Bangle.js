# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite

import flatbuffers

class RangeOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsRangeOptions(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = RangeOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def RangeOptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # RangeOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

def RangeOptionsStart(builder): builder.StartObject(0)
def RangeOptionsEnd(builder): return builder.EndObject()
