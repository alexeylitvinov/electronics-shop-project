from src.item import Item


class MixinChangeLang:
    def __init__(self):
        self.__list_lang = ['EN', 'RU']
        self.__language = self.__list_lang[0]

    def change_lang(self):
        switch = self.__list_lang.pop(0)
        self.__list_lang.append(switch)
        self.__language = self.__list_lang[0]
        return self.__language

    @property
    def language(self):
        return self.__language


class Keyboard(Item, MixinChangeLang):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
