# ImageEnhancerWeb
ImageEnhancerWeb is a Convolutional Neural Network deployment on Django. It contain two model one enhance Low Light Image and other enhance Low Resolution Image.

## Dependencies
`Django==4.0.6`
`numpy==1.20.3`
`opencv_python==4.6.0.66`
`Pillow==9.2.0`
`tensorflow==2.7.0`


## Light Enhancer Result
#### Light Enhancer Model Result on Test Images
##### Model is working pretty well on Test Images. It is brighting up test images without distorting it.

#### Light Enhancer Model Result on Other Images
##### Model is not working that well on Other Images. It is brighting up images but also making some distortion.

## Resolution Enhancer Result
#### Resolution Enhancer Model Result on Test Images
##### Model is working pretty well on Test Images. It is making test images more clear without distorting it.

#### Resolution Enhancer Model Result on Other Images
##### Model is not working that well on Other Images. In some case it is making Image clear but it is also distorting it.
