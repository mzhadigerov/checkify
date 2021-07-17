import json
import logging as log
from pathlib import Path

import fitz
import pdfplumber
from predict import run_prediction

MODEL_DIR = './models/roberta-base/'
DATA_FOLDER = './data/'


with open(DATA_FOLDER + 'questions.json', 'r') as f:
    QUESTIONS = json.load(f)

def jsonFileName(path):
    """Retrieves file name from path and substitutes its extension to json"""
    fileName = path.split('/')[-1]
    return fileName.split('.')[0] + '.json'

def isPdf(path):
    """True if file is pdf, else False"""
    return path.endswith('.pdf')

def isContractChecked(path):
    """True if it is already checked, else False"""
    fileName = jsonFileName(path)
    file = Path(DATA_FOLDER + fileName)
    return file.is_file()

def isSearchablePdf(path):
    """True if pdf is searchable, else False"""
    with pdfplumber.open(path) as f:
        page = f.pages[0]
        text = page.extract_text()
    if text is None:
        return False
    return True

def pdfText(path):
    """Retrieves text from searchable pdf"""
    pdfText = ''
    doc = fitz.open(path)
    for page in doc:
        pdfText += page.getText()
    doc.close()
    return pdfText

def questions2answers(predictions, clean = False):
    """Maps questions from questions.json to predicted answers
    clean: clean postfix from questions
    """
    checkedContract = {}
    for i, p in enumerate(predictions):
        question = QUESTIONS[i]
        if clean:
            question = question.split('Details: ', 1)[1]
        checkedContract[question] = predictions[p]
    return checkedContract


def getCheckedContract(path = None, contract = None):
    """Returns existing checked contract if the contract exists, else predicts answers and returns the contract"""
    if path is not None:
        path = DATA_FOLDER + jsonFileName(path)
        with open(path, 'r', encoding = 'utf-8') as f:
            return json.load(f)
    elif contract is not None:
        predictions = run_prediction(QUESTIONS, contract, MODEL_DIR)
        return questions2answers(predictions, True)
    else:
        err = 'Either path or contract must have a value'
        log.error(err)
        raise Exception(err)

def storeContract(path, contract):
    """Stores contract as in given path"""
    if not isinstance(contract, dict):
        err = 'Contract must be of type dict'
        log.error(err)
        raise Exception(err)
    path = DATA_FOLDER + jsonFileName(path)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(contract, f, ensure_ascii=False, indent=4)

