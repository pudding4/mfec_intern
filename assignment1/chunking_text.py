# ส่วน assignment ตอนนี้ ลองทำ python code โดยหา text ภาษาไทย ขนาดประมาณ 20K bytes โจทย์คือให้แบ่ง text เป็น 
# chunks ขนาด chunk ละประมาณ 1K bytes แต่มีข้อจำกัดว่าถ้าการตัดแบ่ง chunk ทำให้เกิดการ "แยกคำ" ให้เลื่อนจุดตัดแบ่งไปยัง 
# boundary ของคำ โดยจะทำให้ขนาดของ chunk เพิ่มหรือลดจาก 1K bytes ไปอีกเล็กน้อยก็ได้

# 20k size text documents and separate the text into chunks of 1k bytes
# If the chunks results in the separation of words, move the splitting location to the boundary of the word
# and pad or de-pad the resulting chunk
# note that the chunk can be a little bit over or under the 1k bytes since splitting will always occur

import pythainlp 
from pythainlp import word_tokenize

# print the length of each chunks
def bytes_array(arr):
    length_output = []
    for length in arr:
        length_output.append(len(length))
    print(length_output)

# function for counting total number of characters in text
def count(list):
    total = 0
    for characters in list:
        total = total + len(characters)
    return total

# function for splitting the content of the file into 1000 (1KB)
# returns a list of 1k bytes
def chunks(text_to_chunk, size = 1000):

    content = '' # will contain whitespaces
    # open and read in the content of the text file
    with open(text_to_chunk) as f:
        content = f.read()
    f.close()
    # content from the file gets tokenized by words
    tokenized_list = word_tokenize(content, keep_whitespace=False)

    total = 0
    final_chunks = [] # will be split into array of 1kb 
    chunk_1k_string = ""

    for snippet in tokenized_list:   

        if len(chunk_1k_string) + len(snippet) <= size: 
            total += len(snippet)
            chunk_1k_string += snippet
        
        else:
            final_chunks.append(chunk_1k_string) # + snippet
            total = len(snippet)
            chunk_1k_string = snippet

    # append the final chunk (which most likely will be less than 1KB) to the end of the list
    final_chunks.append(chunk_1k_string)

    # write to file everytime
    file = open("chunk_file", "w")
    for i in final_chunks:
        file.write(i + "\n\n\n")
    
    file.close()

    return final_chunks
    
# will only run as a script and will not be run through imports
if __name__ == "__main__":

    # This can be any text file 
    thai_text = 'dummy_text.txt'

    # default size of 1000
    chunked_text = chunks(thai_text) 
    bytes_array(chunked_text)
