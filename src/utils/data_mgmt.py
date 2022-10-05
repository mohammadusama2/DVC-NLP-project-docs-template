import logging
from tqdm import tqdm
import random
import xml.etree.ElementTree as ET # To read xml file
import re
import numpy as np
import scipy.sparse as sparse
import joblib


def process_posts(fd_in, fd_out_train, fd_out_test, target_tag, split):
    line_num = 1 #Starting line
    column_names = "pid\tlabel\ttext\n"
    fd_out_train.write(column_names)
    fd_out_test.write(column_names)
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

            
def save_matrix(df, text_matrix, out_path): #text_matrix is the tfidf matrix that we got
    pid_matrix = sparse.csr_matrix(df.pid.astype(np.int64)).T #We are transposing to make column matrix from row matrix
    label_matrix = sparse.csr_matrix(df.label.astype(np.int64)).T

    result = sparse.hstack([pid_matrix, label_matrix, text_matrix]) #horizontal stack of matrices
    
    msg = f"The output matrix saved at {out_path} of shape {result.shape}"
    logging.info(msg)
    joblib.dump(result, out_path)