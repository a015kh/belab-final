import numpy as np
import librosa

# 51 poses (0~50)
# 1 punch (51)
# left-left: 1.28
# left-middle: 2.9
# left-right: 4.56
# tempo: 140 bpm 
# pose_id mod 0 -> b
# pose_id mod 1 -> g
# pose_id mod 2 -> r
speed = 1.6
tempo = 140
l = 1.28
m = 2.9
y, sr = librosa.load("assets/music/dancing-moon-night.wav", sr=None)
np.random.seed(0)
stride = 512
onsets = librosa.onset.onset_detect(y, sr=sr)

selected = []
period = 2
prev = 0
for onset in onsets:
    if (onset - prev) * stride / sr > period:
        selected.append(onset)
        prev = onset
# selected = np.random.choice(onsets, num_poses)
pose_id = np.arange(52)
sheet = np.zeros((len(selected), 4))
prev_c = np.random.randint(0, 3)
prev_direc = np.random.randint(0, 2)
c = prev_c
direc = prev_direc

r = 0.8

for i, idx in enumerate(sorted(selected)):
    sheet[i][0] = idx * stride / sr
    p = np.random.choice(pose_id)
    new_p = p
    if p != 51:
        if p % 3 == c:
            pass
        else:
            new_p = p // 3 * 3 + c
        
    print(p, new_p, c)
    sheet[i][1] = new_p
    sheet[i][2] = direc
    sheet[i][3] = speed
    color = (2 - int(sheet[i][1]) % 3)
    s = sheet[i][2]
    if np.random.random() > r:
        print("change")
        c = np.random.randint(0, 3)
        direc = 1 - prev_direc
        while c == prev_c:
            c = np.random.randint(0, 3)
        prev_c = c
        prev_direc = direc

# sheet = np.sort(sheet, axis=0)
sheet = sorted(sheet, key=lambda x: x[0])

with open("pose.txt", "w") as fout:
    for line in sheet:
        prefix = "    " * (2 - int(line[1]) % 3)
        fout.write("{}{} {} {}\n".format(
            prefix, np.round(line[0], 2), line[1], line[2]
        ))
