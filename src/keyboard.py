from src.item import Item


class MixinChangeLang:
    def __init__(self):
        self.list_lang = ['EN', 'RU']


class Keyboard(Item, MixinChangeLang):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self.__language = self.list_lang[0]

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        switch = self.list_lang.pop(0)
        self.list_lang.append(switch)
        self.__language = self.list_lang[0]
        return self.__language
