from django.core.exceptions import ValidationError
from string import ascii_lowercase, digits

def characterValidator(strng):
    def validator(value):
        for char in value:
            if value not in strng:
                raise ValidationError(u"%s contains characters not in '%s'" % (value, strng))
    return validator

lowerAlphaNumValidator = characterValidator(ascii_lowercase + digits + '_')
