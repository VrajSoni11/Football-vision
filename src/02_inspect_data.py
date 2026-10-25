from pathlib import Path
from collections import Counter
import yaml

root = Path('data/football')
names = yaml.safe_load((root / 'data.yaml').read_text())['names']
print('Classes:', names)

for split in ['train', 'valid', 'test']:
    labels = root / split / 'labels'
    if not labels.exists():
        continue
    counts = Counter()
    files = list(labels.glob('*.txt'))
    for f in files:
        for line in f.read_text().splitlines():
            counts[int(line.split()[0])] += 1
    print(f'\n{split}: {len(files)} images')
    for k, v in sorted(counts.items()):
        print(f'  {names[k]}: {v}')