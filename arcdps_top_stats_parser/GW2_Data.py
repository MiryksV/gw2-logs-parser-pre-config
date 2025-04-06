#GW2 Data Dictionaries
"""
 Damage_Conditions Dictionary
    {ConditionName: IconURL}
 Control_Conditions Dictionary
    {ConditionName: IconURL}
 Other_Conditions Dictionary
    {ConditionName: IconURL}
 All_Conditions Dictionary
    {ConditionName: IconURL}
 Control_Effects Dictionary
    {EffectName: IconURL}
 Boons Dictionary
    {BoonnName: IconURL}
 Auras Dictionary
    {AuraaName: IconURL}
 WvW_SiegeSkills Dictionary
    {skillID: SkillName}
 ProfIcon Dictionary
    {Profession: [20px IconURL, 40px IconURL]}
"""


# Damage Conditions
Damage_Conditions = {
"Bleeding": "https://wiki.guildwars2.com/images/3/33/Bleeding.png",
"Burning": "https://wiki.guildwars2.com/images/4/45/Burning.png",
"Confusion": "https://wiki.guildwars2.com/images/e/e6/Confusion.png",
"Poisoned": "https://wiki.guildwars2.com/images/1/11/Poisoned.png",
"Torment": "https://wiki.guildwars2.com/images/0/08/Torment.png"
}

#Control Conditions
Control_Conditions = {
"Blinded": "https://wiki.guildwars2.com/images/3/33/Blinded.png",
"Chilled": "https://wiki.guildwars2.com/images/a/a6/Chilled.png",
"Crippled": "https://wiki.guildwars2.com/images/f/fb/Crippled.png",
"Fear": "https://wiki.guildwars2.com/images/e/e6/Fear.png",
"Immobile": "https://wiki.guildwars2.com/images/3/32/Immobile.png",
"Slow": "https://wiki.guildwars2.com/images/f/f5/Slow.png",
"Taunt": "https://wiki.guildwars2.com/images/c/cc/Taunt.png",
"Weakness": "https://wiki.guildwars2.com/images/f/f9/Weakness.png"
}

#Other Conditions
Other_Conditions = {
"Vulnerabilty": "https://wiki.guildwars2.com/images/a/af/Vulnerability.png"
}

#All Conditions
All_Conditions = {
	**Damage_Conditions,
	**Control_Conditions,
	**Other_Conditions
}

#Control Effects
Control_Effects = {
"Daze": "https://wiki.guildwars2.com/images/7/79/Daze.png",
"Stun": "https://wiki.guildwars2.com/images/9/97/Stun.png",
"Knockdown": "https://wiki.guildwars2.com/images/3/36/Knockdown.png",
"Pull": "https://wiki.guildwars2.com/images/3/31/Pull.png",
"Knockback": "https://wiki.guildwars2.com/images/c/ca/Knockback.png",
"Launch": "https://wiki.guildwars2.com/images/6/68/Launch.png",
"Float": "https://wiki.guildwars2.com/images/c/c8/Float.png",
"Sink": "https://wiki.guildwars2.com/images/6/66/Sink.png"
}

#Boons
Boons = {
"Aegis": "https://wiki.guildwars2.com/images/e/e5/Aegis.png",
"Alacrity": "https://wiki.guildwars2.com/images/4/4c/Alacrity.png",
"Fury": "https://wiki.guildwars2.com/images/4/46/Fury.png",
"Might": "https://wiki.guildwars2.com/images/7/7c/Might.png",
"Protection": "https://wiki.guildwars2.com/images/6/6c/Protection.png",
"Quickness": "https://wiki.guildwars2.com/images/b/b4/Quickness.png",
"Regeneration": "https://wiki.guildwars2.com/images/5/53/Regeneration.png",
"Resistance": "https://wiki.guildwars2.com/images/4/4b/Resistance.png",
"Resolution": "https://wiki.guildwars2.com/images/0/06/Resolution.png",
"Stability": "https://wiki.guildwars2.com/images/a/ae/Stability.png",
"Swiftness": "https://wiki.guildwars2.com/images/a/af/Swiftness.png",
"Vigor": "https://wiki.guildwars2.com/images/f/f4/Vigor.png"
}


