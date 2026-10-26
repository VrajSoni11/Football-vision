import cv2
from pathlib import Path

video = cv2.VideoCapture('clips/clipB.mp4')
total = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
step = max(1, total // 60)                  # spread 30 frames evenly over the clip
out = Path('data/my_test_frames')
out.mkdir(parents=True, exist_ok=True)

saved = 0
for i in range(0, total, step):
    video.set(cv2.CAP_PROP_POS_FRAMES, i)
    ok, frame = video.read()
    if not ok or saved == 60:
        break
    cv2.imwrite(str(out / f'clipB_{i:05d}.jpg'), frame)
    saved += 1
print('Saved', saved, 'frames to', out)