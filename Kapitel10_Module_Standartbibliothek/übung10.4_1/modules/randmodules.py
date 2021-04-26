import random

def classicrand():
    return random.random()

def rolldice():
    return random.randint(0,6)

def randint(untergrenze = 0, obergrenze = 6):
    return random.randint(untergrenze,obergrenze)