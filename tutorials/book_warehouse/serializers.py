from rest_framework import serializers
from book_warehouse.models import Book, Publisher, Author


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['id', 'name', 'address', 'phone',
                  'url']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'address', 'url']


class BookSerializer(serializers.ModelSerializer):
    # books = serializers.PrimaryKeyRelatedField(
    #     many=True, queryset=Book.objects.all()
    # )
    id = serializers.IntegerField()
    isbn = serializers.CharField(max_length=255)
    year = serializers.CharField(max_length=5)
    title = serializers.CharField(max_length=100)
    publisher = PublisherSerializer(source='publisher_fk', read_only=True)
    author = AuthorSerializer(source='author_fk', read_only=True)
    publisher_fk = serializers.PrimaryKeyRelatedField(
        queryset=Publisher.objects.all(),
        write_only=True
    )
    author_fk = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(),
        write_only=True
    )
    
    class Meta:
        model = Book
        fields = ['id', 'publisher_fk', 'author_fk', 'isbn', 'year', 'title',
                  'price', 'publisher', 'author']

    # custom object_level validation
    # def validate(self, data):
        # access
        # data['title']

    # custom field_level validation
    def validate_title(self, value):
        value_capitalize = value.capitalize()
        if value.islower() or value.isupper():
            raise serializers.ValidationError(
                "Book title must be in capitalize form."
            )
        return value_capitalize
        
    def create(self, validate_data):
        publisher_data = validate_data.pop('publisher_fk')
        author_data = validate_data.pop('author_fk')
        print('---->', publisher_data, '-----', author_data, '<-----------')
        return Book.objects.create(
            publisher_fk=publisher_data,
            author_fk=author_data,
            **validate_data
        )
    
    def update(self, instance, validate_data):
        if 'publisher_name' in validate_data:
            instance.publisher_name = validate_data.pop('publisher_name')
        if 'author_name' in validate_data:
            instance.author_name = validate_data.pop('author_name')
        for attr, value in validate_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance