#! /bin/sh

# ffmpeg -i https://hls.cntv.myalicdn.com/asp/hls/main/0303000a/3/default/9a9c46561e1445e59e83234ed89cc707/main.m3u8\?maxbr\=2048\&minbr\=400 -c copy -bsf:a aac_adtstoasc output.mp4
ffmpeg -i $1 -c copy -bsf:a aac_adtstoasc $2
