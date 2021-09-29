#!/usr/bin/env python
import sys

import av

# Откроем ресурс на чтение
input_resource = av.open(
    sys.argv[1]
)
# Откроем ресурс на запись.
output_resource = av.open(
    sys.argv[2],
    mode='w',
    format='flv'
)
# Список потоков входного ресурса: видео и аудио
input_streams = list()
# Список потоков выходного ресурса: видео и аудио
output_streams = list()
# Для входного и выходного ресурсов возьмём поток видео.
for stream in input_resource.streams:
    if stream.type == 'video':
        input_streams.append(stream)
        # Создадим видео-поток для выходного ресурса. Кодек `h264`.
        output_streams += [output_resource.add_stream('h264')]
        break
# Для входного и выходного ресурсов возьмём поток аудио.
for stream in input_resource.streams:
    if stream.type == 'audio':
        input_streams.append(stream)
        # Создадим аудио-поток для выходного ресурса. Кодек `aac`.
        output_streams += [output_resource.add_stream('aac')]
        break

for packet in input_resource.demux(input_streams):
    # Получим все кадры пакета.
    for frame in packet.decode():
    #    # Сбросим PTS для самостоятельного вычислении при кодировании.
        frame.pts = None
        # Закодируем соответствующие кадры для выходных потоков.
        for stream in output_streams:
            if packet.stream.type == stream.type:
                #output_resource.mux(frame)#stream.encode(frame))
                pkt = stream.encode(frame)
                print(pkt)
                if pkt:
                    output_resource.mux(pkt)
                #new_packet = []
