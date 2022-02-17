import datetime
import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

class Product(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    image = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title

def getBinary():
    basic_string = "Hello World 1"
    binary_string = bytes(basic_string, 'utf-8')
    return binary_string

def getDuration():
    d = datetime.timedelta(days =-1, seconds = 68400)
    return d

class Author(models.Model):
    name = models.CharField(_('Name'), max_length=100)
    email = models.EmailField(_('Email'), max_length=254, unique=True, null=True, blank=True)
    mobile = models.CharField(_('Mobile'), max_length=20, null=True, blank=True)
    salary = models.FloatField(_('Salary'), null=True, blank=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    tag_name = models.CharField(_('Tag'), max_length=50, null=True, blank=True)

    def __str__(self):
        if self.tag_name:
            return str(self.id) + "||" + self.tag_name
        else:
            return str(self.id)

class Track(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ip_address = models.GenericIPAddressField(_('IP Address'), null=True, blank=True)

    def __str__(self):
        return str(self.id)
    

class Article(models.Model):
    """
        Basic model data types and fields:
            UUIDField               - A field for storing universally unique identifiers. Uses Python’s UUID class. When used on PostgreSQL, this stores in a uuid datatype, otherwise in a char(32).
            CharField               - A field to store text-based values.
            TextField               - A large text field. The default form widget for this field is a Textarea.
            DecimalField            - It is a fixed-precision decimal number, represented in Python by a Decimal instance.
            IntegerField            - It is an integer field. Values from -2147483648 to 2147483647 are safe in all databases supported by Django.
            FloatField              - It is a floating-point number represented in Python by a float instance.
            BooleanField            - A true/false field. The default form widget for this field is a CheckboxInput.
            DateField               - A date, represented in Python by a datetime.date instance
            TimeField               - A time, represented in Python by a datetime.time instance.
            DateTimeField           - It is used for date and time, represented in Python by a datetime.datetime instance.
            URLField                - A CharField for a URL, validated by URLValidator.
            SlugField               - Slug is a newspaper term. A slug is a short label for something, containing only letters, numbers, underscores or hyphens. They’re generally used in URLs.
            GenericIPAddressField   - An IPv4 or IPv6 address, in string format (e.g. 192.0.2.30 or 2a02:42fe::4).
            ImageField              - It inherits all attributes and methods from FileField, but also validates that the uploaded object is a valid image.
            FileField               - It is a file-upload field.
            EmailField              - It is a CharField that checks that the value is a valid email address.
            BinaryField             - A field to store raw binary data. 
            DurationField           - A field for storing periods of time.

        Relationship Fields:
            1. ForeignKey       - A many-to-one relationship. Requires two positional arguments: the class to which the model is related and the on_delete option.
            2. ManyToManyField  - A many-to-many relationship. Requires a positional argument: the class to which the model is related, which works exactly the same as it does for ForeignKey, including recursive and lazy relationships.
            3. OneToOneField    - A one-to-one relationship. Conceptually, this is similar to a ForeignKey with unique=True, but the “reverse” side of the relation will directly return a single object.
    """
    
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(_('Title'), max_length=255)
    slug = models.SlugField(_('Slug'), max_length=255, null=True, blank=True)
    description = models.TextField(_('Description'), max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to='image', max_length=255, null=True, blank=True)
    document = models.FileField(upload_to='document', max_length=255, null=True, blank=True)
    youtube_link = models.URLField(_('Youtube Link'), max_length=255, null=True, blank=True)
    tag = models.ManyToManyField(Tag, blank=True)
    num_stars = models.IntegerField(null=True, blank=True)
    publish_date = models.DateField(_('Publish Date'), null=True, blank=True)
    publish_time = models.TimeField(_('Publish Time'), null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    track = models.OneToOneField(Track, null=True, blank=True, on_delete=models.SET_NULL)

    binary_data = models.BinaryField(_('Binary'), null=True, blank=True)
    duration_data = models.DurationField(_('Duration'), null=True, blank=True)

    created_at = models.DateTimeField(_('Created at'), auto_now_add=True, auto_now=False, editable=False)
    updated_at = models.DateTimeField(_('Updated at'), auto_now_add=False, auto_now=True, editable=False)

    # def clean(self, *args, **kwargs):
    #     errors = {}
    #     other_username = User.objects.filter(username__iexact=self.username)
    #     other_email = User.objects.filter(email__iexact=self.email)
    #     if self.pk:
    #         other_username = other_username.exclude(pk=self.pk)
    #         other_email = other_email.exclude(pk=self.pk)
    #     if other_username.exists():
    #         errors.setdefault('username',[]).append('Sorry! this username already exists.')

    #     if other_email.exists():
    #         errors.setdefault('email',[]).append('Sorry! this email already exists.')

    #     if len(errors):
    #         raise ValidationError(errors)


    def __str__(self):
        return self.title