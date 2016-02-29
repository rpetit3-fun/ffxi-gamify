from collections import OrderedDict
from django import template
from django.db import connections
from polutils.models import Titles
from ffxi.form_constants import *
register = template.Library()


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
    q = """SELECT `war`, `mnk`, `whm`, `blm`, `rdm`, `thf`, `pld`, `drk`,
                  `bst`, `brd`, `rng`, `sam`, `nin`, `drg`, `smn`, `blu`,
                  `cor`, `pup`, `dnc`, `sch`, `geo`, `run`
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
    status['mjob'] = JOB_BY_ID_SHORT[status['mjob']].upper()
    if status['sjob']:
        status['sjob'] = JOB_BY_ID_SHORT[status['sjob']].upper()
    else:
        status['sjob'] = ''
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
    try:
        cursor = connections['darkstar'].cursor()
        q = """SELECT `title` FROM char_stats
               WHERE charid={0} LIMIT 1""".format(charid)
        cursor.execute(q)
        title = dictfetchall(cursor)[0]
        title_name = Titles.objects.get(title_id=title['title'])
        return title_name.title
    except Titles.DoesNotExist:
        return ""


@register.inclusion_tag('character_signet.html')
def get_enhanced_signet(charid):
    signet = OrderedDict((
        ('HP Boost', 0), ('MP Boost', 0), ('Defense', 0), ('Evasion', 0),
        ('Attack', 0), ('Regen', 0), ('Refresh', 0), ('Regain', 0)
    ))
    cursor = connections['darkstar'].cursor()
    q = """SELECT `varname`, `value` FROM char_vars
           WHERE charid={0} AND varname LIKE '[SIGNET]%'""".format(charid)
    cursor.execute(q)

    for row in cursor:
        varname = row[0].replace("[SIGNET]", "").replace("_", " ")
        signet[varname] = row[1]

    return {'signet': signet}
