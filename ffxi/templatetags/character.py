from collections import OrderedDict
from django import template
from django.db import connections
from darkstar.models import Chars, CharJobs
from ffxi.models import ExperienceStats, LinkedAccount
register = template.Library()

JOB_NAMES = {'war': 'Warrior', 'mnk': 'Monk', 'whm': 'White Mage', 
             'blm': 'Black Mage', 'rdm': 'Red Mage', 'thf': 'Thief', 
             'pld': 'Paladin', 'drk': 'Dark Knight', 'bst': 'Beastmaster', 
             'brd': 'Bard', 'rng': 'Ranger', 'sam': 'Samurai',
             'nin': 'Ninja', 'drg': 'Dragoon', 'smn': 'Summoner', 
             'blu': 'Blue Mage', 'cor': 'Corsair', 'pup': 'Puppetmaster', 
             'dnc': 'Dancer', 'sch': 'Scholar', 'geo': 'Geomancer', 
             'run': 'Rune Fencer' }

def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        OrderedDict(zip([JOB_NAMES[col[0]] for col in desc], row))
        for row in cursor.fetchall()
    ]

@register.inclusion_tag('character_jobs.html')
def get_jobs(charid):
    cursor = connections['darkstar'].cursor()
    q = """SELECT `war`, `mnk`, `whm`, `blm`, `rdm`, `thf`, `pld`, `drk`, `bst`, 
                  `brd`, `rng`, `sam`, `nin`, `drg`, `smn`, `blu`, `cor`, `pup`, 
                  `dnc`, `sch`, `geo`, `run` 
           FROM char_jobs WHERE charid={0} LIMIT 1""".format(charid)
    cursor.execute(q)
    return {'jobs': dictfetchall(cursor)[0]}
