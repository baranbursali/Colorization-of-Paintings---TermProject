# Colorization-of-Paintings---TermProject


<b>INTRODUCTION</b><br>
Coloring grayscale images without human need by using various algorithms and methods is a area of research
in machine learning. In this project, we will revise some of the methods which are used for training and
validation purposes. We will inspect both convolutional neural networks (CNN) and generative adversarial
networks (GAN) strategies on colorizing grayscale painting images that is taken from Oxford Paintings Dataset.
It is difficult to obtain grayscale painting images in real world so we converted original RGB colored painting
images to intermediate LAB colored images then grayscale images and use these 2 different approach to find
out which model gives more accurate results on our conditions. Research contains epoch-loss, epoch-accuracy
plots for their related topic, accuracy and Delta-E calculations (which is used for understanding how the human
eye perceives color difference) on results and related works.While there are previous work of similar types of
networks on colorizations, they are not specific to paintings.

<img src="https://i.ibb.co/Vx7ZDPN/img.jpg" alt="Sample" ><br>

GAN:
There are 2 neural network model in Generative Adversarial Networks. These are “Generator” and
“Discriminator”. The generator takes the input and generates fake images as output. The discriminator takes 2
inputs, output generated by generator as its’ one input and original image as other input. It compares the fake
one and original and returns its’ output to generator. Discriminator returns 1 or 0 and it updates false parts of
generator’s fake image as 0. Both start learning from scratch so they learn together.
<br>
Loss function and according to it applying back propagation here is important, since it changes reliability of
training in significant manner.<br><br>
We downloaded our dataset from Oxford Paintings Dataset. 10.000 images are used for training and 2.000
images are used for validation and test purposes for GAN. All images are taken that converted to grayscale and
32x32 scaled images to make significant increase in training time.<br><br>
Our batch size were 32 fixed. Initial learning rate for the generator is 3e-4 and initial learning rate for the
discriminator is 6e-5. Learning rate is adjusted as:<br><br>
<i><b>lr = base_lr * (lr_decay_rate ** (global_step/lr_decay_steps))</b></i><br><br>
We used L1 loss function for generator and BCE loss function for discriminator.
L1 loss stands for Least Absolute Deviations a.k.a LAD.
BCE loss stands for Binary Cross Entropy. It is used for binary classification which is perfect for the
discriminator which is a neural network that have a binary output, 0 or 1.<br><br>
We trained our own model by using batch normalization but we also used some other model which is used
spectral normalization in the discriminator and trained its’ model with CIFAR10 dataset for our analysis. As
indicated, “ using spectral normalization in the discriminator network stabilized the training process and reduced
the number of required training steps”.<br><br>
In implementation we used Torch, OpenCV and Numpy libraries for most of the work.
First, we tried our training on our own PCs but the cost of training was huge and we migrated our work to
Google Colab. It gives us powerful GPU which is Tesla K80 GPU and enough storage for our work. We
connected our drive to the virtual machine and moved our input data to local storage of the computer for fixing
the network bottleneck problem we initially encountered. We used three checkpoints after 200, 466 and 666
epochs to check training progress.<br><br>
After we finished our training and validation, we analyzed our outputs for both our batch normalized model and
others’ spectral normalized model on Delta-E and LAB color based accuracy formula which are shown in
“Validation and Results” section.

<img src="https://i.ibb.co/NFkG420/Method-Page-1-1.png" alt="Method" ><br>

On a typical scale, the Delta E value will range from 0 to 100.<br><br>
Delta E Perception<br>
<= 1.0 Not perceptible by human eyes.<br>
1 - 2 Perceptible through close observation.<br>
2 - 10 Perceptible at a glance.<br>
11 - 49 Colors are more similar than opposite<br>
100 Colors are exact opposite<br>
<br>
Discriminator accuracy change in training by epochs<br>
<img src="https://i.ibb.co/HVffXwf/training-discriminator-accuracy.png" alt="Graph" ><br><br>
<img src="https://i.ibb.co/0XhVMVn/result.jpg" alt="Result" ><br>

Dataset : Elliot J. Crowley, Ernesto Coto and Andrew Zisserman, The Paintings Dataset, https://www.robots.ox.ac.uk/~vgg/data/paintings/, 2020
<br><strong>All GAN training process based on tuned and modified version of Károly Harsányi, Image colorization with GANs, https://github.com/karoly-hars/GAN_image_colorizing, 2020</strong>
