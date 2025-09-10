import base64
class WordLoader:
    @staticmethod
    def get_words(path)->list[str]:
        """Extracts a string from a file, removes the encoding, and returns it as a list."""
        encoded_string =""
        with open(path , 'r') as f:
            encoded_string = f.readline()

        base64_bytes = encoded_string.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        decoded_string = message_bytes.decode('utf-8')
        words = decoded_string.split(",")
        return words 
        


