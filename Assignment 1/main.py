import argparse


def define_parameters():
    parser = argparse.ArgumentParser()

    parser.add_argument("--cipher_type", default="shift", type=str,
                        help="Cipher type should be shift , affine or vigenere")
    parser.add_argument("--operation_type", default="dec", type=str,
                        help="Operation type should be enc or dec")
    parser.add_argument("--input_file", default="input_file", type=str,
                        help="Path of the input file")
    parser.add_argument("--output_file", default="output_file", type=str,
                        help="Path of the output file")
    parser.add_argument("--encryption_keys", default=[7], type=list,
                        help="Path of the output file")
    return parser.parse_args()


args = define_parameters()
input_file = open(args.input_file, "r")
output_file = open(args.output_file, 'w')


def shift_encryption():
    if input_file.mode == 'r':
        plain_text = input_file.read()
        k = args.encryption_keys[0]
        input_lines = plain_text.split('\n')
        for line in input_lines:
            cipher_text = ""
            for i in range(len(line)):
                if line[i].isupper():
                    x = (ord(line[i]) - 65)
                    cipher_text += chr((((x + k) % 26) + 65))
                else:
                    x = (ord(line[i]) - 97)
                    cipher_text += chr((((x + k) % 26) + 97))
            output_file.write(cipher_text+"\n")


def affine_encryption():
    if input_file.mode == 'r':
        plain_text = input_file.read()
        a = args.encryption_keys[0]
        b = args.encryption_keys[1]
        input_lines = plain_text.split('\n')
        for line in input_lines:
            cipher_text = ""
            for i in range(len(line)):
                if line[i].isupper():
                    x = (ord(line[i]) - 65)
                    cipher_text += chr((((a * x + b) % 26) + 65))
                else:
                    x = (ord(line[i]) - 97)
                    cipher_text += chr((((a * x + b) % 26) + 97))

            output_file.write(cipher_text+"\n")


def vigenere_encryption():
    if input_file.mode == 'r':
        plain_text = input_file.read()
        input_lines=plain_text.split('\n')
        for line in input_lines :
            cipher_text=""
            keyword = args.encryption_keys
            for i in range(len(line) - len(keyword)):
                keyword+=keyword[i]
            for i in range(len(line)):
                if line[i].isupper() and keyword[i].isupper():
                    x = (ord(line[i]) - 65)
                    k = (ord(keyword[i]) - 65)
                    cipher_text += chr((((x + k) % 26) + 65))
                elif line[i].isupper() and keyword[i].islower():
                    x = (ord(line[i]) - 65)
                    k = (ord(keyword[i]) - 97)
                    cipher_text += chr((((x + k) % 26) + 65))
                elif line[i].islower() and keyword[i].isupper():
                    x = (ord(line[i]) - 97)
                    k = (ord(keyword[i]) - 65)
                    cipher_text += chr((((x + k) % 26) + 97))
                elif line[i].islower() and keyword[i].islower():
                    x = (ord(line[i]) - 97)
                    k = (ord(keyword[i]) - 97)
                    cipher_text += chr((((x + k) % 26) + 97))

            output_file.write(cipher_text+"\n")


def shift_decryption():
    if input_file.mode == 'r':
        cipher_text = input_file.read()
        k = args.encryption_keys[0]
        input_lines = cipher_text.split('\n')
        for line in input_lines:
            plain_text = ""
            for i in range(len(line)):
                if line[i].isupper():
                    y = (ord(line[i]) - 65)
                    plain_text += chr((((y -k +26) % 26) + 65))
                else:
                    y = (ord(line[i]) - 97)
                    plain_text += chr((((y -k+26) % 26) + 97))

            output_file.write(plain_text+"\n")


def affine_decryption():
    if input_file.mode == 'r':
        cipher_text = input_file.read()
        a = args.encryption_keys[0]
        b = args.encryption_keys[1]
        additive_inverse = 0
        multiplicative_inverse =0
        for i in range(1, 27):
            if (b + i) % 26 == 0:
                additive_inverse = i
            if (a * i) %26 ==1 :
                multiplicative_inverse=i

        input_lines = cipher_text.split('\n')
        for line in input_lines:
            plain_text = ""
            for i in range(len(line)):
                if line[i].isupper():
                    y = (ord(line[i]) - 65)
                    plain_text += chr((((multiplicative_inverse*(y+additive_inverse)) % 26) + 65))
                else:
                    y = (ord(line[i]) - 97)
                    plain_text += chr((((multiplicative_inverse*(y+additive_inverse)) % 26) + 97))
            output_file.write(plain_text+"\n")


def vigenere_decryption():
    if input_file.mode == 'r':
        cipher_text = input_file.read()
        input_lines = cipher_text.split('\n')
        for line in input_lines:
            plain_text = ""
            keyword = args.encryption_keys
            for i in range(len(line) - len(keyword)):
                keyword += keyword[i]
            for i in range(len(line)):
                if line[i].isupper() and keyword[i].isupper():
                    y = (ord(line[i]) - 65)
                    k = (ord(keyword[i]) - 65)
                    plain_text += chr((((y - k + 26) % 26) + 65))
                elif line[i].isupper() and keyword[i].islower():
                    y = (ord(line[i]) - 65)
                    k = (ord(keyword[i]) - 97)
                    plain_text += chr((((y - k + 26) % 26) + 65))
                elif line[i].islower() and keyword[i].isupper():
                    y = (ord(line[i]) - 97)
                    k = (ord(keyword[i]) - 65)
                    plain_text += chr((((y - k + 26) % 26) + 97))
                elif line[i].islower() and keyword[i].islower():
                    y = (ord(line[i]) - 97)
                    k = (ord(keyword[i]) - 97)
                    plain_text += chr((((y - k + 26) % 26) + 97))

            output_file.write(plain_text+"\n")


if __name__ == "__main__":

    if args.operation_type == "enc":
        if args.cipher_type == "shift":
            shift_encryption()
        elif args.cipher_type == "affine":
            affine_encryption()
        elif args.cipher_type == "vigenere":
            vigenere_encryption()
    elif args.operation_type == "dec":
        if args.cipher_type == "shift":
            shift_decryption()
        elif args.cipher_type == "affine":
            affine_decryption()
        elif args.cipher_type == "vigenere":
            vigenere_decryption()
