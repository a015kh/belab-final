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
speed = 2
tempo = 140
l = 1.28
m = 2.9
y, sr = librosa.load("assets/music/dancing-moon-night.wav", sr=None)
np.random.seed(0)
stride = 512
num_poses = 50
onsets = librosa.onset.onset_detect(y, sr=sr)

selected = []
period = 1.5
prev = 0
for onset in onsets:
    if (onset - prev) * stride / sr > period:
        selected.append(onset)
        prev = onset
# selected = np.random.choice(onsets, num_poses)
pose_id = np.arange(51)
sheet = np.zeros((len(selected), 4))

for i, idx in enumerate(sorted(selected)):
    sheet[i][0] = idx * stride / sr
    sheet[i][1] = np.random.choice(pose_id)
    sheet[i][2] = 0
    sheet[i][3] = speed
    c = (2 - int(sheet[i][1]) % 3)
    s = sheet[i][2]
    if (c == 0 and s == 0):
        sheet[i][0] -= 1.3
    elif (c == 2 and s == 1):
        sheet[i][0] -= 0.7
    elif (c == 0 and s == 1):
        sheet[i][0] -= 4.5
    elif (c == 2 and s == 0):
        sheet[i][0] -= 3.0
    elif c == 1:
        sheet[i][0] -= 2.9
    if sheet[i][0] < 0:
        sheet[i][0] = 0

# sheet = np.sort(sheet, axis=0)
sheet = sorted(sheet, key=lambda x: x[0])


with open("pose.txt", "w") as fout:
    for line in sheet:
        prefix = "    " * (2 - int(line[1]) % 3)
        fout.write("{}{} {} {} {}\n".format(
            prefix, np.round(line[0], 2), line[1], line[2], line[3]
        ))
