# MACHINE GENERATED
import bge
import mathutils
import bgelogic
import math

def _initialize(owner):
    network = bgelogic.LogicNetwork()
    CON0000 = bgelogic.ObjectPropertyOperator()
    CON0001 = bgelogic.ObjectPropertyOperator()
    CON0002 = bgelogic.ObjectPropertyOperator()
    CON0003 = bgelogic.ConditionOrList()
    CON0004 = bgelogic.ConditionAnd()
    CON0005 = bgelogic.ObjectPropertyOperator()
    CON0006 = bgelogic.ConditionAnd()
    CON0007 = bgelogic.ObjectPropertyOperator()
    CON0008 = bgelogic.ObjectPropertyOperator()
    CON0009 = bgelogic.ObjectPropertyOperator()
    CON0010 = bgelogic.ObjectPropertyOperator()
    CON0011 = bgelogic.ObjectPropertyOperator()
    CON0012 = bgelogic.ConditionOrList()
    CON0013 = bgelogic.ConditionAnd()
    ACT0014 = bgelogic.SetMaterial()
    ACT0015 = bgelogic.SetMaterial()
    CON0016 = bgelogic.ObjectPropertyOperator()
    CON0017 = bgelogic.ObjectPropertyOperator()
    CON0018 = bgelogic.ObjectPropertyOperator()
    CON0019 = bgelogic.ObjectPropertyOperator()
    CON0020 = bgelogic.ObjectPropertyOperator()
    CON0021 = bgelogic.ObjectPropertyOperator()
    CON0022 = bgelogic.ConditionOrList()
    CON0023 = bgelogic.ConditionAnd()
    CON0024 = bgelogic.ObjectPropertyOperator()
    CON0025 = bgelogic.ObjectPropertyOperator()
    ACT0026 = bgelogic.SetMaterial()
    ACT0027 = bgelogic.SetMaterial()
    ACT0028 = bgelogic.SetMaterial()
    ACT0029 = bgelogic.SetMaterial()
    ACT0030 = bgelogic.ActionSetGameObjectGameProperty()
    CON0031 = bgelogic.ConditionOrList()
    CON0032 = bgelogic.ObjectPropertyOperator()
    CON0033 = bgelogic.ObjectPropertyOperator()
    CON0034 = bgelogic.ObjectPropertyOperator()
    CON0035 = bgelogic.ConditionAnd()
    ACT0036 = bgelogic.SetMaterial()
    ACT0037 = bgelogic.SetMaterial()
    ACT0038 = bgelogic.SetMaterial()
    ACT0039 = bgelogic.SetMaterial()
    ACT0040 = bgelogic.ActionSetGameObjectGameProperty()
    ACT0041 = bgelogic.ActionSetGameObjectGameProperty()
    ACT0042 = bgelogic.ActionSetGameObjectGameProperty()
    ACT0043 = bgelogic.ActionSetGameObjectGameProperty()
    ACT0044 = bgelogic.ActionPlayAction()
    ACT0045 = bgelogic.ActionPlayAction()
    ACT0046 = bgelogic.ActionPlayAction()
    ACT0047 = bgelogic.ActionPlayAction()
    ACT0048 = bgelogic.ActionPlayAction()
    CON0049 = bgelogic.ConditionMousePressed()
    ACT0050 = bgelogic.ActionSetGameObjectGameProperty()
    ACT0051 = bgelogic.ActionSetGameObjectGameProperty()
    CON0052 = bgelogic.ConditionNot()
    CON0053 = bgelogic.ConditionNot()
    CON0054 = bgelogic.ConditionNot()
    CON0055 = bgelogic.ConditionNot()
    CON0056 = bgelogic.ConditionAndList()
    CON0057 = bgelogic.ConditionAndList()
    CON0058 = bgelogic.ConditionNot()
    ACT0059 = bgelogic.ActionRandomInt()
    CON0060 = bgelogic.ConditionAnd()
    CON0061 = bgelogic.ConditionNot()
    ACT0062 = bgelogic.ActionPlayAction()
    ACT0063 = bgelogic.ActionPlayAction()
    CON0064 = bgelogic.ConditionNot()
    ACT0065 = bgelogic.ActionPlayAction()
    ACT0066 = bgelogic.ActionPlayAction()
    CON0067 = bgelogic.ConditionNot()
    CON0068 = bgelogic.ConditionNot()
    CON0069 = bgelogic.ConditionNot()
    ACT0070 = bgelogic.ActionPlayAction()
    CON0000.game_object = "NLO:Cube"
    CON0000.property_name = "mat"
    CON0000.compare_value = 3
    CON0000.operator = 0
    CON0001.game_object = "NLO:Cube"
    CON0001.property_name = "mat"
    CON0001.compare_value = 6
    CON0001.operator = 0
    CON0002.game_object = "NLO:Cube"
    CON0002.property_name = "mat"
    CON0002.compare_value = 9
    CON0002.operator = 0
    CON0003.ca = CON0000
    CON0003.cb = CON0001
    CON0003.cc = CON0002
    CON0003.cd = None
    CON0003.ce = None
    CON0003.cf = None
    CON0004.condition_a = CON0003
    CON0004.condition_b = CON0016
    CON0005.game_object = "NLO:Cube"
    CON0005.property_name = "mat"
    CON0005.compare_value = 15
    CON0005.operator = 0
    CON0006.condition_a = CON0005
    CON0006.condition_b = CON0017
    CON0007.game_object = "NLO:Cube"
    CON0007.property_name = "mat"
    CON0007.compare_value = 4
    CON0007.operator = 0
    CON0008.game_object = "NLO:Cube"
    CON0008.property_name = "mat"
    CON0008.compare_value = 1
    CON0008.operator = 0
    CON0009.game_object = "NLO:Cube"
    CON0009.property_name = "mat"
    CON0009.compare_value = 7
    CON0009.operator = 0
    CON0010.game_object = "NLO:Cube"
    CON0010.property_name = "mat"
    CON0010.compare_value = 10
    CON0010.operator = 0
    CON0011.game_object = "NLO:Cube"
    CON0011.property_name = "mat"
    CON0011.compare_value = 13
    CON0011.operator = 0
    CON0012.ca = CON0008
    CON0012.cb = CON0007
    CON0012.cc = CON0009
    CON0012.cd = CON0010
    CON0012.ce = CON0011
    CON0012.cf = None
    CON0013.condition_a = CON0012
    CON0013.condition_b = CON0025
    ACT0014.condition = CON0013
    ACT0014.game_object = "NLO:Sphere"
    ACT0014.slot = 1
    ACT0014.mat_name = "plastic"
    ACT0015.condition = CON0013
    ACT0015.game_object = "NLO:Cube"
    ACT0015.slot = 1
    ACT0015.mat_name = "normal"
    CON0016.game_object = "NLO:Cube"
    CON0016.property_name = "click agin"
    CON0016.compare_value = True
    CON0016.operator = 0
    CON0017.game_object = "NLO:Cube"
    CON0017.property_name = "click agin"
    CON0017.compare_value = True
    CON0017.operator = 0
    CON0018.game_object = "NLO:Cube"
    CON0018.property_name = "mat"
    CON0018.compare_value = 2
    CON0018.operator = 0
    CON0019.game_object = "NLO:Cube"
    CON0019.property_name = "mat"
    CON0019.compare_value = 5
    CON0019.operator = 0
    CON0020.game_object = "NLO:Cube"
    CON0020.property_name = "mat"
    CON0020.compare_value = 8
    CON0020.operator = 0
    CON0021.game_object = "NLO:Cube"
    CON0021.property_name = "mat"
    CON0021.compare_value = 11
    CON0021.operator = 0
    CON0022.ca = CON0018
    CON0022.cb = CON0019
    CON0022.cc = CON0020
    CON0022.cd = CON0021
    CON0022.ce = None
    CON0022.cf = None
    CON0023.condition_a = CON0022
    CON0023.condition_b = CON0024
    CON0024.game_object = "NLO:Cube"
    CON0024.property_name = "click agin"
    CON0024.compare_value = True
    CON0024.operator = 0
    CON0025.game_object = "NLO:Cube"
    CON0025.property_name = "click agin"
    CON0025.compare_value = True
    CON0025.operator = 0
    ACT0026.condition = CON0023
    ACT0026.game_object = "NLO:Cube"
    ACT0026.slot = 1
    ACT0026.mat_name = "common"
    ACT0027.condition = CON0023
    ACT0027.game_object = "NLO:Sphere"
    ACT0027.slot = 1
    ACT0027.mat_name = "copper"
    ACT0028.condition = CON0006
    ACT0028.game_object = "NLO:Cube"
    ACT0028.slot = 1
    ACT0028.mat_name = "ultra rare"
    ACT0029.condition = CON0006
    ACT0029.game_object = "NLO:Sphere"
    ACT0029.slot = 1
    ACT0029.mat_name = "gem"
    ACT0030.condition = ACT0048.STARTED
    ACT0030.game_object = "NLO:Cube"
    ACT0030.property_name = "click agin"
    ACT0030.property_value = False
    CON0031.ca = CON0033
    CON0031.cb = CON0032
    CON0031.cc = None
    CON0031.cd = None
    CON0031.ce = None
    CON0031.cf = None
    CON0032.game_object = "NLO:Cube"
    CON0032.property_name = "mat"
    CON0032.compare_value = 14
    CON0032.operator = 0
    CON0033.game_object = "NLO:Cube"
    CON0033.property_name = "mat"
    CON0033.compare_value = 12
    CON0033.operator = 0
    CON0034.game_object = "NLO:Cube"
    CON0034.property_name = "click agin"
    CON0034.compare_value = True
    CON0034.operator = 0
    CON0035.condition_a = CON0031
    CON0035.condition_b = CON0034
    ACT0036.condition = CON0035
    ACT0036.game_object = "NLO:Sphere"
    ACT0036.slot = 1
    ACT0036.mat_name = "gold"
    ACT0037.condition = CON0035
    ACT0037.game_object = "NLO:Cube"
    ACT0037.slot = 1
    ACT0037.mat_name = "super rare"
    ACT0038.condition = CON0004
    ACT0038.game_object = "NLO:Cube"
    ACT0038.slot = 1
    ACT0038.mat_name = "rare"
    ACT0039.condition = CON0004
    ACT0039.game_object = "NLO:Sphere"
    ACT0039.slot = 1
    ACT0039.mat_name = "silver"
    ACT0040.condition = ACT0045.STARTED
    ACT0040.game_object = "NLO:Cube"
    ACT0040.property_name = "click agin"
    ACT0040.property_value = False
    ACT0041.condition = ACT0046.STARTED
    ACT0041.game_object = "NLO:Cube"
    ACT0041.property_name = "click agin"
    ACT0041.property_value = False
    ACT0042.condition = ACT0047.STARTED
    ACT0042.game_object = "NLO:Cube"
    ACT0042.property_name = "click agin"
    ACT0042.property_value = False
    ACT0043.condition = ACT0044.STARTED
    ACT0043.game_object = "NLO:Cube"
    ACT0043.property_name = "click agin"
    ACT0043.property_value = False
    ACT0044.condition = CON0035
    ACT0044.game_object = "NLO:Cube"
    ACT0044.action_name = "Shader NodetreeAction.003"
    ACT0044.start_frame = 0.0
    ACT0044.end_frame = 140.0
    ACT0044.layer = 0
    ACT0044.priority = 0
    ACT0044.play_mode = bge.logic.KX_ACTION_MODE_PLAY
    ACT0044.stop = True
    ACT0044.layer_weight = 1.0
    ACT0044.speed = 1.0
    ACT0044.blendin = 0.0
    ACT0044.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    ACT0045.condition = CON0004
    ACT0045.game_object = "NLO:Cube"
    ACT0045.action_name = "Shader NodetreeAction.002"
    ACT0045.start_frame = 0.0
    ACT0045.end_frame = 140.0
    ACT0045.layer = 0
    ACT0045.priority = 0
    ACT0045.play_mode = bge.logic.KX_ACTION_MODE_PLAY
    ACT0045.stop = True
    ACT0045.layer_weight = 1.0
    ACT0045.speed = 1.0
    ACT0045.blendin = 0.0
    ACT0045.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    ACT0046.condition = CON0013
    ACT0046.game_object = "NLO:Cube"
    ACT0046.action_name = "Shader NodetreeAction"
    ACT0046.start_frame = 0.0
    ACT0046.end_frame = 140.0
    ACT0046.layer = 0
    ACT0046.priority = 0
    ACT0046.play_mode = bge.logic.KX_ACTION_MODE_PLAY
    ACT0046.stop = True
    ACT0046.layer_weight = 1.0
    ACT0046.speed = 1.0
    ACT0046.blendin = 0.0
    ACT0046.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    ACT0047.condition = CON0023
    ACT0047.game_object = "NLO:Cube"
    ACT0047.action_name = "Shader NodetreeAction.001"
    ACT0047.start_frame = 0.0
    ACT0047.end_frame = 140.0
    ACT0047.layer = 0
    ACT0047.priority = 0
    ACT0047.play_mode = bge.logic.KX_ACTION_MODE_PLAY
    ACT0047.stop = True
    ACT0047.layer_weight = 1.0
    ACT0047.speed = 1.0
    ACT0047.blendin = 0.0
    ACT0047.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    ACT0048.condition = CON0006
    ACT0048.game_object = "NLO:Cube"
    ACT0048.action_name = "Shader NodetreeAction.004"
    ACT0048.start_frame = 0.0
    ACT0048.end_frame = 140.0
    ACT0048.layer = 0
    ACT0048.priority = 0
    ACT0048.play_mode = bge.logic.KX_ACTION_MODE_PLAY
    ACT0048.stop = True
    ACT0048.layer_weight = 1.0
    ACT0048.speed = 1.0
    ACT0048.blendin = 0.0
    ACT0048.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    CON0049.mouse_button_code = bge.events.LEFTMOUSE
    CON0049.pulse = False
    ACT0050.condition = ACT0051.OUT
    ACT0050.game_object = "NLO:Cube"
    ACT0050.property_name = "click agin"
    ACT0050.property_value = True
    ACT0051.condition = CON0060
    ACT0051.game_object = "NLO:Cube"
    ACT0051.property_name = "mat"
    ACT0051.property_value = ACT0059.OUT_A
    CON0052.condition = ACT0063.STARTED
    CON0053.condition = ACT0062.STARTED
    CON0054.condition = ACT0065.STARTED
    CON0055.condition = ACT0065.RUNNING
    CON0056.ca = CON0049
    CON0056.cb = CON0052
    CON0056.cc = CON0061
    CON0056.cd = CON0053
    CON0056.ce = CON0064
    CON0056.cf = CON0054
    CON0057.ca = CON0055
    CON0057.cb = CON0058
    CON0057.cc = CON0067
    CON0057.cd = CON0068
    CON0057.ce = CON0069
    CON0057.cf = True
    CON0058.condition = ACT0066.STARTED
    ACT0059.max_value = 15
    ACT0059.min_value = 1
    CON0060.condition_a = CON0056
    CON0060.condition_b = CON0057
    CON0061.condition = ACT0063.RUNNING
    ACT0062.condition = None
    ACT0062.game_object = "NLO:Cube"
    ACT0062.action_name = "Shader NodetreeAction.002"
    ACT0062.start_frame = 0.0
    ACT0062.end_frame = 140.0
    ACT0062.layer = 0
    ACT0062.priority = 0
    ACT0062.play_mode = bge.logic.KX_ACTION_MODE_PLAY
    ACT0062.stop = True
    ACT0062.layer_weight = 1.0
    ACT0062.speed = 1.0
    ACT0062.blendin = 0.0
    ACT0062.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    ACT0063.condition = None
    ACT0063.game_object = "NLO:Cube"
    ACT0063.action_name = "Shader NodetreeAction.003"
    ACT0063.start_frame = 0.0
    ACT0063.end_frame = 140.0
    ACT0063.layer = 0
    ACT0063.priority = 0
    ACT0063.play_mode = bge.logic.KX_ACTION_MODE_PLAY
    ACT0063.stop = True
    ACT0063.layer_weight = 1.0
    ACT0063.speed = 1.0
    ACT0063.blendin = 0.0
    ACT0063.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    CON0064.condition = ACT0062.RUNNING
    ACT0065.condition = None
    ACT0065.game_object = "NLO:Cube"
    ACT0065.action_name = "Shader NodetreeAction.004"
    ACT0065.start_frame = 0.0
    ACT0065.end_frame = 140.0
    ACT0065.layer = 0
    ACT0065.priority = 0
    ACT0065.play_mode = bge.logic.KX_ACTION_MODE_PLAY
    ACT0065.stop = True
    ACT0065.layer_weight = 1.0
    ACT0065.speed = 1.0
    ACT0065.blendin = 0.0
    ACT0065.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    ACT0066.condition = None
    ACT0066.game_object = "NLO:Cube"
    ACT0066.action_name = "Shader NodetreeAction.001"
    ACT0066.start_frame = 0.0
    ACT0066.end_frame = 140.0
    ACT0066.layer = 0
    ACT0066.priority = 0
    ACT0066.play_mode = bge.logic.KX_ACTION_MODE_PLAY
    ACT0066.stop = True
    ACT0066.layer_weight = 1.0
    ACT0066.speed = 1.0
    ACT0066.blendin = 0.0
    ACT0066.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    CON0067.condition = ACT0066.RUNNING
    CON0068.condition = ACT0070.STARTED
    CON0069.condition = ACT0070.RUNNING
    ACT0070.condition = None
    ACT0070.game_object = "NLO:Cube"
    ACT0070.action_name = "Shader NodetreeAction"
    ACT0070.start_frame = 0.0
    ACT0070.end_frame = 140.0
    ACT0070.layer = 0
    ACT0070.priority = 0
    ACT0070.play_mode = bge.logic.KX_ACTION_MODE_PLAY
    ACT0070.stop = True
    ACT0070.layer_weight = 1.0
    ACT0070.speed = 1.0
    ACT0070.blendin = 0.0
    ACT0070.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    network.add_cell(CON0000)
    network.add_cell(CON0002)
    network.add_cell(CON0005)
    network.add_cell(CON0007)
    network.add_cell(CON0009)
    network.add_cell(CON0011)
    network.add_cell(CON0016)
    network.add_cell(CON0018)
    network.add_cell(CON0020)
    network.add_cell(CON0024)
    network.add_cell(CON0032)
    network.add_cell(CON0034)
    network.add_cell(CON0049)
    network.add_cell(ACT0059)
    network.add_cell(ACT0062)
    network.add_cell(CON0064)
    network.add_cell(ACT0066)
    network.add_cell(ACT0070)
    network.add_cell(CON0001)
    network.add_cell(CON0008)
    network.add_cell(CON0017)
    network.add_cell(CON0021)
    network.add_cell(CON0025)
    network.add_cell(CON0033)
    network.add_cell(CON0053)
    network.add_cell(CON0058)
    network.add_cell(ACT0063)
    network.add_cell(CON0067)
    network.add_cell(CON0069)
    network.add_cell(CON0003)
    network.add_cell(CON0006)
    network.add_cell(CON0019)
    network.add_cell(ACT0028)
    network.add_cell(CON0031)
    network.add_cell(ACT0048)
    network.add_cell(CON0052)
    network.add_cell(CON0061)
    network.add_cell(CON0068)
    network.add_cell(CON0004)
    network.add_cell(CON0022)
    network.add_cell(ACT0029)
    network.add_cell(CON0035)
    network.add_cell(ACT0037)
    network.add_cell(ACT0039)
    network.add_cell(ACT0044)
    network.add_cell(ACT0065)
    network.add_cell(CON0010)
    network.add_cell(CON0023)
    network.add_cell(ACT0027)
    network.add_cell(ACT0036)
    network.add_cell(ACT0043)
    network.add_cell(ACT0047)
    network.add_cell(CON0054)
    network.add_cell(CON0056)
    network.add_cell(CON0012)
    network.add_cell(ACT0026)
    network.add_cell(ACT0038)
    network.add_cell(ACT0042)
    network.add_cell(CON0055)
    network.add_cell(CON0013)
    network.add_cell(ACT0015)
    network.add_cell(ACT0045)
    network.add_cell(CON0057)
    network.add_cell(ACT0014)
    network.add_cell(ACT0040)
    network.add_cell(ACT0046)
    network.add_cell(CON0060)
    network.add_cell(ACT0030)
    network.add_cell(ACT0051)
    network.add_cell(ACT0041)
    network.add_cell(ACT0050)
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
