# kogan_test
 Tested on Mac OS X 
# To run:
1. If you have docker installed 
    ```docker-compose up ``` should start the API running at localhost:4000 
2. Otherwise 

    - Install requirements in app
    - Inside app folder run python run.py

Both method should start a local api at 4000 port

# API endpoints
    default --> calculates weight for "Air Conditioners"
    /<category> --> caculates weight for category if given

** Note that code does not throw any error if the category does not exist rather it just says the weight is 0. 
