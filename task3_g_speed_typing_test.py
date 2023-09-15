
"""
Created on Tue Sep  5 20:37:34 2023

@author: M.Nasir
"""
# Typing speed test

import time

start_time = time.time()
print(f"Start Time:{start_time:.2f}")
original_paragraph = """In a real application, you would integrate this logic 
                      into your typing speed tester program. """
print(original_paragraph)                      

original_words = original_paragraph.split()                                 
      
user_input= input("Type above paragraph: \n")
end_time = time.time()
print(f"Start Time:{end_time:.2f}")
typed_words = user_input.split()
length_of_typed_words = len(typed_words)
elapsed_time = end_time - start_time
words_per_second = (length_of_typed_words / elapsed_time)
words_per_minute = (length_of_typed_words / elapsed_time) * 60
characters_per_second = (len(user_input) / elapsed_time)
characters_per_minute = (len(user_input) / elapsed_time) * 60
print(f"Elapsed Time: {elapsed_time:.2f} seconds")
print(f"Words Typed: {length_of_typed_words}")
print(f"typing speed Characters_Per_Second(CPS) is: {characters_per_second:.2f}" )
print(f"typing speed Characters_Per_Minute(CPM) is: {characters_per_minute:.2f}" )
print(f"typing speed Words_Per_Second(WPS) is: {words_per_second:.2f}" )
print(f"typing speed Words_Per_Minute(WPM) is: {words_per_minute:.2f}" )
