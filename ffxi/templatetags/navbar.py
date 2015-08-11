from django import template
from ffxi.models import ExperienceStats
register = template.Library()


@register.simple_tag
def active(request, pattern):
    if pattern == request.path:
        return 'active'
    return '{0}+{1}'.format(pattern, request.path)

@register.simple_tag
def get_exp(user):
    try:
        exp_stats = ExperienceStats.objects.get(user=user)
    except ExperienceStats.DoesNotExist:
        exp_stats = ExperienceStats.objects.create(user=user, exp=0, chain=1)
        exp_stats.save()

    return "{:,}".format(exp_stats.exp)
    
@register.simple_tag
def get_chain(user):
    try:
        exp_stats = ExperienceStats.objects.get(user=user)
    except ExperienceStats.DoesNotExist:
        exp_stats = ExperienceStats.objects.create(user=user, exp=0, chain=1)
        exp_stats.save()

    return exp_stats.chain