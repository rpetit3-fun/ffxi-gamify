from collections import OrderedDict
from django import template
from django.db import connections
from polutils.models import Titles
register = template.Library()

JOB_NAMES = {
    'war': 'Warrior', 'mnk': 'Monk', 'whm': 'White Mage', 'blm': 'Black Mage', 
    'rdm': 'Red Mage', 'thf': 'Thief', 'pld': 'Paladin', 'drk': 'Dark Knight', 
    'bst': 'Beastmaster', 'brd': 'Bard', 'rng': 'Ranger', 'sam': 'Samurai',
    'nin': 'Ninja', 'drg': 'Dragoon', 'smn': 'Summoner', 'blu': 'Blue Mage', 
    'cor': 'Corsair', 'pup': 'Puppetmaster', 'dnc': 'Dancer', 'sch': 'Scholar', 
    'geo': 'Geomancer', 'run': 'Rune Fencer' 
}

JOB_BY_ID = { 
    1: 'Warrior', 2: 'Monk', 3: 'White Mage', 4: 'Black Mage', 5: 'Red Mage', 
    6: 'Thief', 7: 'Paladin', 8: 'Dark Knight', 9: 'Beastmaster', 10: 'Bard', 
    11: 'Ranger', 12: 'Samurai', 13: 'Ninja', 14: 'Dragoon', 15: 'Summoner', 
    16: 'Blue Mage', 17: 'Corsair', 18: 'Puppetmaster', 19: 'Dancer', 
    20: 'Scholar', 21: 'Geomancer', 22: 'Rune Fencer'
}
             
def fetchalljobs(cursor):
    desc = cursor.description
    return [
        OrderedDict(zip([JOB_NAMES[col[0]] for col in desc], row))
        for row in cursor.fetchall()
    ]
    
def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
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
    return {'jobs': fetchalljobs(cursor)[0]}

@register.assignment_tag
def get_status(charid):
    cursor = connections['darkstar'].cursor()
    q = """SELECT `hp`, `mp`, `mjob`, `sjob`, `mlvl`, `slvl` 
           FROM char_stats WHERE charid={0} LIMIT 1""".format(charid)
    cursor.execute(q)
    status = dictfetchall(cursor)[0]
    status['mjob'] = JOB_BY_ID[status['mjob']]
    status['sjob'] = JOB_BY_ID[status['sjob']]
    return status

@register.simple_tag
def get_gil(charid):
    cursor = connections['darkstar'].cursor()
    q = """SELECT `quantity` FROM char_inventory 
           WHERE charid={0} and slot=0 LIMIT 1""".format(charid)
    cursor.execute(q)
    return "{:,}".format(cursor.fetchone()[0])

@register.simple_tag
def get_title(charid):
    cursor = connections['darkstar'].cursor()
    q = "SELECT `title` FROM char_stats WHERE charid={0} LIMIT 1".format(charid)
    cursor.execute(q)
    title = dictfetchall(cursor)[0]
    
    title_name = Titles.objects.get(title_id=title['title'])
    return title_name.title

@register.inclusion_tag('character_signet.html')  
def get_enhanced_signet(charid):
    signet = OrderedDict((
        ('HP Boost', 0), ('MP Boost', 0), ('Defense', 0), ('Evasion', 0), 
        ('Regen', 0), ('Refresh', 0), ('Regain', 0)
    ))
    cursor = connections['darkstar'].cursor()
    q = """SELECT `varname`, `value` FROM char_vars 
           WHERE charid={0} AND varname LIKE '[SIGNET]%'""".format(charid)
    cursor.execute(q)
    
    for row in cursor:
        varname = row[0].replace("[SIGNET]", "").replace("_", " ")
        signet[varname] = row[1]
    
    return {'signet': signet}
