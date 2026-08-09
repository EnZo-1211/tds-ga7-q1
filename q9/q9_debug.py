from PIL import Image
import numpy as np

img = Image.open('forensics-frames.png').convert('RGB')
w, h = img.size
# 6 across, 4 down
frame_w = w // 6
frame_h = h // 4

for i in range(24):
    row = i // 6
    col = i % 6
    left = col * frame_w
    upper = row * frame_h
    right = left + frame_w
    lower = upper + frame_h
    frame = img.crop((left, upper, right, lower))
    # print pixel 0,0
    print(f"Frame {i}: {np.array(frame)[0, 0]}")
