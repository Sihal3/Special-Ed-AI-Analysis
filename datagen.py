#!/usr/bin/env python
# coding: utf-8

# In[16]:


studentIDs = []
genders = []
ages = []
creds = []
csizes = []
gpas = []
disability = []
accoms = []
possibled = ["Auditory Disability", "Visual Disability", "Autism", "Low Emotional Intelligence", "Dyslexia", "ADHD", "Down Syndrome", "Reading Disability", "Mathematics Disability", "Speaking Disability", "Developmentally Delayed"]
possiblea = ["Materials in Braille", "Text to Speech Devices", "Breakout Corner", "Use of Toy in Class", "Bigger Print Materials", "Isolated Workstation", "Tutoring Sessions", "Book Buddy", "Use of Calculator on Tests", "AAC Devices", "Special Education Classroom"]
import pandas as pd


# In[ ]:


def datagen(num_values):
    dframe = pd.DataFrame()
    dframe["studentIDs"] = studentidgen(num_values)
    dframe['gender'] = gendergen(num_values)
    dframe['age'] = agegen(num_values)
    dframe['teacher_cred'] = credgen(num_values)
    dframe['class_size'] = csizegen(num_values)
    dframe['disability'] = disabilitygen(num_values)
    dframe['accomadation'] = accomgen(num_values)
    dframe['gpadifference'] = gpagen(num_values)
    return dframe


# In[17]:



def studentidgen(num):
    global studentIDs
    from random import shuffle
    studentIDs = list(range(10000, 10000+num*2))
    shuffle(studentIDs)
    return studentIDs[:num]


# In[18]:


def gendergen(num):
    global genders
    genders = []
    from random import random

    for i in range(num):
        gender = (int)(random()*2)
        if gender == 1:
            gender = 'Male';
        else:
            gender = 'Female'
        genders.append(gender)
    return genders


# In[19]:


def agegen(num):
    global ages
    from random import randint
    ages = []
    for i in range(num):
        age = randint(6, 18)
        ages.append(age)
    return ages


# In[20]:


def credgen(num):
    global creds
    from random import randint
    creds = []
    for i in range(num):
        cred = randint(0, 3)
        if cred == 0:
            cred = 'Associate\'s'
        elif cred == 1:
            cred = 'Bachelor\'s'
        elif cred == 2:
            cred = 'Master\'s'
        else:
            cred = 'PhD'
        creds.append(cred)
    return creds


# In[21]:


def csizegen(num):
    global csizes
    import numpy as np
    csizes = []
    for i in np.random.normal(30, 5, num):
        csizes.append(int(i))
    return csizes


# In[25]:
def disabilitygen(num):
    global disability
    from random import randint
    disability = []
    for i in range(num):
        d = randint(0, len(possibled)-1)
        disability.append(possibled[d])
    return disability

def accomgen(num):
    global accoms
    from random import randint
    accoms = []
    for i in range(num):
        a = randint(0, len(possiblea)-1)
        accoms.append(possiblea[a])
    return accoms

def gpagen(num):
#     negative impact for bigger classroom sizes 
    global gpas
    gpas = []
    from random import random
    from sklearn.preprocessing import scale
    from numpy import clip
    for i in range(num):
        class_size_contrib = -0.5*((csizes[i]-20)/10)
        if creds[i] == "Associate's":
            cred_contrib = -0.2
        elif creds[i] == "Bachelor's":
            cred_contrib = 0.3
        elif creds[i] == "Master's":
            cred_contrib = 0.9
        else:
            cred_contrib = 1.5
        if genders[i] == "Male" and ages[i] < 13:
            gendage_contrib = -0.4
        elif genders[i] == "Male" and ages[i] >= 13:
            gendage_contrib = 0.3
        elif genders[i] == "Female" and ages[i] >= 13:
            gendage_contrib = -0.2
        else:
            gendage_contrib = 0.6
        da_contrib = (-1*abs(possibled.index(disability[i]) - possiblea.index(accoms[i]))+3)*0.5
        gpa = class_size_contrib + gendage_contrib + cred_contrib + da_contrib + random()*2
        gpas.append(gpa)
    gpas = clip((scale(gpas)*1)+0.4, -4, 4)
    return gpas


# In[ ]:




