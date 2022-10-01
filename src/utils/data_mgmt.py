import logging
from tqdm import tqdm
import random
import xml.etree.ElementTree as ET # To read xml file
import re


def process_posts(fd_in, fd_out_train, fd_out_test, target_tag, split):
    line_num = 1 #Starting line
    for line in tqdm(fd_in):
        try:
            # Here it is checking what should i take as test_data or train_data from whatever line it is reading and this decision taken by random.
            fd_out  = fd_out_train if random.random() > split else fd_out_test
            
            # Here we are trying to extract attributes from text
            attr = ET.fromstring(line).attrib #This will take the line and read the attributes of it

            pid =  attr.get("Id", "")
            label = 1 if target_tag in attr.get("Tags", "") else 0
            title = re.sub(r"\s+"," ",attr.get("Title","")).strip() # strip will remove extra spaces from front and back of the title and for in between space we will make use of regex
            body = re.sub(r"\s+"," ",attr.get("Body","")).strip() # regex "\s" means a space and "\s+" means more than one pace which we are replacing with single space if present while extracting title
            text = f"{title} {body}" # title + " " + body
            fd_out.write(f"{pid}\t{label}\t{text}\n")
            line_num += 1
        except Exception as e:
            msg = f"Skipping the broken line {line_num}: {e}\n"
            logging.exception(msg)