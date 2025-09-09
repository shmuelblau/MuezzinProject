import base64
class WordLoader:
    @staticmethod
    def get_words(path)->list[str]:
        encoded_string =""
        with open(path , 'r') as f:
            encoded_string = f.readline()

        base64_bytes = encoded_string.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        decoded_string = message_bytes.decode('utf-8')
        words = decoded_string.split(",")
        return words 
        


print(WordLoader.get_words("C:/Users/user/Desktop/DATA/Projects/MuezzinProject/services/Classified/data/Less_unfriendly.txt"))