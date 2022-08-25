import os
from PIL import Image
import tqdm
files = os.listdir("./")
for i in tqdm.trange(len(files)):
    if files[i].endswith(".png"):
        try:
            im = Image.open(files[i]).convert('RGB')
            im2 = im.resize((128, 128), Image.Resampling.NEAREST)
            im2.save(files[i])
        except:
            print(files[i])
