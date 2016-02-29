""" Insert FFXI titles into the database. """
from bs4 import BeautifulSoup
from django.db.utils import IntegrityError
from django.core.management.base import BaseCommand, CommandError

from polutils.models import Titles


class Command(BaseCommand):
    help = 'Insert FFXI titles into the database.'

    def add_arguments(self, parser):
        parser.add_argument('title', metavar='TITLE_XML',
                            help='XML of Titles from POLUtils MassExtractor.')

    def handle(self, *args, **opts):
        fh = open(opts['title'], 'r').read()
        soup = BeautifulSoup(fh, "lxml")
        for title in soup.find_all('thing'):
            fields = title.find_all('field')
            title_id = fields[0].contents[0]
            title = fields[1].contents[0]

            try:
                title_db, created = Titles.objects.get_or_create(
                    title_id=int(title_id),
                    title=title
                )
            except IntegrityError:
                raise CommandError('Error saving title information')

            print title_id, title, created
