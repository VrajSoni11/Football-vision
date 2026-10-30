| baseline | yolo26n COCO | 960 | – | – | – | 57.5% of frames have a ball box (includes false positives) | 15.4 people/frame; no referee/goalkeeper classes |

| n_960 | yolo26n | 960 | 26 run (best at 11; early stop, patience 15) | <player mAP50> | <ball mAP50> | (Phase 3) | first fine-tune on Kaggle GPU |

| n_960_full | yolo26n | 960 | 100 | 0.924 | 0.414 | (Phase 3) | val numbers; test mAP50 0.811 / mAP50-95 0.499; best≈last; 23 min |