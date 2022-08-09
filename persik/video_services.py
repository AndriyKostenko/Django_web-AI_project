from pathlib import Path
from typing import IO, Generator
from django.http import StreamingHttpResponse
from django.shortcuts import get_object_or_404

from .models import Video



def get_streaming_video(request, pk: int):
    file, status_code, content_length, content_range = open_file(request, pk)
    response = StreamingHttpResponse(file, status=status_code, content_type='video/mp4') #class StreaminghttpResponse
    # allowing us to send data partially one by one

    response['Accept-Ranges'] = 'bytes'
    response['Content-Length'] = str(content_length)
    response['Cache-Control'] = 'no-cache'
    response['Content-Range'] = content_range
    return response


#generator to continue watching video from where we've stpped
def ranged(file: IO[bytes], start: int = 0, end: int = None, block_size: int = 8192,) -> Generator[bytes, None, None]:
    #blocksize - 8192 - default as the proxy buffer size
    consumed = 0 #starting from 0

    file.seek(start)
    while True:
        data_length = min(block_size, end - start - consumed) if end else block_size
        if data_length <= 0: # no more bytes - completed
            break
        data = file.read(data_length) # sending bytes
        if not data:
            break
        consumed += data_length #saving for remembering the point to start for the next time
        yield data

    if hasattr(file, 'close'):
        file.close()


def open_file(request, video_pk: int) -> tuple:
    _video = get_object_or_404(Video, pk=video_pk) #searching for a video

    path = Path(_video.file.path)

    file = path.open('rb')
    file_size = path.stat().st_size

    content_length = file_size
    status_code = 200
    content_range = request.headers.get('range') #we know on which point we have loaded the video

    if content_range is not None:
        content_ranges = content_range.strip().lower().split('=')[-1] #we know from which bytes we can continue loading
        range_start, range_end, *_ = map(str.strip, (content_ranges + '-').split('-')) #dividing right and left sides
        range_start = max(0, int(range_start)) if range_start else 0 # if exists counting the max
        range_end = min(file_size - 1, int(range_end)) if range_end else file_size - 1 # same as above
        content_length = (range_end - range_start) + 1
        file = ranged(file, start=range_start, end=range_end + 1) #saving info about our current state of vide-file
        status_code = 206 # delivering only part of the resource
        content_range = f'bytes {range_start}-{range_end}/{file_size}'

    return file, status_code, content_length, content_range
