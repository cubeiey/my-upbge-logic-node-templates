# MACHINE GENERATED
import bge
import mathutils
import bgelogic
import math

def _initialize(owner):
    network = bgelogic.LogicNetwork()
    PAR0000 = bgelogic.ParameterSwitchValue()
    CON0001 = bgelogic.ConditionKeyPressed()
    ACT0002 = bgelogic.ActionSetObjectAttribute()
    ACT0003 = bgelogic.ActionSetObjectAttribute()
    ACT0004 = bgelogic.ActionSetObjectAttribute()
    ACT0005 = bgelogic.SetMaterial()
    ACT0006 = bgelogic.ActionSetObjectAttribute()
    CON0007 = bgelogic.ConditionKeyPressed()
    PAR0008 = bgelogic.ParameterSwitchValue()
    PAR0009 = bgelogic.ParameterSwitchValue()
    CON0010 = bgelogic.ConditionKeyPressed()
    ACT0011 = bgelogic.ActionSetObjectAttribute()
    ACT0012 = bgelogic.SetMaterial()
    ACT0013 = bgelogic.ActionSetObjectAttribute()
    CON0014 = bgelogic.ConditionKeyPressed()
    ACT0015 = bgelogic.ActionSetObjectAttribute()
    ACT0016 = bgelogic.SetMaterial()
    ACT0017 = bgelogic.ActionSetObjectAttribute()
    PAR0018 = bgelogic.ParameterSwitchValue()
    ACT0019 = bgelogic.SetMaterial()
    ACT0020 = bgelogic.SetMaterial()
    ACT0021 = bgelogic.SetMaterial()
    ACT0022 = bgelogic.SetMaterial()
    ACT0023 = bgelogic.SetMaterial()
    PAR0000.state = CON0001
    CON0001.key_code = bge.events.LEFTARROWKEY
    CON0001.pulse = True
    ACT0002.condition = PAR0000.TRUE
    ACT0002.xyz = {'x': True, 'y': True, 'z': True}
    ACT0002.game_object = "NLO:Plane.001"
    ACT0002.attribute_value = mathutils.Vector((1.5, 1.5, 1.5))
    ACT0002.value_type = 'worldScale'
    ACT0003.condition = PAR0000.FALSE
    ACT0003.xyz = {'x': True, 'y': True, 'z': True}
    ACT0003.game_object = "NLO:Plane.001"
    ACT0003.attribute_value = mathutils.Vector((0.5944669842720032, 0.5944669842720032, 0.5944669842720032))
    ACT0003.value_type = 'worldScale'
    ACT0004.condition = PAR0008.FALSE
    ACT0004.xyz = {'x': True, 'y': True, 'z': True}
    ACT0004.game_object = "NLO:Plane.003"
    ACT0004.attribute_value = mathutils.Vector((0.5944669842720032, 0.5944669842720032, 0.5944669842720032))
    ACT0004.value_type = 'worldScale'
    ACT0005.condition = PAR0008.TRUE
    ACT0005.game_object = "NLO:Plane.003"
    ACT0005.slot = 1
    ACT0005.mat_name = "glow"
    ACT0006.condition = PAR0008.TRUE
    ACT0006.xyz = {'x': True, 'y': True, 'z': True}
    ACT0006.game_object = "NLO:Plane.003"
    ACT0006.attribute_value = mathutils.Vector((1.5, 1.5, 1.5))
    ACT0006.value_type = 'worldScale'
    CON0007.key_code = bge.events.DOWNARROWKEY
    CON0007.pulse = True
    PAR0008.state = CON0007
    PAR0009.state = CON0010
    CON0010.key_code = bge.events.UPARROWKEY
    CON0010.pulse = True
    ACT0011.condition = PAR0009.TRUE
    ACT0011.xyz = {'x': True, 'y': True, 'z': True}
    ACT0011.game_object = "NLO:Plane.002"
    ACT0011.attribute_value = mathutils.Vector((1.5, 1.5, 1.5))
    ACT0011.value_type = 'worldScale'
    ACT0012.condition = PAR0009.TRUE
    ACT0012.game_object = "NLO:Plane.002"
    ACT0012.slot = 1
    ACT0012.mat_name = "glow"
    ACT0013.condition = PAR0009.FALSE
    ACT0013.xyz = {'x': True, 'y': True, 'z': True}
    ACT0013.game_object = "NLO:Plane.002"
    ACT0013.attribute_value = mathutils.Vector((0.5944669842720032, 0.5944669842720032, 0.5944669842720032))
    ACT0013.value_type = 'worldScale'
    CON0014.key_code = bge.events.RIGHTARROWKEY
    CON0014.pulse = True
    ACT0015.condition = PAR0018.FALSE
    ACT0015.xyz = {'x': True, 'y': True, 'z': True}
    ACT0015.game_object = "NLO:Plane"
    ACT0015.attribute_value = mathutils.Vector((0.5944669842720032, 0.5944669842720032, 0.5944669842720032))
    ACT0015.value_type = 'worldScale'
    ACT0016.condition = PAR0018.TRUE
    ACT0016.game_object = "NLO:Plane"
    ACT0016.slot = 1
    ACT0016.mat_name = "glow"
    ACT0017.condition = PAR0018.TRUE
    ACT0017.xyz = {'x': True, 'y': True, 'z': True}
    ACT0017.game_object = "NLO:Plane"
    ACT0017.attribute_value = mathutils.Vector((1.5, 1.5, 1.5))
    ACT0017.value_type = 'worldScale'
    PAR0018.state = CON0014
    ACT0019.condition = PAR0000.TRUE
    ACT0019.game_object = "NLO:Plane.001"
    ACT0019.slot = 1
    ACT0019.mat_name = "glow"
    ACT0020.condition = PAR0000.FALSE
    ACT0020.game_object = "NLO:Plane.001"
    ACT0020.slot = 1
    ACT0020.mat_name = "Material"
    ACT0021.condition = PAR0008.FALSE
    ACT0021.game_object = "NLO:Plane.003"
    ACT0021.slot = 1
    ACT0021.mat_name = "Material"
    ACT0022.condition = PAR0018.FALSE
    ACT0022.game_object = "NLO:Plane"
    ACT0022.slot = 1
    ACT0022.mat_name = "Material"
    ACT0023.condition = PAR0009.FALSE
    ACT0023.game_object = "NLO:Plane.002"
    ACT0023.slot = 1
    ACT0023.mat_name = "Material"
    network.add_cell(CON0001)
    network.add_cell(CON0007)
    network.add_cell(CON0010)
    network.add_cell(CON0014)
    network.add_cell(PAR0018)
    network.add_cell(ACT0022)
    network.add_cell(PAR0000)
    network.add_cell(ACT0003)
    network.add_cell(PAR0008)
    network.add_cell(ACT0015)
    network.add_cell(ACT0017)
    network.add_cell(ACT0020)
    network.add_cell(ACT0002)
    network.add_cell(ACT0005)
    network.add_cell(PAR0009)
    network.add_cell(ACT0012)
    network.add_cell(ACT0016)
    network.add_cell(ACT0021)
    network.add_cell(ACT0004)
    network.add_cell(ACT0011)
    network.add_cell(ACT0019)
    network.add_cell(ACT0006)
    network.add_cell(ACT0023)
    network.add_cell(ACT0013)
    owner["IGNLTree_NodeTree"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NL__NodeTree')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("IGNLTree_NodeTree")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
