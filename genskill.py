#! /usr/bin/python
from random import randint

def merge_two_dicts(x, y):
    z = x.copy()   # start with x's keys and values
    z.update(y)    # modifies z with y's keys and values & returns None
    return z

# templates
def value(baseValueConstant, baseValueAttribute, initializationDefinition, baseValueScaleConstant):
    return {
        "BaseValueConstant": baseValueConstant,
        "BaseValueAttribute": baseValueAttribute,
        "InitializationDefinition": initializationDefinition,
        "BaseValueScaleConstant": baseValueScaleConstant
    }

def kValue(k): return value(k, None, None, 1)
zeroValue = kValue(0)

def strValue(baseValueConstant, baseValueAttribute, initializationDefinition, baseValueScaleConstant): 
    return "(BaseValueConstant=%f,BaseValueAttribute=%s,InitializationDefinition=%s,BaseValueScaleConstant=%f)" % (baseValueConstant, baseValueAttribute, initializationDefinition, baseValueScaleConstant)

def strValueDict(v):
    return "(BaseValueConstant={BaseValueConstant},BaseValueAttribute={BaseValueAttribute},InitializationDefinition={InitializationDefinition},BaseValueScaleConstant={BaseValueScaleConstant})".format(**v)

def attr(**k):
    return merge_two_dicts({
        "AttributeToModify": "",
        "bIncludeDuelingTargets": "False",
        "bIncludeSelfAsTarget": "False",
        "bOnlyEffectTargetsInRange": "False",
        "bExcludeNonPlayerCharacters": "False",
        "EffectTarget": "TARGET_None",
        "TargetInstanceDataName": "",
        "TargetCriteria": "CRITERIA_None",
        "ModifierType": "MT_Scale",
        "BaseModifierValue": zeroValue,
        "GradeToStartApplyingEffect": 1,
        "PerGradeUpgradeInterval": 1,
        "PerGradeUpgrade": zeroValue,
        "BonusUpgradeList": ""
    }, k)

def strAttr(k):
    kclone = k.copy()
    kclone["BaseModifierValue"] = strValueDict(kclone["BaseModifierValue"])
    kclone["PerGradeUpgrade"] = strValueDict(kclone["PerGradeUpgrade"])
    
    return "(AttributeToModify={AttributeToModify},bIncludeDuelingTargets={bIncludeDuelingTargets},bIncludeSelfAsTarget={bIncludeSelfAsTarget},bOnlyEffectTargetsInRange={bOnlyEffectTargetsInRange},bExcludeNonPlayerCharacters={bExcludeNonPlayerCharacters},EffectTarget={EffectTarget},TargetInstanceDataName={TargetInstanceDataName},TargetCriteria={TargetCriteria},ModifierType={ModifierType},BaseModifierValue={BaseModifierValue},GradeToStartApplyingEffect={GradeToStartApplyingEffect},PerGradeUpgradeInterval={PerGradeUpgradeInterval},PerGradeUpgrade={PerGradeUpgrade},BonusUpgradeList={BonusUpgradeList})".format(**kclone)

####
def skill(package, name, k): 
    """k :: (string -> string)"""
    return {
        "package": package,
        "name": name,
        "behaviors": k
    }
def skillA(name, k): return skill("GD_Assassin_Streaming", name, k)

def strSkill(s):
    def strField(field, behaviors):
        val = ""
        if field == "SkillEffectDefinitions":
            val = '(' + ','.join([strAttr(x) for x in behaviors["SkillEffectDefinitions"]]) + ')'
        else: val = behaviors[field]
        return '#<hotfix><key>"SparkOnDemandPatchEntry-%d"</key><value>"%s,%s,%s,,%s"</value><on>\n' % (randint(100000, 999999), s["package"], s["name"], field, val)

    behaviors = s["behaviors"]
    return [strField(field, behaviors) for field in behaviors]












#### actual skills

## CA
caMenu = skillA("GD_Assassin_Skills.Sniping.CriticalAscention:BehaviorProviderDefinition_9", {
    "BehaviorSequences[0].EventData2[1].UserData.bEnabled": "False" 
})

caTimer = skillA("GD_Assassin_Skills.Sniping.CriticalAscention_Stack", {
    "InitialDuration": "1800" 
})

## kunai
friendlyKunai = skillA("GD_Assassin_Skills.ActionSkill.Skill_Stealth:BehaviorProviderDefinition_0.Behavior_SpawnProjectile_0", { 
    # "bInflictRadiusDamageOnOwner": "False",
    "DirectionConeSize": "0.1" 
})

fastKunai = skillA ("GD_Assassin_Skills.Misc.Projectile_Kunai", { 
    "SpeedFormula": strValue(4500, None, None, 2) 
})

