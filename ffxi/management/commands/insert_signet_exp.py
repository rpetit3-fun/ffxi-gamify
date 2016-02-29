""" Insert enhanced Signet upgrade requirements """
from django.db.utils import IntegrityError
from django.core.management.base import BaseCommand, CommandError

from ffxi.models import EnhancedSignetLevels


class Command(BaseCommand):
    help = 'Insert enhanced Signet upgrade requirements.'

    def levels(self, start, mod, total):
        print 1, start
        exp = [start]
        for i in range(1, total):
            print i + 1, int(start + start * mod)
            start = int(start + start * mod)
            exp.append(start)
        return exp

    def handle(self, *args, **opts):
        for exp in self.levels(10000, 0.05, 100):
            try:
                signet, created = EnhancedSignetLevels.objects.get_or_create(
                    exp=exp
                )
            except IntegrityError:
                raise CommandError('Error saving title information')
