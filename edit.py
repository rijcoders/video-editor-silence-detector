import moviepy.editor as mpy
from datetime import timedelta


from silencer import silence

VCODEC = "libx264"
VIDEO_QUALITY = "24"
COMPRESSION = "slow"

title = "7"
load_title = title + ".mp4"
save_title = "new.mp4"

validated_date = []

for i,j in silence:
    if (j - i) > 5:
        time1 = (timedelta(seconds=i))
        time2 = (timedelta(seconds=j))
        time3 = time2 - time1

        validated_date.append(((time1), (time2), (time3)))


def edit_video(load_title, save_title, cuts):
    # load file
    video = mpy.VideoFileClip(load_title)

    # cut file
    clips = []
    for i in range(0, len(cuts)-1):
        if i == 0:
            clip = video.subclip(0, str(cuts[i][0]))
        else:
            clip = video.subclip(str(cuts[i-1][1]), str(cuts[i][0]))
        clips.append(clip)

    final_clip = mpy.concatenate_videoclips(clips)

    # save file
    final_clip.write_videofile(save_title, threads=4, fps=24,
                               codec=VCODEC,
                               preset=COMPRESSION,
                               ffmpeg_params=["-crf",VIDEO_QUALITY])

    video.close()


if __name__ == '__main__':
    edit_video(load_title, save_title, validated_date)
