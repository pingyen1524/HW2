# 林秉言 <span style="color:red">(106061524)</span>

# Project 2 / Panorama Stitching

## Overview
The project is to learn how to


## Implementation
1. Matching SIFT Descriptors
	* item
	* item


   Code highlights:
```
    N1 = descriptor1.shape[0]
    N2 = descriptor2.shape[0]
    THRESH = 0.7
    
    o_1 = np.zeros(0)
    o_2 = np.zeros(0)
    cnt = 0
    d_norm2 = np.zeros(N2)
    for i in range(N1):
        for j in range(N2):
            d_norm2[j-1] = np.sum(((descriptor1[i-1,:] - descriptor2[j-1,:]) ** 2)) ** 0.5
        d_norm2_sort = np.argsort(d_norm2)
        if d_norm2[d_norm2_sort[0]] < THRESH*d_norm2[d_norm2_sort[1]]:
            o_1 = np.append(o_1,i-1)
            o_2 = np.append(o_2,d_norm2_sort[0])
            cnt = cnt + 1
    match = np.zeros((cnt,2))
    match[:,0] = o_1
    match[:,1] = o_2
```

2. Fitting the Transformation Matrix
	* item
	* item



   Code highlights:
```
    H_tran = np.linalg.lstsq(np.transpose(P1), np.transpose(P2))[0]
    H = np.transpose(H_tran)
```

3. RANSAC
	* item
	* item



   Code highlights:
```
    match_num = match.shape[0]
    pt1_m = pt1[match[:, 0].astype(int),:]
    pt2_m = pt2[match[:, 1].astype(int),:]
    
    pt1_m = np.append(np.transpose(pt1_m),np.ones([1,match_num]),axis = 0)
    pt2_m = np.append(np.transpose(pt2_m),np.ones([1,match_num]),axis = 0)
    
    pt1_2_m = np.dot(H,pt1_m)
    dists_tran = (np.sum((pt1_2_m - pt2_m)**2,0))**0.5
    dists = np.transpose(dists_tran)
```

4. Stitching Multiple Images
	* item
	* item



   Code highlights:
```
    if refFrameIndex > currentFrameIndex:
        T = i_To_iPlusOne_Transform[refFrameIndex-1];
        for i in range(refFrameIndex-2,currentFrameIndex-1,-1):
            T = np.dot(T,i_To_iPlusOne_Transform[i]);
    elif refFrameIndex < currentFrameIndex:
        T = np.linalg.pinv(i_To_iPlusOne_Transform[refFrameIndex]);
        for i in range(refFrameIndex+1,currentFrameIndex):
            T = np.dot(T,np.linalg.pinv(i_To_iPlusOne_Transform[i]));
    else:
        T = np.eye(3);
```

## Installation
* Other required packages.
* How to compile from source?

### Results

There are some examples I processed with image stitching.
The first two images are both combination of two images, and the two images
below are combined with multiple images.

images used to form a panorama:2
<table border=1>
<tr>
<td>
<img src="uttower_pano.jpg" width="99%"/>
</td>
</tr>
<tr>
<td>
<img src="Hanging_pano.png" width="99%"/>
</td>
</tr>

</table>

images used to form a panorama:4
<table border=1>
<tr>
<td>
<img src="ypano.png" width="99%"/>
</td>
</tr>

</table>

images used to form a panorama:6
<table border=1>
<tr>
<td>
<img src="pano.png" width="99%"/>
</td>
</tr>

</table>
