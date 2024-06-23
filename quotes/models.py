from django.db.models import Model, CharField, TextField, DateTimeField, ForeignKey, CASCADE, ManyToManyField


class Author(Model):
    name = CharField(max_length=50)
    born_date = CharField(max_length=50)
    born_location = CharField(max_length=100)
    description = TextField()
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Tag(Model):
    name = CharField(max_length=50, null=False, unique=True)

    def __str__(self):
        return self.name


class Quote(Model):
    author = ForeignKey(Author, on_delete=CASCADE, default=None, null=True)
    tags = ManyToManyField(Tag)
    quote = TextField()
    creates_at = DateTimeField(auto_now_add=True)
