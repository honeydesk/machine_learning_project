
from flask import Flask

import sys
from housing.exception import HousingException

from housing.logger import logging

app=Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    try:
        # created a custom exception intentionally
        raise Exception("We are testing custom exception")
    
    # created an object of housing custom exception class
    except Exception as e:
        # had we wanted to raise an exception here, we would have written:
        # this line of code:-> " raise HousingException(e,sys) from e "
        
        # rather here just want to log the error  
        housing = HousingException(e,sys)
       
        # trying to log this error message in the logging file
        logging.info(housing.error_message)
        logging.info("We are testing logging module")  

    return "Warid! you have established the CI/CD pipeline"


if __name__=="__main__":
    app.run(debug=True)


    