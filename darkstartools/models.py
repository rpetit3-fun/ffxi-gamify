# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Abilities(models.Model):
    abilityid = models.SmallIntegerField(db_column='abilityId', primary_key=True)  # Field name made lowercase.
    name = models.TextField(blank=True, null=True)
    job = models.IntegerField()
    level = models.IntegerField()
    validtarget = models.IntegerField(db_column='validTarget')  # Field name made lowercase.
    recasttime = models.SmallIntegerField(db_column='recastTime')  # Field name made lowercase.
    recastid = models.SmallIntegerField(db_column='recastId')  # Field name made lowercase.
    message1 = models.SmallIntegerField()
    message2 = models.SmallIntegerField()
    animation = models.SmallIntegerField()
    range = models.FloatField()
    isaoe = models.IntegerField(db_column='isAOE')  # Field name made lowercase.
    ce = models.SmallIntegerField(db_column='CE')  # Field name made lowercase.
    ve = models.SmallIntegerField(db_column='VE')  # Field name made lowercase.
    meritmodid = models.SmallIntegerField(db_column='meritModID')  # Field name made lowercase.
    addtype = models.SmallIntegerField(db_column='addType')  # Field name made lowercase.
    required_expansion = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'abilities'


class AbilitiesCharges(models.Model):
    recastid = models.SmallIntegerField(db_column='recastId')  # Field name made lowercase.
    job = models.IntegerField()
    level = models.IntegerField()
    maxcharges = models.IntegerField(db_column='maxCharges')  # Field name made lowercase.
    chargetime = models.SmallIntegerField(db_column='chargeTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'abilities_charges'
        unique_together = (('recastid', 'job', 'level'),)


class Accounts(models.Model):
    id = models.IntegerField(primary_key=True)
    login = models.CharField(max_length=16)
    password = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    email2 = models.CharField(max_length=64)
    timecreate = models.DateTimeField()
    timelastmodify = models.DateTimeField()
    content_ids = models.IntegerField()
    status = models.IntegerField()
    priv = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'accounts'


class AccountsBanned(models.Model):
    accid = models.IntegerField(primary_key=True)
    timebann = models.DateTimeField()
    timeunbann = models.DateTimeField()
    banncomment = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounts_banned'


class AccountsParties(models.Model):
    charid = models.ForeignKey('AccountsSessions', db_column='charid', primary_key=True)
    partyid = models.IntegerField()
    partyflag = models.SmallIntegerField()
    allianceid = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'accounts_parties'


class AccountsSessions(models.Model):
    accid = models.IntegerField(unique=True)
    charid = models.IntegerField(primary_key=True)
    targid = models.SmallIntegerField()
    linkshellid1 = models.IntegerField()
    linkshellrank1 = models.SmallIntegerField()
    linkshellid2 = models.IntegerField()
    linkshellrank2 = models.SmallIntegerField()
    session_key = models.CharField(max_length=20)
    server_addr = models.IntegerField()
    server_port = models.SmallIntegerField()
    client_addr = models.IntegerField()
    client_port = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'accounts_sessions'


class AuctionHouse(models.Model):
    itemid = models.SmallIntegerField()
    stack = models.IntegerField()
    seller = models.IntegerField()
    seller_name = models.CharField(max_length=15, blank=True, null=True)
    date = models.IntegerField()
    price = models.IntegerField()
    buyer_name = models.CharField(max_length=15, blank=True, null=True)
    sale = models.IntegerField()
    sell_date = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auction_house'


class AuditChat(models.Model):
    lineid = models.AutoField(db_column='lineID', primary_key=True)  # Field name made lowercase.
    speaker = models.TextField()
    type = models.TextField()
    recipient = models.TextField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'audit_chat'


class Augments(models.Model):
    augmentid = models.SmallIntegerField(db_column='augmentId')  # Field name made lowercase.
    multiplier = models.SmallIntegerField()
    modid = models.SmallIntegerField(db_column='modId')  # Field name made lowercase.
    value = models.SmallIntegerField()
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'augments'


class BcnmBattlefield(models.Model):
    bcnmid = models.SmallIntegerField(db_column='bcnmId')  # Field name made lowercase.
    battlefieldnumber = models.IntegerField(db_column='battlefieldNumber', blank=True, null=True)  # Field name made lowercase.
    monsterid = models.IntegerField(db_column='monsterId')  # Field name made lowercase.
    conditions = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bcnm_battlefield'


class BcnmInfo(models.Model):
    bcnmid = models.SmallIntegerField(db_column='bcnmId', primary_key=True)  # Field name made lowercase.
    zoneid = models.IntegerField(db_column='zoneId')  # Field name made lowercase.
    name = models.CharField(max_length=30)
    fastestname = models.CharField(db_column='fastestName', max_length=15, blank=True, null=True)  # Field name made lowercase.
    fastesttime = models.SmallIntegerField(db_column='fastestTime', blank=True, null=True)  # Field name made lowercase.
    timelimit = models.SmallIntegerField(db_column='timeLimit')  # Field name made lowercase.
    levelcap = models.SmallIntegerField(db_column='levelCap')  # Field name made lowercase.
    partysize = models.SmallIntegerField(db_column='partySize')  # Field name made lowercase.
    lootdropid = models.SmallIntegerField(db_column='lootDropId')  # Field name made lowercase.
    rules = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'bcnm_info'


class BcnmLoot(models.Model):
    lootdropid = models.SmallIntegerField(db_column='LootDropId')  # Field name made lowercase.
    itemid = models.SmallIntegerField(db_column='itemId')  # Field name made lowercase.
    rolls = models.SmallIntegerField()
    lootgroupid = models.IntegerField(db_column='lootGroupId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bcnm_loot'


class BcnmTreasureChests(models.Model):
    bcnmid = models.SmallIntegerField(db_column='bcnmId')  # Field name made lowercase.
    battlefieldnumber = models.IntegerField(db_column='battlefieldNumber', blank=True, null=True)  # Field name made lowercase.
    npcid = models.IntegerField(db_column='npcId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bcnm_treasure_chests'


class BlueSpellList(models.Model):
    spellid = models.SmallIntegerField()
    mob_skill_id = models.SmallIntegerField()
    set_points = models.SmallIntegerField()
    trait_category = models.SmallIntegerField()
    trait_category_weight = models.SmallIntegerField()
    primary_sc = models.SmallIntegerField()
    secondary_sc = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'blue_spell_list'
        unique_together = (('spellid', 'mob_skill_id'),)


class BlueSpellMods(models.Model):
    spellid = models.SmallIntegerField(db_column='spellId')  # Field name made lowercase.
    modid = models.SmallIntegerField()
    value = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'blue_spell_mods'
        unique_together = (('spellid', 'modid'),)


class BlueTraits(models.Model):
    trait_category = models.SmallIntegerField()
    trait_points_needed = models.SmallIntegerField()
    traitid = models.IntegerField()
    modifier = models.SmallIntegerField()
    value = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'blue_traits'
        unique_together = (('trait_category', 'trait_points_needed', 'modifier'),)


class CharBlacklist(models.Model):
    charid_owner = models.IntegerField()
    charid_target = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'char_blacklist'
        unique_together = (('charid_target', 'charid_owner'),)


class CharEffects(models.Model):
    charid = models.IntegerField()
    effectid = models.SmallIntegerField()
    icon = models.SmallIntegerField()
    power = models.SmallIntegerField()
    tick = models.IntegerField()
    duration = models.IntegerField()
    subid = models.SmallIntegerField()
    subpower = models.SmallIntegerField()
    tier = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'char_effects'


class CharEquip(models.Model):
    charid = models.IntegerField()
    slotid = models.IntegerField()
    equipslotid = models.IntegerField()
    containerid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'char_equip'
        unique_together = (('charid', 'equipslotid'),)


class CharExp(models.Model):
    charid = models.IntegerField(primary_key=True)
    mode = models.IntegerField()
    war = models.SmallIntegerField()
    mnk = models.SmallIntegerField()
    whm = models.SmallIntegerField()
    blm = models.SmallIntegerField()
    rdm = models.SmallIntegerField()
    thf = models.SmallIntegerField()
    pld = models.SmallIntegerField()
    drk = models.SmallIntegerField()
    bst = models.SmallIntegerField()
    brd = models.SmallIntegerField()
    rng = models.SmallIntegerField()
    sam = models.SmallIntegerField()
    nin = models.SmallIntegerField()
    drg = models.SmallIntegerField()
    smn = models.SmallIntegerField()
    blu = models.SmallIntegerField()
    cor = models.SmallIntegerField()
    pup = models.SmallIntegerField()
    dnc = models.SmallIntegerField()
    sch = models.SmallIntegerField()
    geo = models.SmallIntegerField()
    run = models.SmallIntegerField()
    merits = models.IntegerField()
    limits = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'char_exp'


class CharInventory(models.Model):
    charid = models.IntegerField()
    location = models.IntegerField()
    slot = models.IntegerField()
    itemid = models.SmallIntegerField(db_column='itemId')  # Field name made lowercase.
    quantity = models.IntegerField()
    bazaar = models.IntegerField()
    signature = models.CharField(max_length=20)
    extra = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'char_inventory'
        unique_together = (('charid', 'location', 'slot'),)


class CharJobs(models.Model):
    charid = models.IntegerField(primary_key=True)
    unlocked = models.IntegerField()
    genkai = models.IntegerField()
    war = models.IntegerField()
    mnk = models.IntegerField()
    whm = models.IntegerField()
    blm = models.IntegerField()
    rdm = models.IntegerField()
    thf = models.IntegerField()
    pld = models.IntegerField()
    drk = models.IntegerField()
    bst = models.IntegerField()
    brd = models.IntegerField()
    rng = models.IntegerField()
    sam = models.IntegerField()
    nin = models.IntegerField()
    drg = models.IntegerField()
    smn = models.IntegerField()
    blu = models.IntegerField()
    cor = models.IntegerField()
    pup = models.IntegerField()
    dnc = models.IntegerField()
    sch = models.IntegerField()
    geo = models.IntegerField()
    run = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'char_jobs'


class CharLook(models.Model):
    charid = models.IntegerField(primary_key=True)
    face = models.IntegerField()
    race = models.IntegerField()
    size = models.IntegerField()
    head = models.SmallIntegerField()
    body = models.SmallIntegerField()
    hands = models.SmallIntegerField()
    legs = models.SmallIntegerField()
    feet = models.SmallIntegerField()
    main = models.SmallIntegerField()
    sub = models.SmallIntegerField()
    ranged = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'char_look'


class CharPet(models.Model):
    charid = models.IntegerField(primary_key=True)
    wyvernid = models.SmallIntegerField()
    automatonid = models.SmallIntegerField()
    unlocked_attachments = models.TextField(blank=True, null=True)
    equipped_attachments = models.TextField(blank=True, null=True)
    adventuringfellowid = models.SmallIntegerField()
    chocoboid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'char_pet'


class CharPetName(models.Model):
    charid = models.IntegerField(primary_key=True)
    wyvernid = models.SmallIntegerField()
    automatonid = models.SmallIntegerField()
    adventuringfellowid = models.SmallIntegerField()
    chocoboid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'char_pet_name'


class CharPoints(models.Model):
    charid = models.IntegerField(primary_key=True)
    sandoria_cp = models.IntegerField()
    bastok_cp = models.IntegerField()
    windurst_cp = models.IntegerField()
    sandoria_supply = models.IntegerField()
    bastok_supply = models.IntegerField()
    windurst_supply = models.IntegerField()
    beastman_seal = models.IntegerField()
    kindred_seal = models.SmallIntegerField()
    kindred_crest = models.SmallIntegerField()
    high_kindred_crest = models.SmallIntegerField()
    sacred_kindred_crest = models.SmallIntegerField()
    ancient_beastcoin = models.SmallIntegerField()
    valor_point = models.SmallIntegerField()
    scyld = models.SmallIntegerField()
    guild_fishing = models.IntegerField()
    guild_woodworking = models.IntegerField()
    guild_smithing = models.IntegerField()
    guild_goldsmithing = models.IntegerField()
    guild_weaving = models.IntegerField()
    guild_leathercraft = models.IntegerField()
    guild_bonecraft = models.IntegerField()
    guild_alchemy = models.IntegerField()
    guild_cooking = models.IntegerField()
    cinder = models.IntegerField()
    fire_fewell = models.IntegerField()
    ice_fewell = models.IntegerField()
    wind_fewell = models.IntegerField()
    earth_fewell = models.IntegerField()
    lightning_fewell = models.IntegerField()
    water_fewell = models.IntegerField()
    light_fewell = models.IntegerField()
    dark_fewell = models.IntegerField()
    ballista_point = models.IntegerField()
    fellow_point = models.IntegerField()
    chocobuck_sandoria = models.SmallIntegerField()
    chocobuck_bastok = models.SmallIntegerField()
    chocobuck_windurst = models.SmallIntegerField()
    research_mark = models.IntegerField()
    tunnel_worm = models.IntegerField()
    morion_worm = models.IntegerField()
    phantom_worm = models.IntegerField()
    moblin_marble = models.IntegerField()
    infamy = models.SmallIntegerField()
    prestige = models.SmallIntegerField()
    legion_point = models.IntegerField()
    spark_of_eminence = models.IntegerField()
    shining_star = models.IntegerField()
    imperial_standing = models.IntegerField()
    runic_portal = models.IntegerField()
    leujaoam_assault_point = models.IntegerField()
    mamool_assault_point = models.IntegerField()
    lebros_assault_point = models.IntegerField()
    periqia_assault_point = models.IntegerField()
    ilrusi_assault_point = models.IntegerField()
    nyzul_isle_assault_point = models.IntegerField()
    zeni_point = models.IntegerField()
    jetton = models.IntegerField()
    therion_ichor = models.IntegerField()
    maw = models.IntegerField()
    past_sandoria_tp = models.IntegerField()
    past_bastok_tp = models.IntegerField()
    past_windurst_tp = models.IntegerField()
    allied_notes = models.IntegerField()
    bayld = models.IntegerField()
    kinetic_unit = models.SmallIntegerField()
    obsidian_fragment = models.IntegerField()
    lebondopt_wing = models.SmallIntegerField()
    pulchridopt_wing = models.SmallIntegerField()
    mweya_plasm = models.IntegerField()
    cruor = models.IntegerField()
    resistance_credit = models.IntegerField()
    dominion_note = models.IntegerField()
    fifth_echelon_trophy = models.IntegerField()
    fourth_echelon_trophy = models.IntegerField()
    third_echelon_trophy = models.IntegerField()
    second_echelon_trophy = models.IntegerField()
    first_echelon_trophy = models.IntegerField()
    cave_points = models.IntegerField()
    id_tags = models.IntegerField()
    op_credits = models.IntegerField()
    traverser_stones = models.IntegerField()
    voidstones = models.IntegerField()
    kupofried_corundums = models.IntegerField()
    imprimaturs = models.IntegerField()
    pheromone_sacks = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'char_points'


class CharProfile(models.Model):
    charid = models.IntegerField(primary_key=True)
    rank_points = models.IntegerField()
    rank_sandoria = models.IntegerField()
    rank_bastok = models.IntegerField()
    rank_windurst = models.IntegerField()
    fame_sandoria = models.SmallIntegerField()
    fame_bastok = models.SmallIntegerField()
    fame_windurst = models.SmallIntegerField()
    fame_norg = models.SmallIntegerField()
    fame_jeuno = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'char_profile'


class CharRecast(models.Model):
    charid = models.IntegerField()
    recast_id = models.SmallIntegerField()
    time = models.IntegerField()
    recast = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'char_recast'
        unique_together = (('charid', 'recast_id'),)


class CharSkills(models.Model):
    charid = models.IntegerField()
    skillid = models.IntegerField()
    value = models.SmallIntegerField()
    rank = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'char_skills'
        unique_together = (('charid', 'skillid'),)


class CharStats(models.Model):
    charid = models.IntegerField(primary_key=True)
    hp = models.SmallIntegerField()
    mp = models.SmallIntegerField()
    nameflags = models.IntegerField()
    mhflag = models.IntegerField()
    mjob = models.IntegerField()
    sjob = models.IntegerField()
    death = models.IntegerField()
    number_2h = models.IntegerField(db_column='2h')  # Field renamed because it wasn't a valid Python identifier.
    title = models.SmallIntegerField()
    bazaar_message = models.TextField(blank=True, null=True)
    zoning = models.IntegerField()
    mlvl = models.IntegerField()
    slvl = models.IntegerField()
    pet_id = models.SmallIntegerField()
    pet_type = models.SmallIntegerField()
    pet_hp = models.SmallIntegerField()
    pet_mp = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'char_stats'


class CharStorage(models.Model):
    charid = models.IntegerField(primary_key=True)
    inventory = models.IntegerField()
    safe = models.IntegerField()
    locker = models.IntegerField()
    satchel = models.IntegerField()
    sack = models.IntegerField()
    case = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'char_storage'


class CharStyle(models.Model):
    charid = models.IntegerField(primary_key=True)
    head = models.SmallIntegerField()
    body = models.SmallIntegerField()
    hands = models.SmallIntegerField()
    legs = models.SmallIntegerField()
    feet = models.SmallIntegerField()
    main = models.SmallIntegerField()
    sub = models.SmallIntegerField()
    ranged = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'char_style'


class CharVars(models.Model):
    charid = models.IntegerField()
    varname = models.CharField(max_length=30)
    value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'char_vars'
        unique_together = (('charid', 'varname'),)


class CharWeaponSkillPoints(models.Model):
    itemindex = models.IntegerField()
    charid = models.IntegerField()
    points = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'char_weapon_skill_points'
        unique_together = (('itemindex', 'charid'),)


class Chars(models.Model):
    charid = models.IntegerField(primary_key=True)
    accid = models.IntegerField()
    charname = models.CharField(max_length=15)
    nation = models.IntegerField()
    pos_zone = models.SmallIntegerField()
    pos_prevzone = models.SmallIntegerField()
    pos_rot = models.IntegerField()
    pos_x = models.FloatField()
    pos_y = models.FloatField()
    pos_z = models.FloatField()
    boundary = models.SmallIntegerField()
    home_zone = models.IntegerField()
    home_rot = models.IntegerField()
    home_x = models.FloatField()
    home_y = models.FloatField()
    home_z = models.FloatField()
    merits = models.TextField(blank=True, null=True)
    missions = models.TextField(blank=True, null=True)
    assault = models.TextField(blank=True, null=True)
    campaign = models.TextField(blank=True, null=True)
    quests = models.TextField(blank=True, null=True)
    keyitems = models.TextField(blank=True, null=True)
    spells = models.TextField(blank=True, null=True)
    set_blue_spells = models.TextField(blank=True, null=True)
    abilities = models.TextField(blank=True, null=True)
    titles = models.TextField(blank=True, null=True)
    zones = models.TextField(blank=True, null=True)
    playtime = models.IntegerField()
    unlocked_weapons = models.TextField(blank=True, null=True)
    gmlevel = models.SmallIntegerField()
    isnewplayer = models.SmallIntegerField()
    mentor = models.SmallIntegerField()
    campaign_allegiance = models.IntegerField()
    isstylelocked = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'chars'


class ConquestSystem(models.Model):
    region_id = models.IntegerField(primary_key=True)
    region_control = models.IntegerField()
    region_control_prev = models.IntegerField()
    sandoria_influence = models.IntegerField()
    bastok_influence = models.IntegerField()
    windurst_influence = models.IntegerField()
    beastmen_influence = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'conquest_system'


class DeliveryBox(models.Model):
    charid = models.IntegerField()
    charname = models.CharField(max_length=15, blank=True, null=True)
    box = models.IntegerField()
    slot = models.SmallIntegerField()
    itemid = models.SmallIntegerField()
    itemsubid = models.SmallIntegerField()
    quantity = models.IntegerField()
    extra = models.TextField(blank=True, null=True)
    senderid = models.IntegerField()
    sender = models.CharField(max_length=15, blank=True, null=True)
    received = models.IntegerField()
    sent = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'delivery_box'
        unique_together = (('charid', 'box', 'slot'),)


class Elevators(models.Model):
    name = models.CharField(max_length=35)
    elevator = models.IntegerField()
    upperdoor = models.IntegerField(db_column='upperDoor')  # Field name made lowercase.
    lowerdoor = models.IntegerField(db_column='lowerDoor')  # Field name made lowercase.
    status = models.IntegerField()
    regime = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'elevators'


class ExpBase(models.Model):
    level = models.IntegerField(primary_key=True)
    exp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'exp_base'


class ExpTable(models.Model):
    level = models.IntegerField(primary_key=True)
    r1 = models.SmallIntegerField()
    r2 = models.SmallIntegerField()
    r3 = models.SmallIntegerField()
    r4 = models.SmallIntegerField()
    r5 = models.SmallIntegerField()
    r6 = models.SmallIntegerField()
    r7 = models.SmallIntegerField()
    r8 = models.SmallIntegerField()
    r9 = models.SmallIntegerField()
    r10 = models.SmallIntegerField()
    r11 = models.SmallIntegerField()
    r12 = models.SmallIntegerField()
    r13 = models.SmallIntegerField()
    r14 = models.SmallIntegerField()
    r15 = models.SmallIntegerField()
    r16 = models.SmallIntegerField()
    r17 = models.SmallIntegerField()
    r18 = models.SmallIntegerField()
    r19 = models.SmallIntegerField()
    r20 = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'exp_table'


class FishingFish(models.Model):
    fishid = models.IntegerField(primary_key=True)
    name = models.TextField()
    min = models.IntegerField()
    max = models.IntegerField()
    watertype = models.IntegerField()
    size = models.IntegerField()
    stamina = models.IntegerField()
    log = models.IntegerField()
    quest = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fishing_fish'


class FishingLure(models.Model):
    lureid = models.SmallIntegerField()
    name = models.TextField()
    fishid = models.SmallIntegerField()
    luck = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'fishing_lure'
        unique_together = (('lureid', 'fishid'),)


class FishingRod(models.Model):
    rodid = models.SmallIntegerField()
    name = models.TextField()
    fishid = models.SmallIntegerField()
    flag = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fishing_rod'
        unique_together = (('rodid', 'fishid'),)


class FishingZone(models.Model):
    zoneid = models.IntegerField()
    name = models.TextField()
    fishid = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'fishing_zone'
        unique_together = (('zoneid', 'fishid'),)


class GuildItemPoints(models.Model):
    guildid = models.IntegerField()
    itemid = models.SmallIntegerField()
    rank = models.SmallIntegerField()
    points = models.SmallIntegerField()
    max_points = models.SmallIntegerField()
    pattern = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'guild_item_points'
        unique_together = (('guildid', 'itemid', 'pattern'),)


class GuildShops(models.Model):
    guildid = models.SmallIntegerField()
    itemid = models.SmallIntegerField()
    min_price = models.IntegerField()
    max_price = models.IntegerField()
    max_quantity = models.SmallIntegerField()
    daily_increase = models.SmallIntegerField()
    initial_quantity = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'guild_shops'
        unique_together = (('guildid', 'itemid'),)


class Guilds(models.Model):
    id = models.IntegerField(primary_key=True)
    points_name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'guilds'


class InstanceEntities(models.Model):
    instanceid = models.IntegerField()
    entity_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'instance_entities'
        unique_together = (('instanceid', 'entity_id'),)


class InstanceList(models.Model):
    instanceid = models.IntegerField(primary_key=True)
    instance_name = models.CharField(max_length=35)
    entrance_zone = models.IntegerField()
    time_limit = models.IntegerField()
    start_x = models.FloatField()
    start_y = models.FloatField()
    start_z = models.FloatField()
    start_rot = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'instance_list'


class ItemArmor(models.Model):
    itemid = models.SmallIntegerField(db_column='itemId', primary_key=True)  # Field name made lowercase.
    name = models.TextField(blank=True, null=True)
    level = models.IntegerField()
    ilevel = models.IntegerField()
    jobs = models.IntegerField()
    mid = models.SmallIntegerField(db_column='MId')  # Field name made lowercase.
    shieldsize = models.IntegerField(db_column='shieldSize')  # Field name made lowercase.
    scripttype = models.SmallIntegerField(db_column='scriptType')  # Field name made lowercase.
    slot = models.SmallIntegerField()
    rslot = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'item_armor'


class ItemBasic(models.Model):
    itemid = models.SmallIntegerField(primary_key=True)
    subid = models.SmallIntegerField()
    name = models.TextField()
    sortname = models.TextField()
    stacksize = models.IntegerField(db_column='stackSize')  # Field name made lowercase.
    flags = models.SmallIntegerField()
    ah = models.IntegerField(db_column='aH')  # Field name made lowercase.
    nosale = models.IntegerField(db_column='NoSale')  # Field name made lowercase.
    basesell = models.IntegerField(db_column='BaseSell')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'item_basic'


class ItemFurnishing(models.Model):
    itemid = models.SmallIntegerField(primary_key=True)
    name = models.TextField()
    storage = models.IntegerField()
    moghancement = models.IntegerField()
    element = models.IntegerField()
    aura = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'item_furnishing'


class ItemLatents(models.Model):
    itemid = models.SmallIntegerField(db_column='itemId')  # Field name made lowercase.
    modid = models.SmallIntegerField(db_column='modId')  # Field name made lowercase.
    value = models.SmallIntegerField()
    latentid = models.SmallIntegerField(db_column='latentId')  # Field name made lowercase.
    latentparam = models.SmallIntegerField(db_column='latentParam')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'item_latents'
        unique_together = (('itemid', 'modid', 'value', 'latentid', 'latentparam'),)


class ItemMods(models.Model):
    itemid = models.SmallIntegerField(db_column='itemId')  # Field name made lowercase.
    modid = models.SmallIntegerField(db_column='modId')  # Field name made lowercase.
    value = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'item_mods'
        unique_together = (('itemid', 'modid'),)


class ItemModsPet(models.Model):
    itemid = models.SmallIntegerField(db_column='itemId')  # Field name made lowercase.
    modid = models.SmallIntegerField(db_column='modId')  # Field name made lowercase.
    value = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'item_mods_pet'
        unique_together = (('itemid', 'modid'),)


class ItemPuppet(models.Model):
    itemid = models.SmallIntegerField(primary_key=True)
    name = models.TextField()
    slot = models.IntegerField()
    element = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'item_puppet'


class ItemUsable(models.Model):
    itemid = models.SmallIntegerField(primary_key=True)
    name = models.TextField()
    validtargets = models.IntegerField(db_column='validTargets')  # Field name made lowercase.
    activation = models.IntegerField()
    animation = models.SmallIntegerField()
    animationtime = models.IntegerField(db_column='animationTime')  # Field name made lowercase.
    maxcharges = models.IntegerField(db_column='maxCharges')  # Field name made lowercase.
    usedelay = models.IntegerField(db_column='useDelay')  # Field name made lowercase.
    reusedelay = models.IntegerField(db_column='reuseDelay')  # Field name made lowercase.
    aoe = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'item_usable'


class ItemWeapon(models.Model):
    itemid = models.SmallIntegerField(db_column='itemId', primary_key=True)  # Field name made lowercase.
    name = models.TextField(blank=True, null=True)
    skill = models.IntegerField()
    subskill = models.IntegerField()
    ilvl_skill = models.SmallIntegerField()
    ilvl_parry = models.SmallIntegerField()
    ilvl_macc = models.SmallIntegerField()
    dmgtype = models.IntegerField(db_column='dmgType')  # Field name made lowercase.
    hit = models.IntegerField()
    delay = models.IntegerField()
    dmg = models.IntegerField()
    unlock_points = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'item_weapon'


class Linkshells(models.Model):
    linkshellid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    color = models.SmallIntegerField()
    poster = models.CharField(max_length=15)
    message = models.TextField(blank=True, null=True)
    messagetime = models.IntegerField()
    postrights = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'linkshells'


class Merits(models.Model):
    meritid = models.SmallIntegerField(primary_key=True)
    name = models.CharField(max_length=25)
    upgrade = models.IntegerField()
    value = models.SmallIntegerField()
    jobs = models.IntegerField()
    upgradeid = models.IntegerField()
    catagoryid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'merits'


class MobDroplist(models.Model):
    dropid = models.SmallIntegerField(db_column='dropId')  # Field name made lowercase.
    type = models.IntegerField()
    itemid = models.SmallIntegerField(db_column='itemId')  # Field name made lowercase.
    rate = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mob_droplist'


class MobFamilyMods(models.Model):
    familyid = models.SmallIntegerField()
    modid = models.SmallIntegerField()
    value = models.SmallIntegerField()
    type = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mob_family_mods'
        unique_together = (('familyid', 'modid'),)


class MobFamilySystem(models.Model):
    familyid = models.SmallIntegerField(primary_key=True)
    family = models.TextField(blank=True, null=True)
    systemid = models.IntegerField()
    system = models.TextField(blank=True, null=True)
    mobsize = models.IntegerField()
    speed = models.IntegerField()
    hp = models.IntegerField(db_column='HP')  # Field name made lowercase.
    mp = models.IntegerField(db_column='MP')  # Field name made lowercase.
    str = models.SmallIntegerField(db_column='STR')  # Field name made lowercase.
    dex = models.SmallIntegerField(db_column='DEX')  # Field name made lowercase.
    vit = models.SmallIntegerField(db_column='VIT')  # Field name made lowercase.
    agi = models.SmallIntegerField(db_column='AGI')  # Field name made lowercase.
    int = models.SmallIntegerField(db_column='INT')  # Field name made lowercase.
    mnd = models.SmallIntegerField(db_column='MND')  # Field name made lowercase.
    chr = models.SmallIntegerField(db_column='CHR')  # Field name made lowercase.
    att = models.SmallIntegerField(db_column='ATT')  # Field name made lowercase.
    def_field = models.SmallIntegerField(db_column='DEF')  # Field name made lowercase. Field renamed because it was a Python reserved word.
    acc = models.SmallIntegerField(db_column='ACC')  # Field name made lowercase.
    eva = models.SmallIntegerField(db_column='EVA')  # Field name made lowercase.
    slash = models.FloatField(db_column='Slash')  # Field name made lowercase.
    pierce = models.FloatField(db_column='Pierce')  # Field name made lowercase.
    h2h = models.FloatField(db_column='H2H')  # Field name made lowercase.
    impact = models.FloatField(db_column='Impact')  # Field name made lowercase.
    fire = models.FloatField(db_column='Fire')  # Field name made lowercase.
    ice = models.FloatField(db_column='Ice')  # Field name made lowercase.
    wind = models.FloatField(db_column='Wind')  # Field name made lowercase.
    earth = models.FloatField(db_column='Earth')  # Field name made lowercase.
    lightning = models.FloatField(db_column='Lightning')  # Field name made lowercase.
    water = models.FloatField(db_column='Water')  # Field name made lowercase.
    light = models.FloatField(db_column='Light')  # Field name made lowercase.
    dark = models.FloatField(db_column='Dark')  # Field name made lowercase.
    element = models.FloatField(db_column='Element')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mob_family_system'


class MobGroups(models.Model):
    groupid = models.IntegerField(primary_key=True)
    poolid = models.IntegerField()
    zoneid = models.SmallIntegerField()
    respawntime = models.IntegerField()
    spawntype = models.IntegerField()
    dropid = models.IntegerField()
    hp = models.IntegerField(db_column='HP')  # Field name made lowercase.
    mp = models.IntegerField(db_column='MP')  # Field name made lowercase.
    minlevel = models.IntegerField(db_column='minLevel')  # Field name made lowercase.
    maxlevel = models.IntegerField(db_column='maxLevel')  # Field name made lowercase.
    allegiance = models.IntegerField()
    roam_distance = models.FloatField()

    class Meta:
        managed = False
        db_table = 'mob_groups'


class MobPets(models.Model):
    mob_mobid = models.IntegerField(primary_key=True)
    pet_offset = models.IntegerField()
    job = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mob_pets'


class MobPoolMods(models.Model):
    poolid = models.SmallIntegerField()
    modid = models.SmallIntegerField()
    value = models.SmallIntegerField()
    type = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mob_pool_mods'
        unique_together = (('poolid', 'modid'),)


class MobPools(models.Model):
    poolid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=24, blank=True, null=True)
    familyid = models.SmallIntegerField()
    modelid = models.CharField(max_length=20)
    mjob = models.IntegerField(db_column='mJob')  # Field name made lowercase.
    sjob = models.IntegerField(db_column='sJob')  # Field name made lowercase.
    cmbskill = models.IntegerField(db_column='cmbSkill')  # Field name made lowercase.
    cmbdelay = models.SmallIntegerField(db_column='cmbDelay')  # Field name made lowercase.
    cmbdmgmult = models.SmallIntegerField(db_column='cmbDmgMult')  # Field name made lowercase.
    behavior = models.SmallIntegerField()
    aggro = models.SmallIntegerField()
    links = models.IntegerField()
    mobtype = models.SmallIntegerField(db_column='mobType')  # Field name made lowercase.
    immunity = models.IntegerField()
    name_prefix = models.IntegerField()
    flag = models.IntegerField()
    flags = models.IntegerField()
    animationsub = models.IntegerField()
    hasspellscript = models.IntegerField(db_column='hasSpellScript')  # Field name made lowercase.
    spelllist = models.SmallIntegerField(db_column='spellList')  # Field name made lowercase.
    namevis = models.IntegerField()
    roamflag = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mob_pools'


class MobSkill(models.Model):
    mob_skill_id = models.SmallIntegerField()
    family_id = models.SmallIntegerField()
    mob_anim_id = models.SmallIntegerField()
    mob_skill_name = models.CharField(max_length=25)
    mob_skill_aoe = models.IntegerField()
    mob_skill_distance = models.FloatField()
    mob_anim_time = models.SmallIntegerField()
    mob_prepare_time = models.SmallIntegerField()
    mob_valid_targets = models.SmallIntegerField()
    mob_skill_flag = models.IntegerField()
    mob_skill_param = models.SmallIntegerField()
    knockback = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mob_skill'
        unique_together = (('mob_skill_id', 'family_id', 'mob_skill_flag'),)


class MobSpawnMods(models.Model):
    mobid = models.IntegerField()
    modid = models.SmallIntegerField()
    value = models.SmallIntegerField()
    type = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mob_spawn_mods'
        unique_together = (('mobid', 'modid'),)


class MobSpawnPoints(models.Model):
    mobid = models.IntegerField(primary_key=True)
    mobname = models.CharField(max_length=24, blank=True, null=True)
    polutils_name = models.CharField(max_length=50, blank=True, null=True)
    groupid = models.IntegerField()
    pos_x = models.FloatField()
    pos_y = models.FloatField()
    pos_z = models.FloatField()
    pos_rot = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mob_spawn_points'


class MobSpellLists(models.Model):
    spell_list_name = models.CharField(max_length=20, blank=True, null=True)
    spell_list_id = models.SmallIntegerField()
    spell_id = models.SmallIntegerField()
    min_level = models.IntegerField()
    max_level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mob_spell_lists'
        unique_together = (('spell_list_id', 'spell_id'),)


class NmSpawnPoints(models.Model):
    mobid = models.IntegerField()
    pos = models.IntegerField()
    pos_x = models.FloatField()
    pos_y = models.FloatField()
    pos_z = models.FloatField()

    class Meta:
        managed = False
        db_table = 'nm_spawn_points'
        unique_together = (('mobid', 'pos'),)


class NpcList(models.Model):
    npcid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=24, blank=True, null=True)
    polutils_name = models.CharField(max_length=50, blank=True, null=True)
    pos_rot = models.IntegerField()
    pos_x = models.FloatField()
    pos_y = models.FloatField()
    pos_z = models.FloatField()
    flag = models.IntegerField()
    speed = models.IntegerField()
    speedsub = models.IntegerField()
    animation = models.IntegerField()
    animationsub = models.IntegerField()
    namevis = models.IntegerField()
    status = models.IntegerField()
    flags = models.IntegerField()
    look = models.CharField(max_length=20)
    name_prefix = models.IntegerField()
    required_expansion = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'npc_list'


class PetList(models.Model):
    petid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15)
    poolid = models.IntegerField()
    minlevel = models.IntegerField(db_column='minLevel')  # Field name made lowercase.
    maxlevel = models.IntegerField(db_column='maxLevel')  # Field name made lowercase.
    time = models.IntegerField()
    element = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pet_list'


