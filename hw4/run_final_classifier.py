def run_final_classifier(path):
    # import
#!/usr/bin/env python
    import matplotlib.pyplot as plt
    from glob import glob
    import numpy as np
    import scipy.ndimage as ndimg
    import skimage.filter as filter
    import skimage.transform as transform
    import re
    from os import listdir
    from multiprocessing import Pool, cpu_count
    from pylab import imread
    from time import time
    import pickle
    from sklearn.ensemble import RandomForestClassifier
    
    def row(img2d):
        return np.shape(img2d)[0]
        
    def col(img2d):
        return np.shape(img2d)[1]
    
    def layer_mean(img2d):
        img1d = img2d[img2d<255]
        return img1d.mean()
    
    def hist_max(img2d):
        img1d = img2d[img2d<255]
        [n, bins, patches]= plt.hist(img1d, np.arange(255))
        return bins[n.argmax()]
    
    def edge_length(img2d):
        "gray input"
        imgsize = float((img2d.shape[0]*img2d.shape[1]))
        med_filter = ndimg.median_filter(img2d, size = (5,5))
        edges = filter.canny(med_filter,3)
        return edges.sum()/imgsize
    
    def edge_sobel_h(img2d):
        "gray input"
        imgsize = float((img2d.shape[0]*img2d.shape[1]))
        med_filter = ndimg.median_filter(img2d, size = (5,5))
        edges_h = filter.hsobel(med_filter/255.)
        return edges_h.sum()/imgsize
    
    def edge_sobel_v(img2d):
        "gray input"
        imgsize = float((img2d.shape[0]*img2d.shape[1]))
        med_filter = ndimg.median_filter(img2d, size = (5,5))
        edges_v = filter.vsobel(med_filter/255.)
        return edges_v.sum()/imgsize
    
    def edge_sobel(img2d):
        "gray input"
        imgsize = float((img2d.shape[0]*img2d.shape[1]))
        med_filter = ndimg.median_filter(img2d, size = (5,5))
        edges = filter.sobel(med_filter/255.)
        return edges.sum()/imgsize
    
    def houghLine(img2d):
        "gray input"
        med_filter = ndimg.median_filter(img2d, size = (5,5))
        edges = filter.sobel(med_filter/255.)
        [H,theta,distances] = transform.hough_line(edges);
        imgsize = float(len(theta)*len(distances))
        return H.sum()/imgsize
    
    def cate_extract(image_path):
        cate_temp = image_path.replace(MYDIRECTORY,'')
        cate = re.search(r'/.+?/', cate_temp)
        return cate_map[cate.group()[1:-1]]
    
    def features(image_path):
        #red mean
        img2d = ndimg.imread(image_path)
        img2d_gray = ndimg.imread(image_path, flatten= True)
        
        row_n = row(img2d_gray)
        col_n = col(img2d_gray)
        
        red_mean = layer_mean(img2d[...,0])
        green_mean = layer_mean(img2d[...,1])
        blue_mean = layer_mean(img2d[...,2])
        gray_mean = layer_mean(img2d_gray)
        
        red_most = hist_max(img2d[...,0])
        green_most = hist_max(img2d[...,1])
        blue_most = hist_max(img2d[...,2])
        gray_most = hist_max(img2d_gray)
        
        length = edge_length(img2d_gray)
        sobel_h = edge_sobel_h(img2d_gray)
        sobel_v = edge_sobel_v(img2d_gray)
        sobel = edge_sobel(img2d_gray)
        hough = houghLine(img2d_gray)
        
        cate = cate_extract(image_path)
        
        return list([row_n, col_n, red_mean, green_mean, blue_mean, gray_mean,\
                         red_most,green_most,blue_most, gray_most,\
                         length, sobel_h, sobel_v, sobel, hough, cate])
        
    #!/usr/bin/env python
    """
    AY 250 - Scientific Research Computing with Python
    Homework Assignment 4 - Parallel Feature Extraction Example
    Author: Christopher Klein, Joshua Bloom
    """
    ## CHANGE THIS NEXT LINE!
    MYDIRECTORY = path
    
    # FUNCTION DEFINITIONS
    # Quick function to divide up a large list into multiple small lists, 
    # attempting to keep them all the same size. 
    def split_seq(seq, size):
            newseq = []
            splitsize = 1.0/size*len(seq)
            for i in range(size):
                newseq.append(seq[int(round(i*splitsize)):
                    int(round((i+1)*splitsize))])
            return newseq
    # Our simple feature extraction function. It takes in a list of image paths, 
    # does some measurement on each image, then returns a list of the image paths
    # paired with the results of the feature measurement.
    def extract_features(image_path_list):
        feature_list = []
        for image_path in image_path_list:
            image_array = imread(image_path)
            ft = features(image_path)
            
            #ft = image_array.shape # This feature is simple. You can modify this
            # code to produce more complicated features and to produce multiple
            # features in one function call.
            feature_list.append(ft)
        return feature_list
    ### Main program starts here ###################################################
    # We first collect all the local paths to all the images in one list
    image_paths = []
    imgsList = listdir(MYDIRECTORY)
    
    # Load test Images
    for name in imgsList:
        image_paths.append(MYDIRECTORY+'/'+name)
    
    print 'filename' + 15*' '+ 'predicted_class'
    print '_ '*20
    # Then, we run the feature extraction function using multiprocessing.Pool so 
    # so that we can parallelize the process and run it much faster.
    #numprocessors = cpu_count() # To see results of parallelizing, set numprocessors
    # to less than cpu_count().
    
    #create an array to store features
    #nFeature = 13
    #features_array = np.zeros(len(image_paths), nFeature)
    
    #Using multicores
    numprocessors = cpu_count()
    
    # We have to cut up the image_paths list into the number of processes we want to
    # run. 
    split_image_paths = split_seq(image_paths, numprocessors)
    
    # Ok, this block is where the parallel code runs. We time it so we can get a 
    # feel for the speed up.
    start_time = time()
    p = Pool(numprocessors)
    result = p.map_async(extract_features, split_image_paths)
    poolresult = result.get()
    end_time = time()
    #DATA = np.vstack([poolresult[i] for i in range(np.shape(poolresult)[0])])
    # All done, print timing results.
    print ("Finished extracting features. Total time: " + 
        str(round(end_time-start_time, 3)) + " s, or " + 
        str( round( (end_time-start_time)/len(image_paths), 5 ) ) + " s/image.")
    # This took about 10-11 seconds on my 2.2 GHz, Core i7 MacBook Pro. It may also
    # be affected by hard disk read speeds.
    
    # To tidy-up a bit, we loop through the poolresult to create a final list of
    # the feature extraction results for all images.
    combined_result = []
    for single_proc_result in poolresult:
        for single_image_result in single_proc_result:
            combined_result.append(single_image_result)
    X_test = np.array(combined_result)
    # X_test are the features of the test images
    # load the trained classifier
    clf = pickle.load(open('trained_classifier.p', 'rb'))
    #load the category table
    cate_map = dict(zip(range(len(categories)),categories))
    # predict the category for the test image
    Y_pred_num = clf.predict(X_test)
    #printing
    for i in len(Y_pred_num):
        filename = image_paths[i].replace(path,'')
        print filename[1:]+ ' '*6 + cate_map[Y_pred_num[i]]