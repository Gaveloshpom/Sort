import re

transliteration_dict= {
    ord("а"): "a",
    ord("б"): "b" ,
    ord("в"): "v",
    ord("г"): "g",
    ord("д"): "d",
    ord("е"): "e",
    ord("є"): "ye",
    ord("ж"): "gj",
    ord("з"): "z",
    ord("и"): "u",
    ord("й"): "y",
    ord("к"): "k",
    ord("л"): "l",
    ord("м"): "m",
    ord("н"): "n",
    ord("п"): "p",
    ord("р"): "r",
    ord("с"): "s",
    ord("т"): "t",
    ord("у"): "u",
    ord("ф"): "f",
    ord("х"): "h",
    ord("ц"): "c",
    ord("ч"): "ch",
    ord("ш"): "sh",
    ord("щ"): "shch",
    ord("ь"): "`",
    ord("ю"): "yu",
    ord("я"): "ya",
}

def normalize(some_string):
    translated = ""
    suf = some_string.rfind(".")
    string = some_string[suf:]
    for i in some_string[0:suf]:
        if i.islower() == True:
            translated += i.translate(transliteration_dict)
        elif i.isupper() == True:
            i = i.lower()
            translated += i.translate(transliteration_dict).upper()
        else:
            translated += i


    result = re.sub(r"\W", "_", translated)
    result = result + string
    return result