class PetName(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    name = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'pet_name'


class ServerVariables(models.Model):
    name = models.CharField(primary_key=True, max_length=50)
    value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'server_variables'


class SkillCaps(models.Model):
    level = models.IntegerField(primary_key=True)
    r0 = models.SmallIntegerField()
    r1 = models.SmallIntegerField()
    r2 = models.SmallIntegerField()
    r3 = models.SmallIntegerField()
    r4 = models.SmallIntegerField()
    r5 = models.SmallIntegerField()
    r6 = models.SmallIntegerField()
    r7 = models.SmallIntegerField()
    r8 = models.SmallIntegerField()
    r9 = models.SmallIntegerField()
    r10 = models.SmallIntegerField()
    r11 = models.SmallIntegerField()
    r12 = models.SmallIntegerField()
    r13 = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'skill_caps'


class SkillRanks(models.Model):
    skillid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=12, blank=True, null=True)
    war = models.IntegerField()
    mnk = models.IntegerField()
    whm = models.IntegerField()
    blm = models.IntegerField()
    rdm = models.IntegerField()
    thf = models.IntegerField()
    pld = models.IntegerField()
    drk = models.IntegerField()
    bst = models.IntegerField()
    brd = models.IntegerField()
    rng = models.IntegerField()
    sam = models.IntegerField()
    nin = models.IntegerField()
    drg = models.IntegerField()
    smn = models.IntegerField()
    blu = models.IntegerField()
    cor = models.IntegerField()
    pup = models.IntegerField()
    dnc = models.IntegerField()
    sch = models.IntegerField()
    geo = models.IntegerField()
    run = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'skill_ranks'


