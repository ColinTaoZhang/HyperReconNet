import cv2
import numpy as np
import h5py
import random

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
img_mask_train = []
img_mask_test = []

random_mask_ = np.random.rand(1024)
random_mask_ = random_mask_.reshape((32, 32))
random_mask = np.zeros((64, 64))
for i in range(32):
  for j in range(32):
    if random_mask_[i][j] < 0.5:
      random_mask[i][j] = 1
      random_mask[i+32][j] = 1
      random_mask[i][j+32] = 1
      random_mask[i+32][j+32] = 1
    else:
      random_mask[i][j] = 0
      random_mask[i+32][j] = 0
      random_mask[i][j+32] = 0
      random_mask[i+32][j+32] = 0

#cv2.imshow('mask', random_mask)
cv2.imwrite('mask_64.png', random_mask*255)
#cv2.waitKey(0)

for i in range(len(path[:])):
  img_path2 = path[i]
  img.append(cv2.imread(img_path1 + img_path2 + "-{}.png".format(i+1), cv2.CV_LOAD_IMAGE_GRAYSCALE))

  h = img1.shape[0]-30
  w = img1.shape[1]
  h = int(h/64)*64
  w = int(w/64)*64
  img_ = np.zeros((31, h, w), dtype="float32")
  img_mask = np.zeros((31, h, w), dtype="float32")

  for k in range(31):
    img_[k] = img[k][k:k+h]

  img_ = img_ / 255

  for k in range(31):
    for i in range(0, h, 64):
      for j in range(0, w, 64):
        for p in range(64):
          for q in range(64):
            img_mask[k][(i-k+p)%h][j+q] = img_[k][(i-k+p)%h][j+q] * random_mask[p][q]

  for i in range(h):
    for j in range(w):
      for k in range(1, 31, 1):
        img_mask[0][i][j] += img_mask[k][i][j]

  for i in range(0, h-63, 32):
    for j in range(0, w-63, 32):
      if np.random.rand() < 0.8:
        img_train.append(img_[:, i:i+64, j:j+64])
        img_mask_train.append(img_mask[0, i:i+64, j:j+64].reshape((1,64,64)))
      else:
        img_test.append(img_[:, i:i+64, j:j+64])
        img_mask_test.append(img_mask[0, i:i+64, j:j+64].reshape((1,64,64)))
  print len(img_train), len(img_test)

l = len(img_mask_train)
print l
l = int(l/10)

with h5py.File('train_random/train1.h5', 'w') as h5:
  h5['data'] = img_mask_train[:l]
  h5['groundtruth'] = img_train[:l]
with h5py.File('train_random/train2.h5', 'w') as h5:
  h5['data'] = img_mask_train[l:2*l]
  h5['groundtruth'] = img_train[l:2*l]
with h5py.File('train_random/train3.h5', 'w') as h5:
  h5['data'] = img_mask_train[2*l:3*l]
  h5['groundtruth'] = img_train[2*l:3*l]
with h5py.File('train_random/train4.h5', 'w') as h5:
  h5['data'] = img_mask_train[3*l:4*l]
  h5['groundtruth'] = img_train[3*l:4*l]
with h5py.File('train_random/train5.h5', 'w') as h5:
  h5['data'] = img_mask_train[4*l:5*l]
  h5['groundtruth'] = img_train[4*l:5*l]
with h5py.File('train_random/train6.h5', 'w') as h5:
  h5['data'] = img_mask_train[5*l:6*l]
  h5['groundtruth'] = img_train[5*l:6*l]
with h5py.File('train_random/train7.h5', 'w') as h5:
  h5['data'] = img_mask_train[6*l:7*l]
  h5['groundtruth'] = img_train[6*l:7*l]
with h5py.File('train_random/train8.h5', 'w') as h5:
  h5['data'] = img_mask_train[7*l:8*l]
  h5['groundtruth'] = img_train[7*l:8*l]
with h5py.File('train_random/train9.h5', 'w') as h5:
  h5['data'] = img_mask_train[8*l:9*l]
  h5['groundtruth'] = img_train[8*l:9*l]
with h5py.File('train_random/train10.h5', 'w') as h5:
  h5['data'] = img_mask_train[9*l:]
  h5['groundtruth'] = img_train[9*l:]

with open('train_random/train.txt', 'w') as fd:
  fd.write('train_random/train1.h5\ntrain_random/train2.h5\ntrain_random/train3.h5\ntrain_random/train4.h5\ntrain_random/train5.h5\ntrain_random/train6.h5\ntrain_random/train7.h5\ntrain_random/train8.h5\ntrain_random/train9.h5\ntrain_random/train10.h5')

l = len(img_mask_test)
print l

l = int(l/2)

with h5py.File('test_random/test1.h5', 'w') as h5:
  h5['data'] = img_mask_test[:l]
  h5['groundtruth'] = img_test[:l]
with h5py.File('test_random/test2.h5', 'w') as h5:
  h5['data'] = img_mask_test[l:]
  h5['groundtruth'] = img_test[l:]

with open('test_random/test.txt', 'w') as fd:
  fd.write('test_random/test1.h5\ntest_random/test2.h5')

