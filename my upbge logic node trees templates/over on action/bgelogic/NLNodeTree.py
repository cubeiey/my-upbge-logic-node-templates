# MACHINE GENERATED
import bge
import mathutils
import bgelogic
import math

def _initialize(owner):
    network = bgelogic.LogicNetwork()
    CON0000 = bgelogic.ConditionMouseTargeting()
    PAR0001 = bgelogic.ParameterSwitchValue()
    ACT0002 = bgelogic.SetMaterial()
    ACT0003 = bgelogic.SetMaterial()
    ACT0004 = bgelogic.ActionPlayAction()
    CON0000.game_object = "NLO:U_O"
    PAR0001.state = CON0000.MOUSE_OVER
    ACT0002.condition = PAR0001.FALSE
    ACT0002.game_object = "NLO:U_O"
    ACT0002.slot = 1
    ACT0002.mat_name = "Material"
    ACT0003.condition = PAR0001.TRUE
    ACT0003.game_object = "NLO:U_O"
    ACT0003.slot = 1
    ACT0003.mat_name = "Material.001"
    ACT0004.condition = ACT0003.OUT
    ACT0004.game_object = "NLO:U_O"
    ACT0004.action_name = "Shader NodetreeAction"
    ACT0004.start_frame = 0.0
    ACT0004.end_frame = 40.0
    ACT0004.layer = 0
    ACT0004.priority = 0
    ACT0004.play_mode = bge.logic.KX_ACTION_MODE_LOOP
    ACT0004.stop = False
    ACT0004.layer_weight = 1.0
    ACT0004.speed = 1.0
    ACT0004.blendin = 0.0
    ACT0004.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    network.add_cell(CON0000)
    network.add_cell(PAR0001)
    network.add_cell(ACT0003)
    network.add_cell(ACT0002)
    network.add_cell(ACT0004)
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