class SkillchainDamageModifiers(models.Model):
    chain_level = models.CharField(max_length=1)
    chain_count = models.CharField(max_length=1)
    initial_modifier = models.IntegerField()
    magic_burst_modifier = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'skillchain_damage_modifiers'
        unique_together = (('chain_level', 'chain_count'),)


class SpellList(models.Model):
    spellid = models.SmallIntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    jobs = models.CharField(max_length=22)
    group = models.IntegerField()
    element = models.IntegerField()
    zonemisc = models.SmallIntegerField()
    validtargets = models.IntegerField(db_column='validTargets')  # Field name made lowercase.
    skill = models.IntegerField()
    mpcost = models.SmallIntegerField(db_column='mpCost')  # Field name made lowercase.
    casttime = models.SmallIntegerField(db_column='castTime')  # Field name made lowercase.
    recasttime = models.IntegerField(db_column='recastTime')  # Field name made lowercase.
    message = models.SmallIntegerField()
    magicburstmessage = models.SmallIntegerField(db_column='magicBurstMessage')  # Field name made lowercase.
    animation = models.SmallIntegerField()
    animationtime = models.SmallIntegerField(db_column='animationTime')  # Field name made lowercase.
    aoe = models.IntegerField(db_column='AOE')  # Field name made lowercase.
    base = models.SmallIntegerField()
    multiplier = models.FloatField()
    ce = models.IntegerField(db_column='CE')  # Field name made lowercase.
    ve = models.IntegerField(db_column='VE')  # Field name made lowercase.
    requirements = models.IntegerField()
    spell_range = models.SmallIntegerField()
    required_expansion = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spell_list'


