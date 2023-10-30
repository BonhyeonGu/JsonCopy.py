import json
import os
import time
import schedule

pathJson = "./copy.json"
proTime = 

def readJsonMap(path_mapping: str):
    with open(path_mapping, 'r', encoding='utf-8') as f:
        jsonMap = json.load(f)
    return jsonMap

def subPro():
    copyJson = readJsonMap(pathJson)
    
def main():
    schedule.every().day.at("13:00").do(run_my_program)

if __name__ == "__main__":
