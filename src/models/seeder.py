from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Patent
import string
from itertools import product
import time

engine = create_engine("sqlite:///../database.db", echo=False)
Session = sessionmaker(engine)
session = Session()

def alphabet_creator_function():
    alphabet_list = [string.ascii_uppercase]*4
    digit_list = [string.digits]*3
    data = list()
    start_time = time.time()
    counter = 0
    for letter in product(*alphabet_list):
        if counter == 10000:
            break
        for digit in product(*digit_list):
            counter += 1
            print(counter)
            patent = "".join(letter+digit)
            session.add(Patent(number=patent))
            session.commit()
    result_time = time.time() - start_time
    print("--- %s seconds ---" %result_time)


if __name__ == '__main__':
    alphabet_creator_function()
    session.close()