#Auras
Auras = {
	"Chaos_Aura": "https://wiki.guildwars2.com/images/e/ec/Chaos_Aura.png",
	"Dark_Aura": "https://wiki.guildwars2.com/images/e/ef/Dark_Aura.png",
	"Fire_Aura": "https://wiki.guildwars2.com/images/c/ce/Fire_Aura.png",
	"Frost_Aura": "https://wiki.guildwars2.com/images/8/87/Frost_Aura_%28effect%29.png",
	"Light_Aura": "https://wiki.guildwars2.com/images/5/5a/Light_Aura.png",
	"Magnetic_Aura": "https://wiki.guildwars2.com/images/0/0b/Magnetic_Aura_%28effect%29.png",
	"Shocking_Aura": "https://wiki.guildwars2.com/images/5/5d/Shocking_Aura_%28effect%29.png",
}

WvW_SiegeSkills = {
	14600: "TurnRightCatapult",
	14601: "TurnLeftCatapult",
	14602: "FireBoulderSkill",
	14611: "TurnLeftMortar",
	14612: "TurnRightMortar",
	14613: "FireTrebuchetSkill",
	14614: "FireTrebuchetDamage1",
	14615: "TurnLeftTrebuchet",
	14616: "TurnRightTrebuchet",
	14618: "VolleyArrowCart",
	14622: "BallistaBolt",
	14627: "PunchSiegeGolem",
	14628: "DeployCatapult",
	14629: "DeployTrebuchet",
	14631: "DeployArrowCart",
	14632: "DeployBallista",
	14633: "DeployAlphaSiegeSuit",
	14639: "WhirlingAssaultSiegeGolem",
	14642: "EjectSiegeGolem",
	14643: "GravelShot2",
	14644: "GravelShotSkill",
	14650: "CripplingVolley",
	14651: "BarbedVolley",
	14655: "ReinforcedShotDamage",
	14665: "RottenCow1",
	14672: "PullSiegeGolem",
	14676: "Ram",
	14678: "DeployFlameRam",
	14680: "DeployGuildCatapult",
	14681: "DeployGuildSiegeSuit",
	14697: "DeploySuperiorCatapult",
	14699: "DeploySuperiorTrebuchet",
	14705: "DeploySuperiorArrowCart",
	14706: "DeploySuperiorBallista",
	14707: "DeployOmegaSiegeSuit",
	14708: "RocketSalvo",
	14709: "RocketPunch",
	14710: "WhirlingInferno",
	14711: "DeploySuperiorFlameRam",
	14712: "SiegeDeploymentBlocked",
	18526: "FireCannonStrips1",
	18529: "GrapeshotDamage",
	18531: "GrapeshotDamageDoubleBleeds1",
	18533: "GrapeshotDamageDoubleBleeds2",
	18535: "FireCannonRadius",
	18537: "FireCannonStrips2",
	18539: "IceShotDamage",
	18541: "IceShotRadiusDamage",
	18543: "IceShot",
	18564: "ImprovedReinforcedShotDamage",
	18568: "ImprovedShatteringBoltDamage",
	18570: "SwiftBoltDamage",
	18574: "SniperBoltDamage",
	18576: "GreaterReinforcedShotDamage",
	18578: "GreaterShatteringBoltDamage",
	18585: "DeployGuildTrebuchet",
	18586: "DeployGuildBallista",
	18591: "SiegeDecayTimer",
	18846: "FirePenetratingSniperArrows",
	18848: "FireReapingArrow",
	18850: "FireDistantVolley",
	18853: "FireImprovedArrows",
	18855: "FireImprovedCripplingArrows",
	18857: "FireImprovedBarbedArrows",
	18860: "FireExsanguinatingArrows",
	18862: "FireStaggeringArrows",
	18865: "FireSufferingArrows",
	18867: "FireDevastatingArrows",
	18869: "FireMercilessArrows",
	18872: "ToxicUnveilingVolley",
	19579: "FireBoulder",
	19601: "FireExplosiveShellsSkill",
	19602: "FireExplosiveShellsDamage",
	19626: "ConcussionBarrageDamage",
	19627: "ConcussionBarrageSkill",
	20242: "HeavyBoulderShot1",
	20243: "GravelShot4",
	20250: "RendingGravelSkill",
	20254: "HeavyBoulderShot2",
	20259: "FireLargeRendingGravelSkill",
	20260: "FireLargeHeavyBoulderSkill",
	20268: "FireHollowedGravelSkill",
	20269: "FireHollowedBoulderSkill",
	20272: "HollowedBoulderShot",
	20273: "HollowedGravelShot",
	20277: "FireHeavyBoulder1",
	20280: "FireLargeHeavyBoulder",
	20284: "FireHollowedGravel",
	20285: "FireHollowedBoulder",
	20290: "FireHeavyBoulder2",
	20978: "FireRottingCow2",
	20979: "FireMegaExplosiveShot1",
	20983: "FireMegaExplosiveShot2",
	20986: "FireBloatedPutridCow",
	20987: "FireColossalExplosiveShot",
	20992: "FireCorrosiveShot1",
	20990: "FireHealingOasisHealing",
	20995: "FireHealingOasisSkill",
	21005: "FireMegaExplosiveShot3",
	21006: "FireRottingCow1",
	21009: "FireTrebuchetDamage2",
	21010: "RottenCow2"
}

