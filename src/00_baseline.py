from pathlib import Path
from ultralytics import YOLO

ROOT = Path(__file__).resolve().parent.parent       # the fballvision folder

model = YOLO('yolo26n.pt')
stream = model.predict(str(ROOT / 'clips' / 'clipB.mp4'), stream=True, save=True,
                       imgsz=960, conf=0.25, classes=[0, 32],   # 0 = person, 32 = sports ball
                       project=str(ROOT / 'runs'), name='baseline', exist_ok=True,
                       verbose=False)               # stops the 727 lines of per-frame output

frames = ball_frames = people_total = 0
for r in stream:
    cls = r.boxes.cls.int().tolist()
    frames += 1
    people_total += cls.count(0)
    ball_frames += 32 in cls

print(f'Frames: {frames}')
print(f'Frames with a ball detected: {ball_frames} ({100 * ball_frames / frames:.1f}%)')
print(f'Average people per frame: {people_total / frames:.1f}')