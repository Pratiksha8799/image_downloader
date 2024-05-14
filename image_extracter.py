# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 18:47:52 2024

@author: user
"""
import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import os
import regex as re
import time


class Image_Extraction:
    def __init__(self):
        pass
    
    def download_images(self,search_query,num_images):
        # search_query = 'Cat'
        # num_images = 2
        print('Extraction code started....')
        pattern = re.compile(r'^https://')
        imag_lis = []
    
        # Create a directory to store the images
        directory = search_query.replace(" ", "_")
        if not os.path.exists(directory):
            os.makedirs(directory)
    
        # Construct the Google Images URL
        url = f"https://www.google.com/search?q={search_query}&tbm=isch"
    
        # Send a GET request to the URL
        response = requests.get(url)
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find all img tags with class 'rg_i'
        image_tags = soup.find_all("img")
        
        for i in image_tags:
            src = i.get('src')
            if src:
                imag_lis.append(src)
            
        imag_lis = list(filter(pattern.match, imag_lis))
        
        imag_lis = imag_lis[:num_images]
        
        for index, img_url in enumerate(imag_lis):
            try:
                # # Set the maximum size for image resizing
                # max_size = (400, 400)
                
                # Send a GET request to the URL to download the image
                response = requests.get(img_url)
                time.sleep(1)
                # Check if the request was successful (status code 200)
                if response.status_code == 200:
                    # Open the image using PIL
                    image = Image.open(BytesIO(response.content))
                    
                    # Resize the image to reduce resolution
                    # image.thumbnail(max_size)
        
                    # Save the resized image to the specified output path
                    image.save(f'{directory}/{directory}_{index+1}.jpg')
        
                    print(f"Image downloaded successfully: {directory}_{index+1}")
                else:
                    print(f"Failed to download image: {url}")
            except Exception as e:
                print(f"Error: {e}")
        