#Profession Icons in 20px[0] and 48px[1]
ProfIcon = {
    #Elementalist Professions
    "Elementalist": ["https://wiki.guildwars2.com/images/5/55/Elementalist_tango_icon_20px.png", "https://wiki.guildwars2.com/images/5/55/Elementalist_tango_icon_48px.png"],
	"Tempest": ["https://wiki.guildwars2.com/images/4/40/Tempest_tango_icon_20px.png", "https://wiki.guildwars2.com/images/4/40/Tempest_tango_icon_48px.png"],
	"Weaver": ["https://wiki.guildwars2.com/images/2/2f/Weaver_tango_icon_20px.png", "https://wiki.guildwars2.com/images/2/2f/Weaver_tango_icon_48px.png"],
	"Catalyst": ["https://wiki.guildwars2.com/images/0/08/Catalyst_tango_icon_20px.png", "https://wiki.guildwars2.com/images/0/08/Catalyst_tango_icon_48px.png"],
	#Mesmer Professions
	"Mesmer": ["https://wiki.guildwars2.com/images/3/38/Mesmer_tango_icon_20px.png", "https://wiki.guildwars2.com/images/3/38/Mesmer_tango_icon_48px.png"],
	"Chronomancer": ["https://wiki.guildwars2.com/images/f/f2/Chronomancer_tango_icon_20px.png", "https://wiki.guildwars2.com/images/f/f2/Chronomancer_tango_icon_48px.png"],
	"Mirage": ["https://wiki.guildwars2.com/images/9/94/Mirage_tango_icon_20px.png", "https://wiki.guildwars2.com/images/9/94/Mirage_tango_icon_48px.png"],
	"Virtuoso": ["https://wiki.guildwars2.com/images/2/21/Virtuoso_tango_icon_20px.png", "https://wiki.guildwars2.com/images/2/21/Virtuoso_tango_icon_48px.png"],
	#Necromancer Professions
	"Necromancer": ["https://wiki.guildwars2.com/images/e/ea/Necromancer_tango_icon_20px.png", "https://wiki.guildwars2.com/images/e/ea/Necromancer_tango_icon_48px.png"],
	"Reaper": ["https://wiki.guildwars2.com/images/3/39/Reaper_tango_icon_20px.png", "https://wiki.guildwars2.com/images/3/39/Reaper_tango_icon_48px.png"],
	"Scourge": ["https://wiki.guildwars2.com/images/4/49/Scourge_tango_icon_20px.png", "https://wiki.guildwars2.com/images/4/49/Scourge_tango_icon_48px.png"],
	"Harbinger": ["https://wiki.guildwars2.com/images/e/eb/Harbinger_tango_icon_20px.png", "https://wiki.guildwars2.com/images/e/eb/Harbinger_tango_icon_48px.png"],
	#Engineer Professions
	"Engineer": ["https://wiki.guildwars2.com/images/d/dd/Engineer_tango_icon_20px.png", "https://wiki.guildwars2.com/images/d/dd/Engineer_tango_icon_48px.png"],
	"Scrapper": ["https://wiki.guildwars2.com/images/4/4a/Scrapper_tango_icon_20px.png", "https://wiki.guildwars2.com/images/4/4a/Scrapper_tango_icon_48px.png"],
	"Holosmith": ["https://wiki.guildwars2.com/images/4/4f/Holosmith_tango_icon_20px.png", "https://wiki.guildwars2.com/images/4/4f/Holosmith_tango_icon_48px.png"],
	"Mechanist": ["https://wiki.guildwars2.com/images/f/f5/Mechanist_tango_icon_20px.png", "https://wiki.guildwars2.com/images/f/f5/Mechanist_tango_icon_48px.png"],
	#Ranger Professions
	"Ranger": ["https://wiki.guildwars2.com/images/b/b5/Ranger_tango_icon_20px.png", "https://wiki.guildwars2.com/images/b/b5/Ranger_tango_icon_48px.png"],
	"Druid": ["https://wiki.guildwars2.com/images/9/91/Druid_tango_icon_20px.png", "https://wiki.guildwars2.com/images/9/91/Druid_tango_icon_48px.png"],
	"Soulbeast": ["https://wiki.guildwars2.com/images/4/4f/Soulbeast_tango_icon_20px.png", "https://wiki.guildwars2.com/images/4/4f/Soulbeast_tango_icon_48px.png"],
	"Untamed": ["https://wiki.guildwars2.com/images/9/90/Untamed_tango_icon_20px.png", "https://wiki.guildwars2.com/images/9/90/Untamed_tango_icon_48px.png"],
	#Thief Professions
	"Thief": ["https://wiki.guildwars2.com/images/c/cd/Thief_tango_icon_20px.png", "https://wiki.guildwars2.com/images/c/cd/Thief_tango_icon_48px.png"],
	"Daredevil": ["https://wiki.guildwars2.com/images/6/61/Daredevil_tango_icon_20px.png", "https://wiki.guildwars2.com/images/6/61/Daredevil_tango_icon_48px.png"],
	"Deadeye": ["https://wiki.guildwars2.com/images/8/81/Deadeye_tango_icon_20px.png", "https://wiki.guildwars2.com/images/8/81/Deadeye_tango_icon_48px.png"],
	"Specter": ["https://wiki.guildwars2.com/images/d/d7/Specter_tango_icon_20px.png", "https://wiki.guildwars2.com/images/d/d7/Specter_tango_icon_48px.png"],
	#Guardian Progessions
	"Guardian": ["https://wiki.guildwars2.com/images/5/53/Guardian_tango_icon_20px.png", "https://wiki.guildwars2.com/images/5/53/Guardian_tango_icon_48px.png"],
	"Dragonhunter": ["https://wiki.guildwars2.com/images/f/fe/Dragonhunter_tango_icon_20px.png", "https://wiki.guildwars2.com/images/f/fe/Dragonhunter_tango_icon_48px.png"],
	"Firebrand": ["https://wiki.guildwars2.com/images/f/ff/Firebrand_tango_icon_20px.png", "https://wiki.guildwars2.com/images/f/ff/Firebrand_tango_icon_48px.png"],
	"Willbender": ["https://wiki.guildwars2.com/images/d/dd/Willbender_tango_icon_20px.png", "https://wiki.guildwars2.com/images/d/dd/Willbender_tango_icon_48px.png"],
	#Revenant Professions
	"Revenant": ["https://wiki.guildwars2.com/images/5/53/Revenant_tango_icon_20px.png", "https://wiki.guildwars2.com/images/5/53/Revenant_tango_icon_48px.png"],
	"Herald": ["https://wiki.guildwars2.com/images/8/8f/Herald_tango_icon_20px.png", "https://wiki.guildwars2.com/images/8/8f/Herald_tango_icon_48px.png"],
	"Renegade": ["https://wiki.guildwars2.com/images/4/4c/Renegade_tango_icon_20px.png", "https://wiki.guildwars2.com/images/4/4c/Renegade_tango_icon_48px.png"],
	"Vindicator": ["https://wiki.guildwars2.com/images/d/dd/Vindicator_tango_icon_20px.png", "https://wiki.guildwars2.com/images/d/dd/Vindicator_tango_icon_48px.png"],
	#Warrior Professions
	"Warrior": ["https://wiki.guildwars2.com/images/2/28/Warrior_tango_icon_20px.png", "https://wiki.guildwars2.com/images/2/28/Warrior_tango_icon_48px.png"],
	"Berserker": ["https://wiki.guildwars2.com/images/7/70/Berserker_tango_icon_20px.png", "https://wiki.guildwars2.com/images/7/70/Berserker_tango_icon_48px.png"],
	"Spellbreaker": ["https://wiki.guildwars2.com/images/4/42/Spellbreaker_tango_icon_20px.png", "https://wiki.guildwars2.com/images/4/42/Spellbreaker_tango_icon_48px.png"],
	"Bladesworn": ["https://wiki.guildwars2.com/images/f/f8/Bladesworn_tango_icon_20px.png", "https://wiki.guildwars2.com/images/f/f8/Bladesworn_tango_icon_48px.png"]
}