slagKunai126 = skillA ("GD_Assassin_Skills.Misc.Projectile_Kunai:BehaviorProviderDefinition_0.Behavior_Explode_126", {
    "StatusEffectChance": value(1, None, None, 4),
    "Definition": "ExplosionDefinition'GD_Explosions.Slag.Explosion_SlagMaster'"
})
slagKunai128 = skillA ("GD_Assassin_Skills.Misc.Projectile_Kunai:BehaviorProviderDefinition_0.Behavior_Explode_128", {
    "StatusEffectChance": value(1, None, None, 4),
    "Definition": "ExplosionDefinition'GD_Explosions.Slag.Explosion_SlagMaster'"
})
slagKunai130 = skillA ("GD_Assassin_Skills.Misc.Projectile_Kunai:BehaviorProviderDefinition_0.Behavior_Explode_130", {
    "StatusEffectChance": value(1, None, None, 4),
    "Definition": "ExplosionDefinition'GD_Explosions.Slag.Explosion_SlagMaster'"
})

## swap Fearless and Grim
swapFearlessGrim = skillA("GD_Assassin_Skills.SkillTree.Branch_BloodShed", {
    "Tiers[1].Skills[0]": "SkillDefinition'GD_Assassin_Skills.Cunning.Fearless" }
)

swapGrimFearless = skillA("GD_Assassin_Skills.SkillTree.Branch_Cunning", {
    "Tiers[0].Skills[1]": "SkillDefinition'GD_Assassin_Skills.Bloodshed.Grim" }
)

## CS
csActivationChance = skillA("GD_Assassin_Skills.Misc.Att_CounterStrike_ActivationChance", {
    "BaseValue": strValue(0.00, None, None, 1) 
})

csActive = skillA("GD_Assassin_Skills.Cunning.CounterStrike_Active", {
    "InitialDuration": 90,
    "DamageEvents": "()",
    "KillEvents": r"((EventType=SKE_KilledEnemy,EventConstraints=((DamageTypeConstraint=None,DamageSourceConstraint=Class'WillowGame.WillowDmgSource_Melee',bMustBeCriticalDamage=False,bMustBeOneShotKill=False)),EventName=\"Damaged Enemy with Melee\"))",

    "SkillEffectDefinitions": [
        attr(
            AttributeToModify="AttributeDefinition'D_Attributes.DamageEnhancementModifiers.PlayerAttackUnsuspectingTargetModifier'",
            EffectTarget="TARGET_Self",
            ModifierType="MT_Scale",
            BaseModifierValue=kValue(1.5)),
        # attr(
        #     AttributeToModify="AttributeDefinition'D_Attributes.DamageEnhancementModifiers.PlayerMeleeAttackTargetFromBehindModifier'",
        #     EffectTarget="TARGET_Self",
        #     ModifierType="MT_Scale",
        #     BaseModifierValue=kValue(0.3)),
        # ensure atleast one deception
        attr(
            AttributeToModify="AttributeDefinition'D_Attributes.ActiveSkillCooldownResource.ActiveSkillCooldownConsumptionRate'",
            EffectTarget="TARGET_Self",
            ModifierType="MT_Scale",
            BaseModifierValue=kValue(0.33)),
        # prevent CC from triggering during CC
        # attr(
        #     AttributeToModify="DesignerAttributeDefinition'GD_Assassin_Skills.Misc.Att_CounterStrike_ActivationChance'",
        #     EffectTarget="TARGET_Self",
        #     ModifierType="MT_PostAdd",
        #     BaseModifierValue=kValue(-1))
    ]
})

cs = skillA("GD_Assassin_Skills.Cunning.CounterStrike", {
    "DamageEvents": r"((EventType=SDE_DamagedEnemy,EventConstraints=((DamageTypeConstraint=None,DamageSourceConstraint=Class'WillowGame.WillowDmgSource_Melee',bMustBeCriticalDamage=False,bMustBeOneShotKill=False)),EventName=\"AssassinTookDamage\"))",

    "SkillEffectDefinitions": [
        attr(
            AttributeToModify="DesignerAttributeDefinition'GD_Assassin_Skills.Misc.Att_CounterStrike_ActivationChance'",
            EffectTarget="TARGET_Self",
            ModifierType="MT_PreAdd",
            BaseModifierValue=value(0, "DesignerAttributeDefinition'GD_Assassin_Skills.Misc.Att_ActionSkillIsActive'", None, -0.83),
            PerGradeUpgrade=value(0, "DesignerAttributeDefinition'GD_Assassin_Skills.Misc.Att_ActionSkillIsActive'", None, 0.25)),
        
    ],
  
    "SkillDescription": "Executing in deception has a chance to add a [skill]FRENZY[-skill] stack. Stacks stay until the next [skill]melee kill[-skill] and give +[skill]100%[-skill] ambush damage."  
})

csUI = skillA("GD_Assassin_Skills.Cunning.CounterStrike:AttributePresentationDefinition_0", {
    "Attribute": "DesignerAttributeDefinition'GD_Assassin_Skills.Misc.Att_CounterStrike_ActivationChance'",
    "SignStyle": "SIGNSTYLE_AsIs",
    "Description": "Counter Strike Activation Chance: $NUMBER$",
    "RoundingMode": "ATTRROUNDING_Float",
    "bDisplayPercentAsFloat": "True"
})

