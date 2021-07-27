# MACHINE GENERATED
import bge
import mathutils
import bgelogic
import math

def _initialize(owner):
    network = bgelogic.LogicNetwork()
    CON0000 = bgelogic.ConditionKeyPressed()
    CON0001 = bgelogic.ConditionKeyPressed()
    ACT0002 = bgelogic.ActionSetGameObjectGameProperty()
    ACT0003 = bgelogic.ActionSetGameObjectGameProperty()
    CON0004 = bgelogic.ObjectPropertyOperator()
    CON0005 = bgelogic.ObjectPropertyOperator()
    CON0006 = bgelogic.ConditionAndList()
    ACT0007 = bgelogic.ActionSetGameObjectGameProperty()
    CON0008 = bgelogic.ObjectPropertyOperator()
    ACT0009 = bgelogic.ActionSetGameObjectGameProperty()
    CON0010 = bgelogic.ObjectPropertyOperator()
    CON0011 = bgelogic.ConditionAndList()
    ACT0012 = bgelogic.ActionSetGameObjectGameProperty()
    ACT0013 = bgelogic.ActionSetGameObjectGameProperty()
    CON0014 = bgelogic.ObjectPropertyOperator()
    CON0015 = bgelogic.ObjectPropertyOperator()
    ACT0016 = bgelogic.ActionSetGameObjectGameProperty()
    ACT0017 = bgelogic.ActionSetGameObjectGameProperty()
    CON0018 = bgelogic.ObjectPropertyOperator()
    CON0019 = bgelogic.ConditionAndList()
    CON0020 = bgelogic.ConditionAndList()
    CON0021 = bgelogic.ObjectPropertyOperator()
    ACT0022 = bgelogic.ActionSetGameObjectGameProperty()
    ACT0023 = bgelogic.ActionSetGameObjectGameProperty()
    CON0024 = bgelogic.ObjectPropertyOperator()
    CON0025 = bgelogic.ObjectPropertyOperator()
    CON0026 = bgelogic.ConditionAndList()
    ACT0027 = bgelogic.ActionSetGameObjectGameProperty()
    ACT0028 = bgelogic.ActionSetGameObjectGameProperty()
    CON0029 = bgelogic.ObjectPropertyOperator()
    CON0030 = bgelogic.ConditionAndList()
    CON0031 = bgelogic.ObjectPropertyOperator()
    CON0032 = bgelogic.ObjectPropertyOperator()
    CON0033 = bgelogic.ConditionAndList()
    CON0034 = bgelogic.ObjectPropertyOperator()
    ACT0035 = bgelogic.ActionSetGameObjectGameProperty()
    ACT0036 = bgelogic.ActionSetGameObjectGameProperty()
    CON0037 = bgelogic.ObjectPropertyOperator()
    CON0038 = bgelogic.ObjectPropertyOperator()
    CON0039 = bgelogic.ConditionAndList()
    ACT0040 = bgelogic.ActionSetGameObjectGameProperty()
    ACT0041 = bgelogic.ActionSetGameObjectGameProperty()
    CON0042 = bgelogic.ObjectPropertyOperator()
    ACT0043 = bgelogic.ActionSetGameObjectVisibility()
    ACT0044 = bgelogic.ActionSetObjectAttribute()
    ACT0045 = bgelogic.ActionSetGameObjectVisibility()
    CON0046 = bgelogic.ObjectPropertyOperator()
    ACT0047 = bgelogic.ActionSetObjectAttribute()
    CON0048 = bgelogic.ObjectPropertyOperator()
    CON0049 = bgelogic.ObjectPropertyOperator()
    ACT0050 = bgelogic.ActionSetObjectAttribute()
    ACT0051 = bgelogic.ActionSetGameObjectVisibility()
    CON0052 = bgelogic.ObjectPropertyOperator()
    ACT0053 = bgelogic.ActionSetObjectAttribute()
    ACT0054 = bgelogic.ActionSetGameObjectVisibility()
    CON0055 = bgelogic.ObjectPropertyOperator()
    ACT0056 = bgelogic.ActionSetObjectAttribute()
    CON0057 = bgelogic.ObjectPropertyOperator()
    ACT0058 = bgelogic.ActionSetGameObjectVisibility()
    CON0059 = bgelogic.ObjectPropertyOperator()
    ACT0060 = bgelogic.ActionSetObjectAttribute()
    ACT0061 = bgelogic.ActionSetGameObjectVisibility()
    ACT0062 = bgelogic.ActionSetObjectAttribute()
    ACT0063 = bgelogic.ActionSetObjectAttribute()
    CON0064 = bgelogic.ConditionKeyPressed()
    CON0065 = bgelogic.ObjectPropertyOperator()
    CON0066 = bgelogic.ObjectPropertyOperator()
    CON0067 = bgelogic.ConditionAndList()
    ACT0068 = bgelogic.ActionSetGameObjectGameProperty()
    CON0000.key_code = bge.events.RIGHTARROWKEY
    CON0000.pulse = False
    CON0001.key_code = bge.events.LEFTARROWKEY
    CON0001.pulse = False
    ACT0002.condition = CON0006
    ACT0002.game_object = "NLO:Plane"
    ACT0002.property_name = "3"
    ACT0002.property_value = False
    ACT0003.condition = CON0006
    ACT0003.game_object = "NLO:Plane.001"
    ACT0003.property_name = "4"
    ACT0003.property_value = True
    CON0004.game_object = "NLO:Plane"
    CON0004.property_name = "3"
    CON0004.compare_value = True
    CON0004.operator = 0
    CON0005.game_object = "NLO:Cube"
    CON0005.property_name = "change mat"
    CON0005.compare_value = False
    CON0005.operator = 0
    CON0006.ca = CON0000
    CON0006.cb = CON0004
    CON0006.cc = CON0005
    CON0006.cd = True
    CON0006.ce = True
    CON0006.cf = True
    ACT0007.condition = CON0011
    ACT0007.game_object = "NLO:Plane.001"
    ACT0007.property_name = "4"
    ACT0007.property_value = False
    CON0008.game_object = "NLO:Plane.001"
    CON0008.property_name = "4"
    CON0008.compare_value = True
    CON0008.operator = 0
    ACT0009.condition = CON0011
    ACT0009.game_object = "NLO:Plane.002"
    ACT0009.property_name = "1"
    ACT0009.property_value = True
    CON0010.game_object = "NLO:Cube"
    CON0010.property_name = "change mat"
    CON0010.compare_value = False
    CON0010.operator = 0
    CON0011.ca = CON0000
    CON0011.cb = CON0008
    CON0011.cc = CON0010
    CON0011.cd = True
    CON0011.ce = True
    CON0011.cf = True
    ACT0012.condition = CON0019
    ACT0012.game_object = "NLO:Plane.003"
    ACT0012.property_name = "2"
    ACT0012.property_value = False
    ACT0013.condition = CON0019
    ACT0013.game_object = "NLO:Plane"
    ACT0013.property_name = "3"
    ACT0013.property_value = True
    CON0014.game_object = "NLO:Plane.003"
    CON0014.property_name = "2"
    CON0014.compare_value = True
    CON0014.operator = 0
    CON0015.game_object = "NLO:Cube"
    CON0015.property_name = "change mat"
    CON0015.compare_value = False
    CON0015.operator = 0
    ACT0016.condition = CON0020
    ACT0016.game_object = "NLO:Plane.002"
    ACT0016.property_name = "1"
    ACT0016.property_value = False
    ACT0017.condition = CON0020
    ACT0017.game_object = "NLO:Plane.003"
    ACT0017.property_name = "2"
    ACT0017.property_value = True
    CON0018.game_object = "NLO:Plane.002"
    CON0018.property_name = "1"
    CON0018.compare_value = True
    CON0018.operator = 0
    CON0019.ca = CON0000
    CON0019.cb = CON0014
    CON0019.cc = CON0015
    CON0019.cd = True
    CON0019.ce = True
    CON0019.cf = True
    CON0020.ca = CON0000
    CON0020.cb = CON0018
    CON0020.cc = CON0021
    CON0020.cd = True
    CON0020.ce = True
    CON0020.cf = True
    CON0021.game_object = "NLO:Cube"
    CON0021.property_name = "change mat"
    CON0021.compare_value = False
    CON0021.operator = 0
    ACT0022.condition = CON0026
    ACT0022.game_object = "NLO:Plane.001"
    ACT0022.property_name = "4"
    ACT0022.property_value = False
    ACT0023.condition = CON0026
    ACT0023.game_object = "NLO:Plane"
    ACT0023.property_name = "3"
    ACT0023.property_value = True
    CON0024.game_object = "NLO:Plane.001"
    CON0024.property_name = "4"
    CON0024.compare_value = True
    CON0024.operator = 0
    CON0025.game_object = "NLO:Cube"
    CON0025.property_name = "change mat"
    CON0025.compare_value = False
    CON0025.operator = 0
    CON0026.ca = CON0001
    CON0026.cb = CON0024
    CON0026.cc = CON0025
    CON0026.cd = True
    CON0026.ce = True
    CON0026.cf = True
    ACT0027.condition = CON0030
    ACT0027.game_object = "NLO:Plane.002"
    ACT0027.property_name = "1"
    ACT0027.property_value = False
    ACT0028.condition = CON0030
    ACT0028.game_object = "NLO:Plane.001"
    ACT0028.property_name = "4"
    ACT0028.property_value = True
    CON0029.game_object = "NLO:Cube"
    CON0029.property_name = "change mat"
    CON0029.compare_value = False
    CON0029.operator = 0
    CON0030.ca = CON0001
    CON0030.cb = CON0031
    CON0030.cc = CON0029
    CON0030.cd = True
    CON0030.ce = True
    CON0030.cf = True
    CON0031.game_object = "NLO:Plane.002"
    CON0031.property_name = "1"
    CON0031.compare_value = True
    CON0031.operator = 0
    CON0032.game_object = "NLO:Plane.003"
    CON0032.property_name = "2"
    CON0032.compare_value = True
    CON0032.operator = 0
    CON0033.ca = CON0001
    CON0033.cb = CON0032
    CON0033.cc = CON0034
    CON0033.cd = True
    CON0033.ce = True
    CON0033.cf = True
    CON0034.game_object = "NLO:Cube"
    CON0034.property_name = "change mat"
    CON0034.compare_value = False
    CON0034.operator = 0
    ACT0035.condition = CON0039
    ACT0035.game_object = "NLO:Plane"
    ACT0035.property_name = "3"
    ACT0035.property_value = False
    ACT0036.condition = CON0039
    ACT0036.game_object = "NLO:Plane.003"
    ACT0036.property_name = "2"
    ACT0036.property_value = True
    CON0037.game_object = "NLO:Plane"
    CON0037.property_name = "3"
    CON0037.compare_value = True
    CON0037.operator = 0
    CON0038.game_object = "NLO:Cube"
    CON0038.property_name = "change mat"
    CON0038.compare_value = False
    CON0038.operator = 0
    CON0039.ca = CON0001
    CON0039.cb = CON0037
    CON0039.cc = CON0038
    CON0039.cd = True
    CON0039.ce = True
    CON0039.cf = True
    ACT0040.condition = CON0033
    ACT0040.game_object = "NLO:Plane.003"
    ACT0040.property_name = "2"
    ACT0040.property_value = False
    ACT0041.condition = CON0033
    ACT0041.game_object = "NLO:Plane.002"
    ACT0041.property_name = "1"
    ACT0041.property_value = True
    CON0042.game_object = "NLO:Plane.003"
    CON0042.property_name = "2"
    CON0042.compare_value = True
    CON0042.operator = 0
    ACT0043.condition = CON0042
    ACT0043.game_object = "NLO:Icosphere"
    ACT0043.visible = True
    ACT0043.recursive = False
    ACT0044.condition = CON0046
    ACT0044.xyz = {'x': True, 'y': True, 'z': True}
    ACT0044.game_object = "NLO:Plane"
    ACT0044.attribute_value = mathutils.Vector((1.900596022605896, 1.541003942489624, 1.5946309566497803))
    ACT0044.value_type = 'worldScale'
    ACT0045.condition = CON0046
    ACT0045.game_object = "NLO:Torus"
    ACT0045.visible = True
    ACT0045.recursive = False
    CON0046.game_object = "NLO:Plane"
    CON0046.property_name = "3"
    CON0046.compare_value = True
    CON0046.operator = 0
    ACT0047.condition = CON0048
    ACT0047.xyz = {'x': True, 'y': True, 'z': True}
    ACT0047.game_object = "NLO:Plane.001"
    ACT0047.attribute_value = mathutils.Vector((1.900596022605896, 1.541003942489624, 1.5946309566497803))
    ACT0047.value_type = 'worldScale'
    CON0048.game_object = "NLO:Plane.001"
    CON0048.property_name = "4"
    CON0048.compare_value = True
    CON0048.operator = 0
    CON0049.game_object = "NLO:Plane.003"
    CON0049.property_name = "2"
    CON0049.compare_value = False
    CON0049.operator = 0
    ACT0050.condition = CON0049
    ACT0050.xyz = {'x': True, 'y': True, 'z': True}
    ACT0050.game_object = "NLO:Plane.003"
    ACT0050.attribute_value = mathutils.Vector((0.900596022605896, 0.5410040020942688, 0.594631016254425))
    ACT0050.value_type = 'worldScale'
    ACT0051.condition = CON0049
    ACT0051.game_object = "NLO:Icosphere"
    ACT0051.visible = False
    ACT0051.recursive = False
    CON0052.game_object = "NLO:Plane"
    CON0052.property_name = "3"
    CON0052.compare_value = False
    CON0052.operator = 0
    ACT0053.condition = CON0052
    ACT0053.xyz = {'x': True, 'y': True, 'z': True}
    ACT0053.game_object = "NLO:Plane"
    ACT0053.attribute_value = mathutils.Vector((0.900596022605896, 0.5410040020942688, 0.594631016254425))
    ACT0053.value_type = 'worldScale'
    ACT0054.condition = CON0052
    ACT0054.game_object = "NLO:Torus"
    ACT0054.visible = False
    ACT0054.recursive = False
    CON0055.game_object = "NLO:Plane.001"
    CON0055.property_name = "4"
    CON0055.compare_value = False
    CON0055.operator = 0
    ACT0056.condition = CON0055
    ACT0056.xyz = {'x': True, 'y': True, 'z': True}
    ACT0056.game_object = "NLO:Plane.001"
    ACT0056.attribute_value = mathutils.Vector((0.900596022605896, 0.5410040020942688, 0.594631016254425))
    ACT0056.value_type = 'worldScale'
    CON0057.game_object = "NLO:Plane.002"
    CON0057.property_name = "1"
    CON0057.compare_value = False
    CON0057.operator = 0
    ACT0058.condition = CON0057
    ACT0058.game_object = "NLO:Cone"
    ACT0058.visible = False
    ACT0058.recursive = False
    CON0059.game_object = "NLO:Plane.002"
    CON0059.property_name = "1"
    CON0059.compare_value = True
    CON0059.operator = 0
    ACT0060.condition = CON0059
    ACT0060.xyz = {'x': True, 'y': True, 'z': True}
    ACT0060.game_object = "NLO:Plane.002"
    ACT0060.attribute_value = mathutils.Vector((1.900596022605896, 1.541003942489624, 1.5946309566497803))
    ACT0060.value_type = 'worldScale'
    ACT0061.condition = CON0059
    ACT0061.game_object = "NLO:Cone"
    ACT0061.visible = True
    ACT0061.recursive = False
    ACT0062.condition = CON0042
    ACT0062.xyz = {'x': True, 'y': True, 'z': True}
    ACT0062.game_object = "NLO:Plane.003"
    ACT0062.attribute_value = mathutils.Vector((1.900596022605896, 1.541003942489624, 1.5946309566497803))
    ACT0062.value_type = 'worldScale'
    ACT0063.condition = CON0057
    ACT0063.xyz = {'x': True, 'y': True, 'z': True}
    ACT0063.game_object = "NLO:Plane.002"
    ACT0063.attribute_value = mathutils.Vector((0.900596022605896, 0.5410040020942688, 0.594631016254425))
    ACT0063.value_type = 'worldScale'
    CON0064.key_code = bge.events.ENTERKEY
    CON0064.pulse = False
    CON0065.game_object = "NLO:Cube"
    CON0065.property_name = "change mat"
    CON0065.compare_value = False
    CON0065.operator = 0
    CON0066.game_object = "NLO:Plane.002"
    CON0066.property_name = "1"
    CON0066.compare_value = True
    CON0066.operator = 0
    CON0067.ca = CON0066
    CON0067.cb = CON0065
    CON0067.cc = CON0064
    CON0067.cd = True
    CON0067.ce = True
    CON0067.cf = True
    ACT0068.condition = CON0067
    ACT0068.game_object = "NLO:Cube"
    ACT0068.property_name = "change mat"
    ACT0068.property_value = True
    network.add_cell(CON0000)
    network.add_cell(CON0004)
    network.add_cell(CON0008)
    network.add_cell(CON0010)
    network.add_cell(CON0014)
    network.add_cell(CON0018)
    network.add_cell(CON0021)
    network.add_cell(CON0024)
    network.add_cell(CON0029)
    network.add_cell(CON0031)
    network.add_cell(CON0034)
    network.add_cell(CON0037)
    network.add_cell(CON0042)
    network.add_cell(CON0046)
    network.add_cell(CON0048)
    network.add_cell(CON0052)
    network.add_cell(ACT0054)
    network.add_cell(CON0057)
    network.add_cell(CON0059)
    network.add_cell(ACT0061)
    network.add_cell(ACT0063)
    network.add_cell(CON0065)
    network.add_cell(CON0001)
    network.add_cell(CON0005)
    network.add_cell(CON0011)
    network.add_cell(CON0015)
    network.add_cell(CON0019)
    network.add_cell(CON0025)
    network.add_cell(CON0030)
    network.add_cell(CON0038)
    network.add_cell(ACT0043)
    network.add_cell(ACT0045)
    network.add_cell(CON0049)
    network.add_cell(ACT0051)
    network.add_cell(CON0055)
    network.add_cell(ACT0058)
    network.add_cell(ACT0062)
    network.add_cell(CON0066)
    network.add_cell(CON0006)
    network.add_cell(ACT0009)
    network.add_cell(ACT0013)
    network.add_cell(CON0020)
    network.add_cell(CON0026)
    network.add_cell(ACT0028)
    network.add_cell(CON0039)
    network.add_cell(ACT0044)
    network.add_cell(ACT0050)
    network.add_cell(ACT0056)
    network.add_cell(CON0064)
    network.add_cell(ACT0002)
    network.add_cell(ACT0007)
    network.add_cell(ACT0016)
    network.add_cell(ACT0022)
    network.add_cell(ACT0027)
    network.add_cell(ACT0035)
    network.add_cell(ACT0047)
    network.add_cell(ACT0060)
    network.add_cell(ACT0003)
    network.add_cell(ACT0017)
    network.add_cell(CON0032)
    network.add_cell(ACT0036)
    network.add_cell(ACT0053)
    network.add_cell(ACT0012)
    network.add_cell(CON0033)
    network.add_cell(ACT0041)
    network.add_cell(ACT0023)
    network.add_cell(CON0067)
    network.add_cell(ACT0040)
    network.add_cell(ACT0068)
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
