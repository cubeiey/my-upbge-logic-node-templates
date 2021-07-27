# MACHINE GENERATED
import bge
import mathutils
import bgelogic
import math

def _initialize(owner):
    network = bgelogic.LogicNetwork()
    ACT0000 = bgelogic.ActionSetObjectAttribute()
    PAR0001 = bgelogic.ParameterVector4Simple()
    CON0002 = bgelogic.ObjectPropertyOperator()
    ACT0003 = bgelogic.ActionSetObjectAttribute()
    CON0004 = bgelogic.ObjectPropertyOperator()
    PAR0005 = bgelogic.ParameterVector4Simple()
    CON0006 = bgelogic.ObjectPropertyOperator()
    ACT0007 = bgelogic.ActionSetObjectAttribute()
    PAR0008 = bgelogic.ParameterVector4Simple()
    PAR0009 = bgelogic.ParameterVector4Simple()
    CON0010 = bgelogic.ObjectPropertyOperator()
    ACT0011 = bgelogic.ActionSetObjectAttribute()
    PAR0012 = bgelogic.ParameterVector4Simple()
    ACT0013 = bgelogic.ActionSetObjectAttribute()
    CON0014 = bgelogic.ObjectPropertyOperator()
    PAR0015 = bgelogic.ParameterVector4Simple()
    CON0016 = bgelogic.ObjectPropertyOperator()
    ACT0017 = bgelogic.ActionSetObjectAttribute()
    ACT0018 = bgelogic.ActionRandomInt()
    ACT0019 = bgelogic.ActionSetGameObjectGameProperty()
    ACT0020 = bgelogic.ActionPlayAction()
    CON0021 = bgelogic.ConditionKeyPressed()
    ACT0000.condition = CON0002
    ACT0000.xyz = {'x': True, 'y': True, 'z': True}
    ACT0000.game_object = "NLO:U_O"
    ACT0000.attribute_value = PAR0001.OUTV
    ACT0000.value_type = 'worldOrientation'
    PAR0001.input_x = 0.0
    PAR0001.input_y = 90.0
    PAR0001.input_z = 0.0
    PAR0001.input_w = 1.0
    CON0002.game_object = "NLO:U_O"
    CON0002.property_name = "luck"
    CON0002.compare_value = 6
    CON0002.operator = 0
    ACT0003.condition = CON0004
    ACT0003.xyz = {'x': True, 'y': True, 'z': True}
    ACT0003.game_object = "NLO:U_O"
    ACT0003.attribute_value = PAR0005.OUTV
    ACT0003.value_type = 'worldOrientation'
    CON0004.game_object = "NLO:U_O"
    CON0004.property_name = "luck"
    CON0004.compare_value = 2
    CON0004.operator = 0
    PAR0005.input_x = 0.0
    PAR0005.input_y = 0.0
    PAR0005.input_z = 90.0
    PAR0005.input_w = 90.0
    CON0006.game_object = "NLO:U_O"
    CON0006.property_name = "luck"
    CON0006.compare_value = 4
    CON0006.operator = 0
    ACT0007.condition = CON0006
    ACT0007.xyz = {'x': True, 'y': True, 'z': True}
    ACT0007.game_object = "NLO:U_O"
    ACT0007.attribute_value = PAR0008.OUTV
    ACT0007.value_type = 'worldOrientation'
    PAR0008.input_x = 0.0
    PAR0008.input_y = 0.0
    PAR0008.input_z = -90.0
    PAR0008.input_w = 90.0
    PAR0009.input_x = 0.0
    PAR0009.input_y = 0.0
    PAR0009.input_z = 0.0
    PAR0009.input_w = 90.0
    CON0010.game_object = "NLO:U_O"
    CON0010.property_name = "luck"
    CON0010.compare_value = 1
    CON0010.operator = 0
    ACT0011.condition = CON0010
    ACT0011.xyz = {'x': True, 'y': True, 'z': True}
    ACT0011.game_object = "NLO:U_O"
    ACT0011.attribute_value = PAR0009.OUTV
    ACT0011.value_type = 'worldOrientation'
    PAR0012.input_x = 0.0
    PAR0012.input_y = -90.0
    PAR0012.input_z = 0.0
    PAR0012.input_w = 90.0
    ACT0013.condition = CON0014
    ACT0013.xyz = {'x': True, 'y': True, 'z': True}
    ACT0013.game_object = "NLO:U_O"
    ACT0013.attribute_value = PAR0012.OUTV
    ACT0013.value_type = 'worldOrientation'
    CON0014.game_object = "NLO:U_O"
    CON0014.property_name = "luck"
    CON0014.compare_value = 3
    CON0014.operator = 0
    PAR0015.input_x = 0.0
    PAR0015.input_y = 90.0
    PAR0015.input_z = 0.0
    PAR0015.input_w = 90.0
    CON0016.game_object = "NLO:U_O"
    CON0016.property_name = "luck"
    CON0016.compare_value = 5
    CON0016.operator = 0
    ACT0017.condition = CON0016
    ACT0017.xyz = {'x': True, 'y': True, 'z': True}
    ACT0017.game_object = "NLO:U_O"
    ACT0017.attribute_value = PAR0015.OUTV
    ACT0017.value_type = 'worldOrientation'
    ACT0018.max_value = 6
    ACT0018.min_value = 1
    ACT0019.condition = ACT0020.FINISHED
    ACT0019.game_object = "NLO:U_O"
    ACT0019.property_name = "luck"
    ACT0019.property_value = ACT0018.OUT_A
    ACT0020.condition = CON0021
    ACT0020.game_object = "NLO:Cube"
    ACT0020.action_name = "CubeAction"
    ACT0020.start_frame = 0.0
    ACT0020.end_frame = 20.0
    ACT0020.layer = 0
    ACT0020.priority = 0
    ACT0020.play_mode = bge.logic.KX_ACTION_MODE_PLAY
    ACT0020.stop = True
    ACT0020.layer_weight = 1.0
    ACT0020.speed = 2.0
    ACT0020.blendin = 0.0
    ACT0020.blend_mode = bge.logic.KX_ACTION_BLEND_ADD
    CON0021.key_code = bge.events.AKEY
    CON0021.pulse = False
    network.add_cell(PAR0001)
    network.add_cell(CON0004)
    network.add_cell(CON0006)
    network.add_cell(PAR0008)
    network.add_cell(CON0010)
    network.add_cell(PAR0012)
    network.add_cell(CON0014)
    network.add_cell(CON0016)
    network.add_cell(ACT0018)
    network.add_cell(CON0021)
    network.add_cell(CON0002)
    network.add_cell(PAR0005)
    network.add_cell(PAR0009)
    network.add_cell(ACT0013)
    network.add_cell(ACT0020)
    network.add_cell(ACT0000)
    network.add_cell(ACT0007)
    network.add_cell(PAR0015)
    network.add_cell(ACT0019)
    network.add_cell(ACT0003)
    network.add_cell(ACT0017)
    network.add_cell(ACT0011)
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
