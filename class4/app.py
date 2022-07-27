import streamlit as st
import boto3
from PIL import Image

st.title('Object Recognition System')

img_file=st.file_uploader('Upload the image',type=['png','jpg','jpeg'])

if img_file is not None:
    file_details={}
    file_details['name']=img_file.name
    file_details['type']=img_file.type
    file_details['size']=img_file.size

    st.write(file_details)

    with open('src.jpg','wb') as f:
        f.write(img_file.getbuffer())
    
    st.image(Image.open(img_file))

    client=boto3.client('rekognition')
    imageSource=open('src.jpg','rb')
    # RR - Request and Response
    response=client.detect_labels(
        Image={'Bytes':imageSource.read()}
    )
    #st.write(response)
    if response['Labels']:
        for i in response['Labels']:
            if i['Confidence']>80:
                st.success(i['Name']+ ','+ str(i['Confidence']))
