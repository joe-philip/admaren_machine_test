from random import choice

from django.core.management import base, utils


class Command(base.BaseCommand):
    help = 'Generate an APIKey'

    def handle(self, *args, **kwargs):
        print('Add this to your .env file:\n\n')
        key = utils.get_random_secret_key()
        import string
        if '#' in key:
            random_char = choice(string.ascii_letters + string.digits)
            key = key.replace('#', random_char)
        self.stdout.write(self.style.SUCCESS(f'SECRET_KEY={key}'))
