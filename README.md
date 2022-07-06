# ImageEnhancerWeb :high_brightness:
ImageEnhancerWeb is a Convolutional Neural Network deployment on Django. It contain two model one enhance Low Light Image and other enhance Low Resolution Image. Architecture is proposed by [Paper](https://arxiv.org/pdf/2003.06792v2.pdf)

## Dependencies
`Django==4.0.6`
`numpy==1.20.3`
`opencv_python==4.6.0.66`
`Pillow==9.2.0`
`tensorflow==2.7.0`

<hr>

## Light Enhancer Result

![Light Enhancer Test Image](https://media.githubusercontent.com/media/riddhesh-jangid/ImageEnhancerWeb/main/media/images/778.png)![Light Enhancer Result Image](https://media.githubusercontent.com/media/riddhesh-jangid/ImageEnhancerWeb/main/media/images/778_processed.png)
<br>
![Light Enhancer Test Image](https://media.githubusercontent.com/media/riddhesh-jangid/ImageEnhancerWeb/main/media/images/111.png)![Light Enhancer Result Image](https://media.githubusercontent.com/media/riddhesh-jangid/ImageEnhancerWeb/main/media/images/111_processed.png)
<br>
![Light Enhancer Test Image](https://media.githubusercontent.com/media/riddhesh-jangid/ImageEnhancerWeb/main/media/images/780.png)![Light Enhancer Result Image](https://media.githubusercontent.com/media/riddhesh-jangid/ImageEnhancerWeb/main/media/images/780_processed.png)

```
Light Enhancer Model Result on Test Images
- Model is working pretty well on Test Images. It is brighting up test images without distorting it.

Light Enhancer Model Result on Other Images
- Model is not working that well on Other Images. It is brighting up images but also making some distortion.
```

<hr>

## Resolution Enhancer Result

![Light Enhancer Test Image](https://media.githubusercontent.com/media/riddhesh-jangid/ImageEnhancerWeb/main/media/images/7.png)![Light Enhancer Result Image](https://media.githubusercontent.com/media/riddhesh-jangid/ImageEnhancerWeb/main/media/images/7_processed.png)
<br>
![Light Enhancer Test Image](https://media.githubusercontent.com/media/riddhesh-jangid/ImageEnhancerWeb/main/media/images/5.png)![Light Enhancer Result Image](https://media.githubusercontent.com/media/riddhesh-jangid/ImageEnhancerWeb/main/media/images/5_processed.png)
<br>
![Light Enhancer Test Image](https://media.githubusercontent.com/media/riddhesh-jangid/ImageEnhancerWeb/main/media/images/13.png)![Light Enhancer Result Image](https://media.githubusercontent.com/media/riddhesh-jangid/ImageEnhancerWeb/main/media/images/13_processed.png)


```
Resolution Enhancer Model Result on Test Images
- Model is working pretty well on Test Images. It is making test images more clear without distorting it.

Resolution Enhancer Model Result on Other Images
- Model is not working that well on Other Images. In some case it is making Image clear but it is also distorting it.
```
