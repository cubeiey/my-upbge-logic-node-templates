# MACHINE GENERATED
import bge
import mathutils
import bgelogic
import math

def _initialize(owner):
    network = bgelogic.LogicNetwork()
    CON0000 = bgelogic.ConditionMousePressed()
    CON0001 = bgelogic.ConditionMouseTargeting()
    PAR0002 = bgelogic.ParameterMouseData()
    ACT0003 = bgelogic.ActionSetObjectAttribute()
    PAR0004 = bgelogic.ParameterVector3Simple()
    CON0005 = bgelogic.ConditionOnUpdate()
    CON0006 = bgelogic.ConditionAndList()
    CON0000.mouse_button_code = bge.events.LEFTMOUSE
    CON0000.pulse = True
    CON0001.game_object = "NLO:U_O"
    ACT0003.condition = CON0006
    ACT0003.xyz = {'x': True, 'y': True, 'z': False}
    ACT0003.game_object = "NLO:U_O"
    ACT0003.attribute_value = PAR0004.OUTV
    ACT0003.value_type = 'worldScale'
    PAR0004.input_x = PAR0002.MX
    PAR0004.input_y = PAR0002.MY
    PAR0004.input_z = 0.0
    CON0006.ca = CON0001.MOUSE_OVER
    CON0006.cb = CON0000
    CON0006.cc = CON0005
    CON0006.cd = True
    CON0006.ce = True
    CON0006.cf = True
    network.add_cell(CON0000)
    network.add_cell(PAR0002)
    network.add_cell(PAR0004)
    network.add_cell(CON0001)
    network.add_cell(CON0005)
    network.add_cell(CON0006)
    network.add_cell(ACT0003)
    owner["IGNLTree_scale with cursor position"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NL__scale with cursor position')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("IGNLTree_scale with cursor position")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
