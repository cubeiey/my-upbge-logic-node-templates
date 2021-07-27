# MACHINE GENERATED
import bge
import mathutils
import bgelogic
import math

def _initialize(owner):
    network = bgelogic.LogicNetwork()
    CON0000 = bgelogic.ConditionMouseTargeting()
    ACT0001 = bgelogic.ActionApplyRotation()
    CON0000.game_object = "NLO:U_O"
    ACT0001.local = True
    ACT0001.condition = CON0000.MOUSE_OVER
    ACT0001.game_object = "NLO:U_O"
    ACT0001.rotation = mathutils.Vector((0.2617993950843811, 0.2617993950843811, 0.0))
    network.add_cell(CON0000)
    network.add_cell(ACT0001)
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