## fearless
fearlessUI1 = skillA("GD_Assassin_Skills.Cunning.Fearless:AttributePresentationDefinition_7", {
    "Attribute": "AttributeDefinition'D_Attributes.Weapon.WeaponProjectilesPerShot'",
    "Description": "Projectiles:  $NUMBER$"
})
fearlessUI2 = skillA("GD_Assassin_Skills.Cunning.Fearless:AttributePresentationDefinition_6", {
    "Attribute": "ResourcePoolAttributeDefinition'D_Attributes.HealthResourcePool.HealthActiveRegenerationRate'",
    "SignStyle": "SIGNSTYLE_AsIs",
    "Description": "Regenerates $NUMBER$ of your Max Health / sec.",
    "RoundingMode": "ATTRROUNDING_Float",
    "bDisplayPercentAsFloat": "True"
})
fearless = skillA("GD_Assassin_Skills.Cunning.Fearless", {
    "SkillEffectDefinitions": [
        attr(
            AttributeToModify="ResourcePoolAttributeDefinition'D_Attributes.HealthResourcePool.HealthActiveRegenerationRate'",
            EffectTarget="TARGET_None",
            ModifierType="MT_Scale",
            BaseModifierValue=kValue(0.003),
            PerGradeUpgrade=kValue(0.003)),
        attr(
            AttributeToModify="ResourcePoolAttributeDefinition'D_Attributes.HealthResourcePool.HealthPassiveRegenerationRate'",
            EffectTarget="TARGET_Self",
            ModifierType="MT_PostAdd",
            BaseModifierValue=value(0, "ResourcePoolAttributeDefinition'D_Attributes.HealthResourcePool.HealthMaxValue'", None, 0.003),
            PerGradeUpgrade=value(0, "ResourcePoolAttributeDefinition'D_Attributes.HealthResourcePool.HealthMaxValue'", None, 0.003)),
        attr(
            AttributeToModify="AttributeDefinition'D_Attributes.Weapon.WeaponFireInterval'",
            EffectTarget="TARGET_Self",
            ModifierType="MT_Scale",
            BaseModifierValue=kValue(-0.05),
            PerGradeUpgrade=kValue(-0.05)),
        attr(
            AttributeToModify="AttributeDefinition'D_Attributes.Weapon.WeaponProjectilesPerShot'",
            EffectTarget="TARGET_None",
            ModifierType="MT_PreAdd",
            BaseModifierValue=value(0, "AttributeDefinition'D_Attributes.WeaponType.Weapon_Is_Sniper_Rifle'", None, 1)),
        attr(
            AttributeToModify="AttributeDefinition'D_Attributes.Weapon.WeaponProjectileSpeedMultiplier'",
            EffectTarget="TARGET_None",
            ModifierType="MT_PreAdd",
            BaseModifierValue=value(0, "AttributeDefinition'D_Attributes.WeaponType.Weapon_Is_Sniper_Rifle'", None, -0.8)),
    ]
})


##
mmfFeedback = skillA("GD_Assassin_Skills.Bloodshed.ManyMustFall_Feedback", {
    "SkillEffectDefinitions": [
        attr(
            AttributeToModify="AttributeDefinition'D_Attributes.Weapon.WeaponPerShotAccuracyImpulse'",
            EffectTarget="TARGET_None",
            ModifierType="MT_Scale",
            BaseModifierValue=kValue(1),
            PerGradeUpgrade=zeroValue),
        attr(
            AttributeToModify="DesignerAttributeDefinition'GD_Assassin_Skills.Misc.Att_CounterStrike_ActivationChance'",
            EffectTarget="TARGET_Self",
            ModifierType="MT_PostAdd",
            BaseModifierValue=kValue(-1),
            PerGradeUpgrade=zeroValue),
    ],
})

## execute
execute = skillA("GD_Assassin_Skills.ActionSkill.ActionSkill_Deception", {
    "bTargetRequiredForExecute": False,
    "bEnemyTargetRequiredForExecute": False,
    "bLockMovementAndRotation": False,
    "ExecuteVelocity": 9000,
    "AirSpeed": 12000,
    "ExecuteDuration": 50,
    "bEnableExecuteAimAssistance": False,
})

fastDeception = skillA("GD_Assassin_Skills.ActionSkill.ActionSkill_Deception:BehaviorProviderDefinition_0", {
    "BehaviorSequences[0].ConsolidatedOutputLinkData[5].ActivateDelay": "0.0"
})

fastDeception2 = skillA("GD_Assassin_Skills.ActionSkill.SpecialMove_SpawnHologram_1stPerson", {
    "PlayRate": "10",
})


### main
skills1 = [
    caMenu,
    caTimer,
    friendlyKunai,
    fastKunai,
    # slagKunai126,
    # slagKunai128,
    # slagKunai130,
    # swapFearlessGrim,
    # swapGrimFearless,
    cs,
    csActive,
    csActivationChance,
    csUI,
    # mmfFeedback,
    fearlessUI1,
    fearlessUI2,
    fearless,
    execute,
    fastDeception,
    fastDeception2,
]

def main(): 
    print "#<melee-zer0>"
    for skill in skills1:
        print '\n'.join(strSkill(skill))
    print "#</melee-zer0>"

main()

