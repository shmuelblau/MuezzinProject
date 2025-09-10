from classes.word_loader import WordLoader
from config import *
class Classified:
    """Contains static methods that can accept text and display 3 new fields for
      it with informationabout the dangers related to the words it extracts from a file."""
    

    very_unfriendly = [word.lower() for word in WordLoader.get_words(PATH_VERY)]
    less_unfriendly = [word.lower() for word in WordLoader.get_words(PATH_LESS)]
    words_len = len(very_unfriendly) +( len(less_unfriendly)//2 )
    line_none = 10 
    line_medium = 30

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

        a = text_len / 100
        percent = count // a 
        percent = int(percent) if percent < 100 else int(100) 
        return percent 
    

    @staticmethod    
    def get_is_bds(num:int)-> bool:
        return num > Classified.line_none
        
    

    @staticmethod
    def get_threat_level(num:int ) -> str:
        result =  "high" if  num > Classified.line_medium  else "medium" if num > Classified.line_none else "none"
        return result
    
    @staticmethod
    def get_all_farams(text:str) -> dict:
        percent = Classified.get_percent(text)
        result = {
            "bds_percent" : percent ,
            "is_bds":Classified.get_is_bds(percent) ,
            "bds_threat_level" : Classified.get_threat_level(percent)
        }

        return result
    

