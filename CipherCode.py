alphabets = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
    "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
] #dataset


def alphaPos(alphabet): #function to determine the position of each letter in the message
    for i in range(len(alphabets)):
        if alphabets[i] == alphabet:
            return i

repeat = "yes"

while repeat == 'yes':
  crypt = input(
      "Type what you want to do? If encrypt, type 'encode';\nif decrypt, type 'decode':\n"
  ).lower()
  while (crypt != 'encode' and crypt != 'decode'):
      print("You have entered the wrong input, please try again.")
      crypt = input(
          "Type what do you want to do? If encrypt, type 'encode';\nif decrypt, type 'decode':\n"
      )

  msg = input("Type your message:\n").lower()

  shift = int(input("By what amount you want to shift each letter?\n"))
  if shift >= 26:
      shift = shift % 26
  else:
      shift = shift

  eMsg = ""
  dMsg = ""
  if crypt == 'encode': #encryption of message
        for letter in msg:
            if letter in alphabets:    
              rePos = alphaPos(letter)
              enPos = rePos + shift
              if enPos > 26:
                enPos = enPos - 26
              eMsg += alphabets[enPos]
            else:
                eMsg += letter
      print(eMsg)
  elif crypt == 'decrypt': #decryption of message
      for letter in msg:
            if letter in alphabets:
              rePos = alphaPos(letter)
              dePos = rePos - shift
              if dePos < 0:
                dePos = 26 + dePos
              else:
                dePos = dePos
              dMsg += alphabets[dePos]
            else:
                dMsg += letter
      print(dMsg)

  repeat = input("You wanna cipher/decipher a message? Types yes or no:\n").lower() #whether to repeat the loop or not
  while (repeat != 'yes') and (repeat != 'no'):
    repeat = input("Please type correct input.\nYou wanna cipher/decipher a message? Types yes or no:\n").lower()
  if repeat == "no":
    print("Thank you for using the cipher.\nHave a good day!")
