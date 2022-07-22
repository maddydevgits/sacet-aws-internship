import streamlit as st
import boto3
from PIL import Image # pip install pillow

st.title('Amazon Lens using Rekognition')

img_file=st.file_uploader('Upload the Image',type=['png','jpg','jpeg'])

if img_file is not None:
    file_details={}
    file_details['type']=img_file.type
    file_details['name']=img_file.name
    file_details['size']=img_file.size
    st.write(file_details)
    st.image(Image.open(img_file),width=250)

    with open('src.jpg','wb') as f:
        f.write(img_file.getbuffer())
    
    client=boto3.client('rekognition')
    imageSource=open('src.jpg','rb')
    response=client.detect_text(Image={'Bytes':imageSource.read()})
    #st.write(response)
    if response['TextDetections']:
        for i in response['TextDetections']:
            if i['Type']=='LINE':
                st.write(i['DetectedText'])
