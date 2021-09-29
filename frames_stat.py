#!/usr/bin/env python
import sys

import av


print("filename,pkt_num,frame_num,type,pts,dts,time,time_base,is_corrupt")

i = 0
k = 0

def frames_stat(filename):
    global i, k
    input_resource = av.open(filename)
    input_streams = []


    # Для входного ресурса возьмём потоки .
    for stream in input_resource.streams:
        if stream.type in ('video', 'audio'):
            input_streams.append(stream)
            input_streams.append(stream)


    for packet in input_resource.demux(input_streams):
        i = i + 1
        # Получим все кадры пакета.
        for frame in packet.decode():
            k = k + 1
            params = [
                filename,
                str(i),
                str(k),
                str(frame.__class__.__name__),
                str(frame.pts),
                str(frame.dts),
                str(frame.time),
                str(frame.time_base),
                str(int(frame.is_corrupt)),
            ]
            print(",".join(params))
    input_resource.close()


if __name__=='__main__':
    for filename in sys.argv[1:]:
        frames_stat(filename)
