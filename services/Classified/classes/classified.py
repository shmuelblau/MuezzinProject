from classes.word_loader import WordLoader
from config import *
class Classified:
    very_unfriendly = [word.lower() for word in WordLoader.get_words(PATH_VERY)]
    less_unfriendly = [word.lower() for word in WordLoader.get_words(PATH_LESS)]
    words_len = len(very_unfriendly) +( len(less_unfriendly)//2 )

    @staticmethod
    def get_percent(text:str) -> int:
        text = text.lower()
        text_len = len(text.split())
        count = 0
        for word in Classified.very_unfriendly:
            if word in text:
                count += 2
        for word in Classified.less_unfriendly:
            if word in text:
                count += 1
        
        text_len = len(text.split())
        if count > Classified.words_len //2 :
            count += count


        percent = count 
        # nead to add logic
        return percent
    

    @staticmethod    
    def get_is_bds(int)-> bool:
        return True
    

    @staticmethod
    def get_threat_level(int) -> str:
        return ""
    
    @staticmethod
    def get_all_farams(str) -> dict:
        return{}
    

