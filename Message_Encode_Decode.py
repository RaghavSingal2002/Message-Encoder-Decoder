import base64


# Encoding

sample_string = 'Raghav Singal'
sample_string_bytes = sample_string.encode('ascii')


encoded_bytes = base64.b64encode(sample_string_bytes)
encoded_bytes_string = encoded_bytes.decode('ascii')

# Decoding 

encoded_bytes_string_revert = encoded_bytes_string.encode('ascii')
decoded_bytes = base64.b64decode(encoded_bytes_string_revert)

secret_message = decoded_bytes.decode('ascii')


print(secret_message)




