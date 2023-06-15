from chunking_text import chunks, bytes_array
import unittest

test_text = 'test_text/test_txt'

class testChunk(unittest.TestCase):

    def test_chunk_10B(self):
        # mocking the word_tokenize function
        # list = ["สวัสดี", "ล้ม", "ลง", "รักษา", "ขอบ","คุณ", "เดิน","ทาง", "รักษา","หมา", "ตลาด", "อร่อย", "ร้อน", "น้ำ"]
        expected_output = ["สวัสดีล้ม", "ลงรักษาขอบ", "คุณเดินทาง", "รักษาหมา", "ตลาดอร่อย", "ร้อนน้ำ"]
        # size will be 10B for the sake of testing
        output = chunks(test_text, size = 10)
        # to see the length of each output
        print(output)
        bytes_array(output)
        self.assertEqual(output, expected_output)

    def test_chunk_20B(self):
        # mocking the word_tokenize function
        # list = ["สวัสดี", "ล้ม", "ลง", "รักษา", "ขอบ","คุณ", "เดิน", "ทาง", "รักษา","หมา", "ตลาด", "อร่อย", "ร้อน", "น้ำ"]
        expected_output = ["สวัสดีล้มลงรักษาขอบ", "คุณเดินทางรักษาหมา", "ตลาดอร่อยร้อนน้ำ"]
        # size will be 20B for the sake of testing
        output = chunks(test_text, size = 20)
        # to see the length of each output
        print(output)
        bytes_array(output)
        self.assertEqual(output, expected_output)

if __name__ == "__main__":

    unittest.main()