class StatusEffects(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    flags = models.IntegerField()
    type = models.SmallIntegerField()
    negative_id = models.SmallIntegerField(blank=True, null=True)
    overwrite = models.SmallIntegerField()
    block_id = models.SmallIntegerField(blank=True, null=True)
    remove_id = models.SmallIntegerField()
    element = models.SmallIntegerField()
    min_duration = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'status_effects'


class SynthRecipes(models.Model):
    id = models.SmallIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type')  # Field name made lowercase.
    keyitem = models.IntegerField(db_column='KeyItem')  # Field name made lowercase.
    alchemy = models.IntegerField(db_column='Alchemy')  # Field name made lowercase.
    bone = models.IntegerField(db_column='Bone')  # Field name made lowercase.
    cloth = models.IntegerField(db_column='Cloth')  # Field name made lowercase.
    cook = models.IntegerField(db_column='Cook')  # Field name made lowercase.
    gold = models.IntegerField(db_column='Gold')  # Field name made lowercase.
    leather = models.IntegerField(db_column='Leather')  # Field name made lowercase.
    smith = models.IntegerField(db_column='Smith')  # Field name made lowercase.
    wood = models.IntegerField(db_column='Wood')  # Field name made lowercase.
    crystal = models.SmallIntegerField(db_column='Crystal')  # Field name made lowercase.
    hqcrystal = models.SmallIntegerField(db_column='HQCrystal')  # Field name made lowercase.
    ingredient1 = models.SmallIntegerField(db_column='Ingredient1')  # Field name made lowercase.
    ingredient2 = models.SmallIntegerField(db_column='Ingredient2')  # Field name made lowercase.
    ingredient3 = models.SmallIntegerField(db_column='Ingredient3')  # Field name made lowercase.
    ingredient4 = models.SmallIntegerField(db_column='Ingredient4')  # Field name made lowercase.
    ingredient5 = models.SmallIntegerField(db_column='Ingredient5')  # Field name made lowercase.
    ingredient6 = models.SmallIntegerField(db_column='Ingredient6')  # Field name made lowercase.
    ingredient7 = models.SmallIntegerField(db_column='Ingredient7')  # Field name made lowercase.
    ingredient8 = models.SmallIntegerField(db_column='Ingredient8')  # Field name made lowercase.
    result = models.SmallIntegerField(db_column='Result')  # Field name made lowercase.
    resulthq1 = models.SmallIntegerField(db_column='ResultHQ1')  # Field name made lowercase.
    resulthq2 = models.SmallIntegerField(db_column='ResultHQ2')  # Field name made lowercase.
    resulthq3 = models.SmallIntegerField(db_column='ResultHQ3')  # Field name made lowercase.
    resultqty = models.IntegerField(db_column='ResultQty')  # Field name made lowercase.
    resulthq1qty = models.IntegerField(db_column='ResultHQ1Qty')  # Field name made lowercase.
    resulthq2qty = models.IntegerField(db_column='ResultHQ2Qty')  # Field name made lowercase.
    resulthq3qty = models.IntegerField(db_column='ResultHQ3Qty')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'synth_recipes'


class Traits(models.Model):
    traitid = models.IntegerField()
    name = models.TextField()
    job = models.IntegerField()
    level = models.IntegerField()
    rank = models.IntegerField()
    modifier = models.SmallIntegerField()
    value = models.SmallIntegerField()
    required_expansion = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'traits'


class Transport(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    transport = models.IntegerField()
    door = models.IntegerField()
    dock_x = models.FloatField()
    dock_y = models.FloatField()
    dock_z = models.FloatField()
    dock_rot = models.IntegerField()
    boundary = models.SmallIntegerField()
    anim_arrive = models.IntegerField()
    anim_depart = models.IntegerField()
    time_offset = models.SmallIntegerField()
    time_interval = models.SmallIntegerField()
    time_anim_arrive = models.IntegerField()
    time_waiting = models.SmallIntegerField()
    time_anim_depart = models.IntegerField()
    zone = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'transport'


class TreasureSpawnPoints(models.Model):
    npcid = models.IntegerField()
    pos = models.IntegerField()
    pos_rot = models.IntegerField()
    pos_x = models.FloatField()
    pos_y = models.FloatField()
    pos_z = models.FloatField()

    class Meta:
        managed = False
        db_table = 'treasure_spawn_points'
        unique_together = (('npcid', 'pos'),)


class WaterPoints(models.Model):
    waterid = models.AutoField(primary_key=True)
    zoneid = models.SmallIntegerField()
    type = models.IntegerField()
    pointid = models.IntegerField()
    pos_x = models.FloatField()
    pos_y = models.FloatField()
    pos_z = models.FloatField()

    class Meta:
        managed = False
        db_table = 'water_points'


class WeaponSkills(models.Model):
    weaponskillid = models.IntegerField(primary_key=True)
    name = models.TextField()
    jobs = models.CharField(max_length=22)
    type = models.IntegerField()
    skilllevel = models.SmallIntegerField()
    element = models.IntegerField()
    animation = models.IntegerField()
    range = models.IntegerField()
    aoe = models.IntegerField()
    primary_sc = models.IntegerField()
    secondary_sc = models.IntegerField()
    tertiary_sc = models.IntegerField()
    main_only = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'weapon_skills'


class ZoneSettings(models.Model):
    zoneid = models.SmallIntegerField(primary_key=True)
    zonetype = models.SmallIntegerField()
    zoneip = models.TextField()
    zoneport = models.SmallIntegerField()
    name = models.TextField()
    music_day = models.IntegerField()
    music_night = models.IntegerField()
    battlesolo = models.IntegerField()
    battlemulti = models.IntegerField()
    restriction = models.IntegerField()
    tax = models.FloatField()
    misc = models.SmallIntegerField()
    navmesh = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'zone_settings'


class ZoneWeather(models.Model):
    zoneid = models.SmallIntegerField()
    weather_day = models.SmallIntegerField()
    common = models.IntegerField()
    normal = models.IntegerField()
    rare = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'zone_weather'
        unique_together = (('zoneid', 'weather_day'),)


class Zonelines(models.Model):
    zoneline = models.IntegerField(primary_key=True)
    fromzone = models.SmallIntegerField()
    tozone = models.SmallIntegerField()
    tox = models.FloatField()
    toy = models.FloatField()
    toz = models.FloatField()
    rotation = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'zonelines'
