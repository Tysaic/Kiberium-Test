from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Patent
import string
from itertools import product
import time

engine = create_engine("mysql+pymysql://kiberium:root1234@localhost/kiberium_db", echo=False)
Session = sessionmaker(engine)
session = Session()

def alphabet_creator_function():
    alphabet_list = [string.ascii_uppercase]*4
    digit_list = [string.digits]*3
    data = list()
    start_time = time.time()
    for letter in product(*alphabet_list):
        for digit in product(*digit_list):
            patent = "".join(letter+digit)
            session.add(Patent(number=patent))
            session.commit()
            #yield delta
    result_time = time.time() - start_time
    print("--- %s seconds ---" %result_time)


if __name__ == '__main__':
    alphabet_creator_function()
    session.close()
