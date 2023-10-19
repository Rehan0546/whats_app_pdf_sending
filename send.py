#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 15:04:32 2023

@author: rehan
"""

# import pywhatkit as kit
import pandas as pd
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import time
import argparse
parser = argparse.ArgumentParser(
                    prog='send',
                    description='sending pdf to multiple numbers',
                    epilog='completed')

parser.add_argument('-msg', '--message',default='Here is pdf of....')      # option that takes a value
parser.add_argument('-pdf', '--pdf_path',default = '')  # on/off flag
parser.add_argument('-sleep', '--sleep_time',default=15)  # on/off flag
parser.add_argument('-excel', '--excel_path',default='numbers.xlsx')  # on/off flag
parser.add_argument('-try', '--tray_again',default=3)  # on/off flag

args = parser.parse_args()

# Your WhatsApp message and PDF file path
message = args.message
pdf_path = args.pdf_path
sleep_time = int(args.sleep_time)
# List of recipient phone numbers
phone_numbers = pd.read_excel(args.excel_path).iloc[:,0]
phone_numbers = ['+'+str(i) for i in phone_numbers]
total_numbers = len(phone_numbers)
print(phone_numbers)


print('loading...')
driver = webdriver.Chrome()

# Open WhatsApp Web and scan QR code manually
driver.get("https://web.whatsapp.com")
input("Scan the QR code and press Enter after logging in...")

def sending_msg(phone_numbers,
                message = message,
                pdf_path = pdf_path,
                sleep_time = sleep_time,
                driver = driver):

    # Send PDF to multiple numbers
    error_numbers = []
    for i, number in enumerate(phone_numbers):
        try:
            # Open a new chat with the recipient
            chat_url = f"https://web.whatsapp.com/send?phone={number}"
            driver.get(chat_url)
            time.sleep(sleep_time)
    

            # time.sleep(2)
            document_option = driver.find_element("xpath",'//div[@title="Type a message"]')
            document_option.click()
            document_option.send_keys(message)  # Replace with the path to your PDF file
            time.sleep(2)
            
            # Click the attachment button
            attachment_button = driver.find_element("xpath",'//div[@title="Attach"]')
            attachment_button.click()
            time.sleep(2)
            
            # Click on the document option
            document_option = driver.find_element("xpath",'//input[@accept="*"]')
            document_option.send_keys(pdf_path)  # Replace with the path to your PDF file
            # if i==0:
            #     time.sleep(sleep_time)
            
            # Wait for a few seconds to allow the file to upload
            time.sleep(sleep_time//3)
            # Click the send button
            send_button = driver.find_element("xpath",'//span[@data-icon="send"]')
            send_button.click()
            # if i==0:
            #     time.sleep(sleep_time)
            # else:
            time.sleep(5)
            
            
            print(f"sent message to {number}")
        except Exception as e:
            print(f"Failed to send message to {number}: {str(e)}")
            error_numbers.append(number)
    return error_numbers
print('sengind in progress...')
phone_numbers = sending_msg(phone_numbers)
if len(phone_numbers):
    for i in range(int(args.try_again)):
        phone_numbers = sending_msg(phone_numbers)
        if not len(phone_numbers):
            break
        
# Close the browser window

if len(phone_numbers):
    with open('not_sent.txt', 'w') as filehandle:
        for listitem in phone_numbers:
            filehandle.write('%s\n' % listitem)
            
print(f'completed {total_numbers-len(phone_numbers)}/{total_numbers}')

driver.quit()
