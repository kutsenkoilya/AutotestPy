# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 10:47:28 2020

@author: kompich
"""

import os
from selenium import webdriver

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
element.send_keys(file_path)