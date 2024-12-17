from Modelos.user import User

class Companies(User):
    def __init__(self, id_company, name_company, catch_phrase, bs, userId):
        super().__init__(userId)
        self.id_company = id_company
        self.name_company = name_company
        self.catch_phrase = catch_phrase
        self.bs = bs