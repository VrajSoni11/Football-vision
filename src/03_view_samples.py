import random, cv2, yaml
from pathlib import Path

root = Path('data/football')
names = yaml.safe_load((root / 'data.yaml').read_text())['names']
out = Path('assets/samples')
out.mkdir(parents=True, exist_ok=True)

imgs = list((root / 'train' / 'images').glob('*.jpg'))
for p in random.sample(imgs, min(30, len(imgs))):
    img = cv2.imread(str(p))
    h, w = img.shape[:2]
    lab = root / 'train' / 'labels' / (p.stem + '.txt')
    if lab.exists():
        for line in lab.read_text().splitlines():
            c, x, y, bw, bh = line.split()[:5]
            c = int(c)
            x, y, bw, bh = float(x) * w, float(y) * h, float(bw) * w, float(bh) * h
            x1, y1 = int(x - bw / 2), int(y - bh / 2)
            x2, y2 = int(x + bw / 2), int(y + bh / 2)
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(img, str(names[c]), (x1, max(y1 - 5, 12)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
    cv2.imwrite(str(out / p.name), img)
print('Saved to assets/samples')