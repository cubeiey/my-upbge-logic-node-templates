# MACHINE GENERATED
import bge
import mathutils
import bgelogic
import math

def _initialize(owner):
    network = bgelogic.LogicNetwork()
    CON0000 = bgelogic.ConditionMousePressed()
    CON0001 = bgelogic.ConditionMouseTargeting()
    ACT0002 = bgelogic.ActionSetObjectAttribute()
    CON0003 = bgelogic.ConditionAnd()
    PAR0004 = bgelogic.ParameterVector3Simple()
    PAR0005 = bgelogic.ParameterMouseData()
    PAR0006 = bgelogic.ParameterArithmeticOp()
    CON0000.mouse_button_code = bge.events.LEFTMOUSE
    CON0000.pulse = True
    CON0001.game_object = "NLO:U_O"
    ACT0002.condition = CON0003
    ACT0002.xyz = {'x': True, 'y': True, 'z': True}
    ACT0002.game_object = "NLO:U_O"
    ACT0002.attribute_value = PAR0004.OUTV
    ACT0002.value_type = 'worldScale'
    CON0003.condition_a = CON0001.MOUSE_OVER
    CON0003.condition_b = CON0000
    PAR0004.input_x = PAR0006
    PAR0004.input_y = PAR0006
    PAR0004.input_z = PAR0006
    PAR0006.operator = bgelogic.ParameterArithmeticOp.op_by_code("ADD")
    PAR0006.operand_a = PAR0005.MX
    PAR0006.operand_b = PAR0005.MX
    network.add_cell(CON0000)
    network.add_cell(PAR0005)
    network.add_cell(CON0001)
    network.add_cell(CON0003)
    network.add_cell(PAR0006)
    network.add_cell(PAR0004)
    network.add_cell(ACT0002)
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
