from django import template
from darkstar.models import Chars
from ffxi.models import ExperienceStats, LinkedAccount
register = template.Library()


@register.simple_tag
def active(request, pattern):
    if pattern == request.path:
        return 'active'
    return '{0}+{1}'.format(pattern, request.path)

@register.assignment_tag
def get_exp_stats(user):
    try:
        exp_stats = ExperienceStats.objects.get(user=user)
    except ExperienceStats.DoesNotExist:
        exp_stats = ExperienceStats.objects.create(user=user, exp=0, chain=1)
        exp_stats.save()

    return {'exp': "{:,}".format(exp_stats.exp), 'chain': exp_stats.chain}
    
@register.assignment_tag
def get_characters(user):
    try:
        accounts = LinkedAccount.objects.filter(user=user).values_list('acc_id', flat=True) 
        accounts = ','.join(["'" + str(id) + "'" for id in accounts])
    except LinkedAccount.DoesNotExist:
        return None
    
    q = """SELECT charid, charname FROM chars 
           WHERE accid IN ({0})""".format(accounts)
    characters = Chars.objects.using('darkstar').raw(q) 
    if len(list(characters)) == 0:
        return None
    else:
        chars = {}
        for character in characters:
            chars[character.charid] = character.charname
        return chars
