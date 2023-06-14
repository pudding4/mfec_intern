# ส่วน assignment ตอนนี้ ลองทำ python code โดยหา text ภาษาไทย ขนาดประมาณ 20K bytes โจทย์คือให้แบ่ง text เป็น 
# chunks ขนาด chunk ละประมาณ 1K bytes แต่มีข้อจำกัดว่าถ้าการตัดแบ่ง chunk ทำให้เกิดการ "แยกคำ" ให้เลื่อนจุดตัดแบ่งไปยัง 
# boundary ของคำ โดยจะทำให้ขนาดของ chunk เพิ่มหรือลดจาก 1K bytes ไปอีกเล็กน้อยก็ได้

# 20k size text documents and separate the text into chunks of 1k bytes
# If the chunks results in the separation of words, move the splitting location to the boundary of the word
# and pad or de-pad the resulting chunk
# note that the chunk can be a little bit over or under the 1k bytes since splitting will always occur

import pythainlp
from pythainlp import sent_tokenize

# This can be any text file 
thai_text = 'text.txt'

# function for counting total number of characters in text
def count(list):
    total = 0
    for characters in list:
        total = total + len(characters)
    return total

# function for splitting the content of the file into 1000 (1KB)
# returns a list of 1k bytes
def chunks(list, size = 1000):
    total = 0
    final_chunks = [] # will be split into array of 1kb 
    chunk_1k_string = ""

    for snippet in list:
        
        if (total < size):
            #print(len(chunk_1k_string))
            total = total + len(snippet)
            chunk_1k_string = chunk_1k_string + snippet
        else:
            final_chunks.append(chunk_1k_string + snippet)
            total = 0
            chunk_1k_string = ""  

    # append the final chunk (which most likely will be less than 1KB) to the end of the list
    final_chunks.append(chunk_1k_string)
    #print(len("".join(str(x) for x in final_chunks)))
    #print(final_chunks)
    return final_chunks
    
content = '' # will contain whitespaces
# open and read in the content of the text file
with open(thai_text) as f:
    content = f.read()

# will only run as a script and will not be run through imports
if __name__ == "__main__":

    # content from the file gets tokenized 
    # whitespaces and newlines will always viewed as a word boundary
    list_of_content = sent_tokenize(content, engine="whitespace+newline")
    one_kb_arr = chunks(list_of_content)
    print(one_kb_arr)

f.close() # close the file