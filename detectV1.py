import numpy as np
import math

# i'll add more thresholds later to meet requirements
# UPDATE: Thresholds added
thresh1 = 35
thresh2 = 40
thresh3 = 55

# distance of camera to targets, strongly suggested maximum 1 meter
distance = 1

# field of view of camera, should be 110 degrees
FOV = 110

# maybe at some point i'll stop using this constant, but for now, this works for 0.9 to 1 m
pixel_size = 0.03848 * 0.03848

# this finds the size of the cluster of pixels above the threshold temperature
def findNeighbors(i, j, thresh, frame, already_clustered):
    if (i < 0 or j < 0 or i >= len(frame) or j >= len(frame[0]) or (i, j) in already_clustered):
        return 0
    if (frame[i][j] >= thresh):
        already_clustered.add((i, j))
        return 1 + findNeighbors(i+1, j, thresh, frame, already_clustered) + findNeighbors(i-1, j, thresh, frame, already_clustered) + findNeighbors(i, j+1, thresh, frame, already_clustered) + findNeighbors(i, j-1, thresh, frame, already_clustered)
    return 0


# returns the (approximate) size of the target in meters squared
def findSize(pixels):
    return pixels * pixel_size

def detect(getFrame_output):
    frame = getFrame_output
    frame = np.array(frame)
    frame.shape = (24, 32)

    # set of tuples that have already been 'claimed' by a cluster of pixels above threshold
    already_clustered = set()
    # list of tuples of form (size, temperature)
    clusters = []

    # now we loop through the pixels, and if a pixel is above the threshold and not already part of a cluster,
    # then we find its cluster size
    for i in range(len(frame)):
        for j in range(len(frame[0])):
            if ((i, j) not in already_clustered): 
                if (frame[i][j] >= thresh3):
                    neighbors = findNeighbors(i, j, thresh3, frame, already_clustered)
                    size = findSize(neighbors)
                    if (neighbors > 0):
                        clusters.append((size, thresh3, frame, already_clustered))
                elif (frame[i][j] >= thresh2):
                    neighbors = findNeighbors(i, j, thresh2, frame, already_clustered)
                    size = findSize(neighbors)
                    if (neighbors > 0):
                        clusters.append((size, thresh2))
                elif (frame[i][j] >= thresh1):
                    neighbors = findNeighbors(i, j, thresh1, frame, already_clustered)
                    size = findSize(neighbors)
                    if (neighbors > 0):
                        clusters.append((size, thresh1))
    
    return clusters

    # printing out the clusters for the sake of testing
    #for x in clusters:
    #    print(x)
