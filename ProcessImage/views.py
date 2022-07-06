from django.shortcuts import render
from .forms import ResolutionImageForm, LightImageForm
import numpy as np
import cv2
from PIL import Image
import tensorflow as tf
import os
import sys
from pathlib import Path
import json


ResolutionEnhancerPath = os.path.join(os.getcwd(),'ProcessImage','ResolutionEnhancer')
LightEnhancerPath = os.path.join(os.getcwd(),'ProcessImage','LightEnhancer')
ResolutionEnhancer = ''
LightEnhancer = ''

currentDir = os.getcwd()

def index(request):
    global ResolutionEnhancer
    global LightEnhancer
    if ResolutionEnhancer and LightEnhancer:
        pass
    else:
        ResolutionEnhancer = tf.keras.models.load_model( ResolutionEnhancerPath, compile=False)
        LightEnhancer = tf.keras.models.load_model(LightEnhancerPath, compile=False)
    if request.method == 'POST':
        print(request)
        print(request.POST['image_type'])
        if request.POST['image_type'] == "light":
            light_form = LightImageForm(request.POST, request.FILES)
            resolution_form = ResolutionImageForm()
            if light_form.is_valid():
                light_form.save()

                img_object = light_form.instance
                image_name = str(img_object.image.url.split('/')[-1])
                image_path = os.path.join(currentDir,'media\images',image_name)
                image = cv2.imread( image_path )            
                image = cv2.resize(image, (256,256))
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                image = image.astype("float32") / 255.0

                light_image = LightEnhancer.predict(np.expand_dims(image, axis=0))
                light_image = light_image[0] * 255
                light_image = light_image.astype(np.uint8)            
                image = image * 255
                image = image.astype(np.uint8)            
                new_url = img_object.image.url.split('.')[0]+"_processed."+img_object.image.url.split('.')[-1]
                new_url_path = image_path.split('.')[0]+"_processed."+image_path.split('.')[-1]
                Image.fromarray(light_image).save(new_url_path)
                Image.fromarray(image).save(image_path)

                list_json_file = open(os.path.join(currentDir,'media','imageList.json'),'r')
                imageList = json.load(list_json_file)
                imageList["lightImage"][img_object.image.url] = new_url
                image_dict = {
                    "lowLightImage" : imageList['lightImage'].keys(),
                    "highLightImage" : imageList['lightImage'].values(),
                    "lowResolutionImage" : imageList['resolutionImage'].keys(),
                    "highResolutionImage" : imageList['resolutionImage'].values()
                }
                list_json_file.close()
                list_json_file = open(os.path.join(currentDir,'media','imageList.json'),'w')
                json_imageList = json.dumps(imageList, indent=4)
                list_json_file.write(json_imageList)
                list_json_file.close()
                return render(request, 'index.html', 
                    {
                        'resolution_form':resolution_form, 
                        'light_form' : light_form,
                        'image_dict' : image_dict
                    }
                )
        else:
            resolution_form = ResolutionImageForm(request.POST, request.FILES)
            light_form = LightImageForm()
            if resolution_form.is_valid():
                resolution_form.save()

                img_object = resolution_form.instance
                image_name = str(img_object.image.url.split('/')[-1])
                image_path = os.path.join(currentDir,'media\images',image_name)
                image = cv2.imread( image_path )            
                image = cv2.resize(image, (256,256))
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                image = image.astype("float32") / 255.0

                higher_res_image = ResolutionEnhancer.predict(np.expand_dims(image, axis=0))
                higher_res_image = higher_res_image[0] * 255
                higher_res_image = higher_res_image.astype(np.uint8)            
                image = image * 255
                image = image.astype(np.uint8)            
                new_url = img_object.image.url.split('.')[0]+"_processed."+img_object.image.url.split('.')[-1]
                new_url_path = image_path.split('.')[0]+"_processed."+image_path.split('.')[-1]
                Image.fromarray(higher_res_image).save(new_url_path)
                Image.fromarray(image).save(image_path)

                list_json_file = open(os.path.join(currentDir,'media','imageList.json'),'r')
                imageList = json.load(list_json_file)
                imageList["resolutionImage"][img_object.image.url] = new_url
                image_dict = {
                    "lowLightImage" : imageList['lightImage'].keys(),
                    "highLightImage" : imageList['lightImage'].values(),
                    "lowResolutionImage" : imageList['resolutionImage'].keys(),
                    "highResolutionImage" : imageList['resolutionImage'].values()
                }
                list_json_file.close()
                list_json_file = open(os.path.join(currentDir,'media','imageList.json'),'w')
                json_imageList = json.dumps(imageList, indent=4)
                list_json_file.write(json_imageList)
                list_json_file.close()

                return render(request, 'index.html', 
                    {
                        'resolution_form':resolution_form, 
                        'light_form' : light_form,
                        'image_dict' : image_dict
                    }
                )
    else:
        resolution_form = ResolutionImageForm()
        light_form = LightImageForm()
        list_json_file = open(os.path.join(currentDir,'media','imageList.json'),'r')
        imageList = json.load(list_json_file)

        image_dict = {
            "lowLightImage" : imageList['lightImage'].keys(),
            "highLightImage" : imageList['lightImage'].values(),
            "lowResolutionImage" : imageList['resolutionImage'].keys(),
            "highResolutionImage" : imageList['resolutionImage'].values()
        }

        list_json_file.close()


    return render(request, 'index.html', 
        {
            'resolution_form':resolution_form,
            'light_form' : light_form,
            'image_dict' : image_dict
        }
    )
