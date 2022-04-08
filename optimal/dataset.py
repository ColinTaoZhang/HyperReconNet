import cv2
import numpy as np
import h5py
import random

"""
img_path1 = "harvard/train/"
path = ["1","2","3","4","5","6","7","8","9","10",
    "11","12","13","14","15","16","17","18","19","20",
    "21","22","23","24","25","26","27","28","29","30",
    "31","32","33","34","35"]
"""

img_path1 = "icvl/train/"
path = ["1","2","3","4","5","6","7","8","9","10",
	"11","12","13","14","15","16","17","18","19","20",
	"21","22","23","27","28","29","30",
	"31","32","33","34","35","36","37","38","39","40",
	"41","47","48","49","50","51",
	"80","81","82","86","87","88","89","149","150",
	"151","152","153","154","155","156","157","158","159","160",
	"161","162","163","164","165","166","167","168","169","170",
	"171","172","173","174","175","176","177","178","179","180",
	"181","182","183","184","185","186","187","188","189","190",
	"191","192","193","194","195","196","197","199","201"]

img_train = []
img_test = []
img = []

for i in range(len(path[:])):
  img_path2 = path[i]
  img.append(cv2.imread(img_path1 + img_path2 + "-{}.png".format(i+1), cv2.CV_LOAD_IMAGE_GRAYSCALE))

  h = img[0].shape[0]-30
  w = img[0].shape[1]
  img_ = np.zeros((31, h, w), dtype="float32")

  for k in range(31):
    img_[k] = img[k][k:k+h]

  img_ = img_ / 255

  for i in range(0, h-15, 7):
    for j in range(0, w-15, 7):
      if np.random.rand() < 0.8:
        img_train.append(img_[:, i:i+16, j:j+16])
      else:
        img_test.append(img_[:, i:i+16, j:j+16])
  print len(img_train), len(img_test)

l = len(img_train)
print l

l = int(l/20)

with h5py.File('train/train1.h5', 'w') as h5:
    h5['data'] = img_train[:l]
with h5py.File('train/train2.h5', 'w') as h5:
    h5['data'] = img_train[l:2*l]
with h5py.File('train/train3.h5', 'w') as h5:
    h5['data'] = img_train[2*l:3*l]
with h5py.File('train/train4.h5', 'w') as h5:
    h5['data'] = img_train[3*l:4*l]
with h5py.File('train/train5.h5', 'w') as h5:
    h5['data'] = img_train[4*l:5*l]
with h5py.File('train/train6.h5', 'w') as h5:
    h5['data'] = img_train[5*l:6*l]
with h5py.File('train/train7.h5', 'w') as h5:
    h5['data'] = img_train[6*l:7*l]
with h5py.File('train/train8.h5', 'w') as h5:
    h5['data'] = img_train[7*l:8*l]
with h5py.File('train/train9.h5', 'w') as h5:
    h5['data'] = img_train[8*l:9*l]
with h5py.File('train/train10.h5', 'w') as h5:
    h5['data'] = img_train[9*l:10*l]
with h5py.File('train/train11.h5', 'w') as h5:
    h5['data'] = img_train[10*l:11*l]
with h5py.File('train/train12.h5', 'w') as h5:
    h5['data'] = img_train[11*l:12*l]
with h5py.File('train/train13.h5', 'w') as h5:
    h5['data'] = img_train[12*l:13*l]
with h5py.File('train/train14.h5', 'w') as h5:
    h5['data'] = img_train[13*l:14*l]
with h5py.File('train/train15.h5', 'w') as h5:
    h5['data'] = img_train[14*l:15*l]
with h5py.File('train/train16.h5', 'w') as h5:
    h5['data'] = img_train[15*l:16*l]
with h5py.File('train/train17.h5', 'w') as h5:
    h5['data'] = img_train[16*l:17*l]
with h5py.File('train/train18.h5', 'w') as h5:
    h5['data'] = img_train[17*l:18*l]
with h5py.File('train/train19.h5', 'w') as h5:
    h5['data'] = img_train[18*l:19*l]
with h5py.File('train/train20.h5', 'w') as h5:
    h5['data'] = img_train[19*l:]

with open('train/train.txt', 'w') as fd:
    fd.write('train/train1.h5\ntrain/train2.h5\ntrain/train3.h5\ntrain/train4.h5\ntrain/train5.h5\ntrain/train6.h5\ntrain/train7.h5\ntrain/train8.h5\ntrain/train9.h5\ntrain/train10.h5' \
      'train/train11.h5\ntrain/train12.h5\ntrain/train13.h5\ntrain/train14.h5\ntrain/train15.h5\ntrain/train16.h5\ntrain/train17.h5\ntrain/train18.h5\ntrain/train19.h5\ntrain/train20.h5')

l = len(img_test)
l = int(l/2)

with h5py.File('test/test1.h5', 'w') as h5:
    h5['data'] = img_test[:l]
with h5py.File('test/test2.h5', 'w') as h5:
    h5['data'] = img_test[l:]

with open('test/test.txt', 'w') as fd:
    fd.write('test/test1.h5\ntest/test2.h5')
