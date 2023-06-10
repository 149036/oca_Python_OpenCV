#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2 


# In[2]:


data = cv2.VideoCapture('./sample.mp4')


# In[3]:


#type(data)


# In[4]:


#data.isOpened()


# In[5]:


def movie(data):
    while 1:
        ret, frame = data.read()
        if ret:
            cv2.imshow('sample data', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            data.set(cv2.CAP_PROP_POS_FRAMES, 0)
    cv2.destroyWindow('sample data')


# In[ ]:


movie(data)

