import sys

###########
# FUNÇÕES #
###########

def showHelp():
    print("""
        arguments: 
            -h | mostra a lista de argumentos
            -c "CRYPT" | mensagem a ser criptografada

            -d "DECRPT" | mesagem a ser decriptografada

            -k "KEY" | chave de criptografia 
    """)
    exit()

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def createFullKey(key, text):

    finalText = ""

    if len(key) < len(text):
        repeatAmount = len(text) // len(key)
        _repeatAmount = len(text) % len(key)

        finalText += key * repeatAmount
        
        finalText += key[0:_repeatAmount]

    return finalText

def formatText(text):
    return text.replace(" ", "")

##########
# CÓDIGO #
##########

operationType = 0
args = sys.argv[1:len(sys.argv)]

if "-h" in args:
    showHelp()

if "-k" in args:
    global rawKey
    rawKey = args[args.index("-k") + 1].upper()
else:
    showHelp()

if "-c" in args:
    global rawEncryptText
    rawEncryptText = args[args.index("-c") + 1].upper()

    operationType = 1

    if "-d" in args:
        showHelp()

elif "-d" in args:
    global rawDecryptText
    rawDecryptText = args[args.index("-d") + 1].upper()

    operationType = 2

else:
    showHelp()

if operationType == 1:

    encryptedText = ""

    keyText = createFullKey(rawKey, rawEncryptText)
    encryptText = formatText(rawEncryptText)

    for i in range(len(encryptText)):

        rotateAmount = alphabet.find(keyText[i])
        actualPosition = alphabet.find(encryptText[i])

        replacePotision = actualPosition - rotateAmount

        if(replacePotision < 0):
            __temp = rotateAmount - actualPosition
            replacePotision = len(alphabet) - __temp


        replaceChar = alphabet[replacePotision]

        encryptedText += replaceChar


    print(f"\nCódigo criptografado: {encryptedText}\nChave: {rawKey}\n")

elif operationType == 2:

    decryptedText = ""

    keyText = createFullKey(rawKey, rawDecryptText)
    decryptText = formatText(rawDecryptText)

    for i in range(len(decryptText)):

        rotateAmount = alphabet.find(keyText[i])
        actualPosition = alphabet.find(decryptText[i])

        replacePotision = actualPosition + rotateAmount

        if(replacePotision > len(alphabet) - 1):
            replacePotision = replacePotision - len(alphabet)

        replaceChar = alphabet[replacePotision]

        decryptedText += replaceChar

    print(f"\nCódigo decriptografado: {decryptedText}\nChave: {rawKey}\n")