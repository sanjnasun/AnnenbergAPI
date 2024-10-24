class ArticleObject:
    def __init__(self, title, link, date, image):
        self.title = title
        self.link = link
        self.date = date
        self.image = image

    def __str__(self):
        return f"{self.title}({self.link})({self.date})({self.image})" #string constructor


    def __hash__(self):
        return hash((self.title, self.link, self.date, self.image))

    def __eq__(self, other):
        if not isinstance(other, ArticleObject):
            return False
        return (self.title, self.link, self.date, self.image) == (other.title, other.link, other.date, other.image)