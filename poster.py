from keys import *
import time

while True:
    list = "generated_sentences.txt"

    #Chooses and then removes first sentence in the list
    with open(list, 'r') as fin:
        data = fin.read().splitlines(True)
    with open(list, 'w') as fout:
        fout.writelines(data[1:])
    print(data[0])

    # tweeting!
    api.update_status(status=data[0])

    # waiting n hours before sending the next tweet
    hours = 1
    time.sleep(3600*hours)

