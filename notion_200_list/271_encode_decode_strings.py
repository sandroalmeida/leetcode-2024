# solution 1 - using unicode character
def encode(strs):
    return 'π'.join(strs)


def decode(s):
    return s.split('π')


test = ["testing", "this", "string"]
print(encode(test))
print(decode(encode(test)))


# solution 2 - using scape character
def encode2(strs):
    # Initialize an empty string to hold the encoded strings
    encoded_string = ''

    # Iterate over each string in the input list
    for s in strs:
        # Replace each occurrence of '/' with '//'
        # This is our way of "escaping" the slash character
        # Then add our delimiter '/:' to the end
        encoded_string += s.replace('/', '//') + '/:'

    # Return the final encoded string
    return encoded_string


def decode2(s):
    decoded_strings = []
    current_string = ""
    i = 0
    while i < len(s):
        if s[i:i + 2] == '/:':
            decoded_strings.append(current_string)
            current_string = ""
            i += 2
        elif s[i:i + 2] == '//':
            current_string += '/'
            i += 2
        else:
            current_string += s[i]
            i += 1
    return decoded_strings


test = ["testing", "this", "string"]
print(encode2(test))
print(decode2(encode2(test)))
