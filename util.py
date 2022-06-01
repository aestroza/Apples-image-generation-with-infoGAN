import os
import natsort
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array


'Defino una funcion para obtener el "path" de cada imagen segun su categoria, junto con el nombre de las clases (carpetas) utilizo natsort para que queden ordenados como lo veo en la carpeta.'
def get_path_to_images(path):
    # Put files into lists and return them as one list of size 4
    # omito el 0 porque corresponde a la carpeta apple
    
    list_of_list_of_paths_to_img = []
    folders_names = []
    
    sub_folder_list = [x[0] for x in os.walk(path)][1:]
    for folder_path in sub_folder_list:
        list_of_list_of_paths_to_img.append(natsort.natsorted([os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('.jpg')]))
        folders_names.append(os.path.basename(os.path.normpath(folder_path)))
        
    return list_of_list_of_paths_to_img, folders_names


# Display one image
def display_one(a, title1 = "Original"):
    plt.imshow(a), plt.title(title1)
    plt.xticks([]), plt.yticks([])
    plt.show()
    
def display_one_gray(a, title1 = "Original"):
    plt.imshow(a, cmap='gray'), plt.title(title1)
    plt.xticks([]), plt.yticks([])
    plt.show()
    
# Display two images
def display_two(a, b, title1 = "Original", title2 = "Edited"):
    plt.subplot(121), plt.imshow(a), plt.title(title1)
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(b), plt.title(title2)
    plt.xticks([]), plt.yticks([])
    plt.show()
    
# Getting images resized to number_of_pixels x number_of_pixels  
def get_images(list_of_list_of_paths, number_of_pixels = None ):
    # if target_size = None -> load_img defaults to original size
    
    if number_of_pixels == None:
      target_size = None
    else:
      n = number_of_pixels
      target_size = (n,n)
    
    img_array = []
    
    for list_of_paths in list_of_list_of_paths:
        aux = []
        for path in list_of_paths:
            img = load_img(path, target_size=target_size)
            aux.append(img_to_array(img)/255.)    
        img_array.append(aux)
        display_one(aux[0])
    
    return img_array
 
    
def unison_shuffled_copies(a, b):
    assert len(a) == len(b)
    p = np.random.permutation(len(a))
    return a[p], b[p]
