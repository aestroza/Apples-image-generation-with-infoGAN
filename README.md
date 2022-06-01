# Apples-image-generation-with-infoGAN

Repo where I generate images of different types of apples with infoGAN (controlled type of apple generated). This project was originally a homework for a Deep Leaning course I took at my University, here I've tried to make a cleaner version of it.

I trained a model that worked with 32x32 images and trained for 40000 training steps, the size is small due to computer power limitations. The original data set has 13 types of apples, but here I have used only 4 types of apples, this time is mainly for simplicity, but the full 13 categories can also be implemented. 

Here I showcase some of the generated images.

- Apple Red Delicious
![generated_delicious_red](https://user-images.githubusercontent.com/65049620/171448646-caa47789-1a1e-4124-8db0-e894520a4c1a.png)

- Apple Granny Smith
![generated_granny_smith](https://user-images.githubusercontent.com/65049620/171448663-6883b79c-76f0-4646-9ddd-2f91fc226497.png)

- Apple Golden 1
![generated_golden_1](https://user-images.githubusercontent.com/65049620/171448675-18c08726-1cfd-4365-8e3f-1e1f2c3b4a5d.png)

- Apple Braeburn
![generated_braeburn](https://user-images.githubusercontent.com/65049620/171449283-2b8c89c3-d839-42f5-8c45-54b877391193.png)

The apple images are from the "Fruits 360" dataset available on [Kaggle Here](https://www.kaggle.com/datasets/moltean/fruits)

The info folder and the infogan_rgb file are mainly the code from Rowel Atienza, [see original files here](https://github.com/PacktPublishing/Advanced-Deep-Learning-with-Keras). I have modified it a little to work with RGB images, and to also accept more parameters as inputs in some functions in order to have more control over it.
