Features:
1. row number of the image
2. column number of the image
This just tells us the size of the image. Might be useful, might be not…

3. the mean value in red layer
4. the mean value in green layer
5. the mean value in blue layer
6. the mean value in grey(flattened) layer
These tell us the average value in each color

7. the value has the most count in red layer
8. the value has the most count in green layer
9. the value has the most count in blue layer
10. the value has the most count in gray layer
These tell us the most probable value in each color.

11. total length of the edges after Canny filter
12. total length of the edges after horizonal sobel filter
13. total length of the edges after vertical sobel filter
14. total length of the edges after 2d sobel filter
15. sum the result of houghLine transform
These tell us something about the geometry

Result:
The data are still being trained at 5 pm. No result yet.
The random guessing will give an accuracy of 2%.

Running files:
'hw4_training.ipynb' is the script written for training the data. 

'trained_classifier.p' should contain the classifier file. But the training is not done yet. I will upload it to git as soon as it is done.

'run_final_classifier.ipynb' is the script to give prediction on the new images. You can run it in ipython notebook by run_final_classifier(path) after running the function.

'categories.p' is the file contain a dict descibing the categories. Please download it to the same folder as run_final_classifier.ipynb before running it.