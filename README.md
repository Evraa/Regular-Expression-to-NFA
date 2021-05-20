# RE to NFA using Thompson's algorithm
Steps adopted:

    1- Validate the correctness of the RE.
    2- Parse the RE with rounded brackets.
    3- Convert the parsed RE into states.
    4- Jsonify the states.
    5- Create a graphical visualization of the NFA produced.

## How to run
1. Install the required libraries
    ```shell
    pip install re
    pip install graphviz
    ```
2. for linux: install graphiz on your local path
    ```
        sudo apt-get install graphviz
    ```
3. To run
    ```shell
    python main,py
    ```  


## Documentation link for assumptions
[link](https://docs.google.com/document/d/1EZeWb3oIqYZfdo28vllwxE7rJ9fTHSisLDYjm2j82LI/edit?usp=sharing)