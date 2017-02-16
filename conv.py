source = "HeadPoseImageDatabase"
target = "t"

import os
import shutil

NUMPERSONS = 15

names = []

for i in range(1, NUMPERSONS+1):
	tsource = source+"/Person"+str(i).zfill(2)
	for fn in os.listdir(tsource):
		if fn.endswith(".jpg") and fn[8]=="1":
			nname = str(i)+fn[11:]
			names.append(nname)
			shutil.copy(os.path.join(tsource,fn), os.path.join(target,nname))
print(names)
