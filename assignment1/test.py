from chunking_text import chunks, bytes_array

def test_chunk_10B():
    # mocking the word_tokenize function
    list = ["สวัสดี", "ล้ม", "ลง", "รักษา", "ขอบ","คุณ", "เดิน","ทาง", "รักษา","หมา", "ตลาด", "อร่อย", "ร้อน", "น้ำ"]
    expected_output = ["สวัสดีล้ม", "ลงรักษาขอบ", "คุณเดินทาง", "รักษาหมา", "ตลาดอร่อย", "ร้อนน้ำ"]
    # size will be 10B for the sake of testing
    output = chunks(list, size = 10)
    # to see the length of each output
    bytes_array(output)
    assert output == expected_output

def test_chunk_20B():
    # mocking the word_tokenize function
    list = ["สวัสดี", "ล้ม", "ลง", "รักษา", "ขอบ","คุณ", "เดิน", "ทาง", "รักษา","หมา", "ตลาด", "อร่อย", "ร้อน", "น้ำ"]
    expected_output = ["สวัสดีล้มลงรักษาขอบ", "คุณเดินทางรักษาหมา", "ตลาดอร่อยร้อนน้ำ"]
    # size will be 10B for the sake of testing
    output = chunks(list, size = 20)
    # to see the length of each output
    bytes_array(output)
    assert output == expected_output

if __name__ == "__main__":

    test_chunk_10B()
    print("Everything passed (10B)")
    test_chunk_20B()
    print("Everything passed (20B)")