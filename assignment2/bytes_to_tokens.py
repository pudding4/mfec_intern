# Assignment 2:
# จากโจทย์เดิมให้เปลี่ยนจาก chunk ละประมาณ 1K bytes เป็น chunk ละประมาณ 1K tokens

import tiktoken
import sys
# temporary insertion of path so we can use function "chunks" from another folder
sys.path.insert(0, '/mnt/c/Users/User/OneDriveWork/Desktop/mfec_intern/assignment1') 
from chunking_text import chunks

# scaling the bytes so that the tokenization can reach approximately 1000
SCALE = 1.1
chunks.__defaults__ = (chunks.__defaults__[0]*SCALE,) 

# functions for counting number of tokens from a string
def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """ Return the number of tokens in a text string. """
    encoding = tiktoken.encoding_for_model(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

# main function for 1000 bytes to 1000 tokens
def bytes_to_tokens(text):
    encoding_name = 'gpt-3.5-turbo'
    arr_bytes_chunk = chunks(text)
    final_arr = []
    # tokenized each string in the splitted array
    for token in arr_bytes_chunk:
        final_arr.append(num_tokens_from_string(token, encoding_name))
    return final_arr

if __name__ == "__main__":
    # This can be any text file 
    thai_text = 'test_text/dummy_text.txt'
    tokens = bytes_to_tokens(thai_text)
    print(tokens)
    
# Code summary
"""
I implemented the function called bytes_to_tokens(text) which takes in the parameter as text files and call the function chunks() from assignment1
chunks() will return an array of strings with each string sizing at 1000 bytes (by default)
I then loop through the array of string and tokenize each strings through the tiktoken library
the function num_token_from_string() returns the total number of tokens

The global SCALE variable is set to 1.1 where I then times it with the default value of 1000 which allow the tokenization to reach approximately 1000
without breaking any words. (Note: the value 1.1 allows the token to reach closest to 1000 tokens)

Test Output: [1029, 997, 1011, 1042, 1037, 1031, 46]
The bytes_to_tokens function returns an array of the total number of tokens from the strings.
"""



