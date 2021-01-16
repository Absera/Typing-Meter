from utilities import *
import time
import sys

def play():
    random_words = open("files/words.txt", "r") if sys.argv[1] == "common" else open("files/random_words.txt", "r")
    random_word_r = random_words.readlines()

    amount_of_words = 0
    net_amount_of_words = 0
    slice1 = 0
    slice2 = 5
    typing_minutes = input("Wanna Type? Enter Minute(s): ")
    if 0 < int(typing_minutes) < 20:
        current_time = time.time()
        randomize(open("files/words.txt", "r").readlines(), open("files/random_words.txt", "w"))
        for word in random_word_r:
            word = word.strip()
            random_words_sliced = random_word_r[slice1:slice2]
            typed = input(strip_list(random_words_sliced) + strip_list([" | "]))
            if typed == "   ":
                break

            amount_of_words += len(typed.split(" "))
            slice1 = slice2
            slice2 = slice2 + 5

            # check word accuracy
            list_of_typed_words = typed.split(" ")
            list_of_words = list(map(lambda x: x.strip(), random_words_sliced))

            for t_word, l_word in zip(list_of_typed_words, list_of_words):
                if t_word == l_word:
                    net_amount_of_words += 1
            time_taken_on_progress = (time.time() - current_time) / 60
            if time_taken_on_progress >= float(typing_minutes):
                break

        time_taken = (time.time() - current_time) / 60
        print("\n")
        print("Typed Words: ", amount_of_words, "words")
        print("Net Words: ", net_amount_of_words, "words")
        print("Time Taken: ", split_float(time_taken), "minute(s)")
        print("WPM: ", split_float((net_amount_of_words / time_taken)), "words")
        time.sleep(3)
        if input("Pay Again? ") in [" yes", "yes", " y", "y"]:
            play()
        else:
            quit()
    else:
        print("Please Make Sure You Entered an Integer Between 1 and 20")


play()
