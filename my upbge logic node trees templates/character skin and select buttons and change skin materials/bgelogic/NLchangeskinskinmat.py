# MACHINE GENERATED
import bge
import mathutils
import bgelogic
import math

def _initialize(owner):
    network = bgelogic.LogicNetwork()
    CON0000 = bgelogic.ConditionAndList()
    CON0001 = bgelogic.ConditionAnd()
    CON0002 = bgelogic.ConditionAndList()
    CON0003 = bgelogic.ObjectPropertyOperator()
    CON0004 = bgelogic.ObjectPropertyOperator()
    CON0005 = bgelogic.ConditionAnd()
    ACT0006 = bgelogic.ActionSetGameObjectGameProperty()
    ACT0007 = bgelogic.ActionSetGameObjectGameProperty()
    CON0008 = bgelogic.ConditionAndList()
    CON0009 = bgelogic.ObjectPropertyOperator()
    CON0010 = bgelogic.ObjectPropertyOperator()
    CON0011 = bgelogic.ConditionAnd()
    ACT0012 = bgelogic.ActionSetGameObjectGameProperty()
    ACT0013 = bgelogic.ActionSetGameObjectGameProperty()
    CON0014 = bgelogic.ConditionAndList()
    CON0015 = bgelogic.ObjectPropertyOperator()
    CON0016 = bgelogic.ObjectPropertyOperator()
    CON0017 = bgelogic.ConditionAnd()
    ACT0018 = bgelogic.ActionSetGameObjectGameProperty()
    ACT0019 = bgelogic.ActionSetGameObjectGameProperty()
    CON0020 = bgelogic.ObjectPropertyOperator()
    CON0021 = bgelogic.ObjectPropertyOperator()
    ACT0022 = bgelogic.ActionSetGameObjectGameProperty()
    ACT0023 = bgelogic.ActionSetGameObjectGameProperty()
    CON0024 = bgelogic.ObjectPropertyOperator()
    CON0025 = bgelogic.ConditionAnd()
    CON0026 = bgelogic.ConditionAndList()
    CON0027 = bgelogic.ObjectPropertyOperator()
    ACT0028 = bgelogic.ActionSetGameObjectGameProperty()
    ACT0029 = bgelogic.ActionSetGameObjectGameProperty()
    CON0030 = bgelogic.ObjectPropertyOperator()
    CON0031 = bgelogic.ConditionAndList()
    CON0032 = bgelogic.ConditionAnd()
    CON0033 = bgelogic.ObjectPropertyOperator()
    ACT0034 = bgelogic.ActionSetGameObjectGameProperty()
    ACT0035 = bgelogic.ActionSetGameObjectGameProperty()
    CON0036 = bgelogic.ConditionKeyPressed()
    CON0037 = bgelogic.ConditionKeyPressed()
    CON0038 = bgelogic.ObjectPropertyOperator()
    ACT0039 = bgelogic.SetMaterial()
    ACT0040 = bgelogic.SetMaterial()
    CON0041 = bgelogic.ObjectPropertyOperator()
    CON0042 = bgelogic.ObjectPropertyOperator()
    ACT0043 = bgelogic.SetMaterial()
    CON0044 = bgelogic.ObjectPropertyOperator()
    ACT0045 = bgelogic.ActionSetObjectAttribute()
    ACT0046 = bgelogic.ActionSetGameObjectVisibility()
    CON0047 = bgelogic.ObjectPropertyOperator()
    ACT0048 = bgelogic.ActionSetObjectAttribute()
    CON0049 = bgelogic.ObjectPropertyOperator()
    CON0050 = bgelogic.ObjectPropertyOperator()
    ACT0051 = bgelogic.ActionSetObjectAttribute()
    ACT0052 = bgelogic.ActionSetGameObjectVisibility()
    CON0053 = bgelogic.ObjectPropertyOperator()
    ACT0054 = bgelogic.ActionSetObjectAttribute()
    CON0055 = bgelogic.ObjectPropertyOperator()
    ACT0056 = bgelogic.ActionSetGameObjectVisibility()
    CON0057 = bgelogic.ObjectPropertyOperator()
    ACT0058 = bgelogic.ActionSetObjectAttribute()
    ACT0059 = bgelogic.ActionSetGameObjectVisibility()
    ACT0060 = bgelogic.ActionSetObjectAttribute()
    CON0061 = bgelogic.ObjectPropertyOperator()
    ACT0062 = bgelogic.ActionSetObjectAttribute()
    ACT0063 = bgelogic.ActionSetGameObjectVisibility()
    CON0064 = bgelogic.ObjectPropertyOperator()
    ACT0065 = bgelogic.ActionSetGameObjectVisibility()
    ACT0066 = bgelogic.ActionSetObjectAttribute()
    CON0067 = bgelogic.ConditionKeyPressed()
    CON0068 = bgelogic.ConditionAndList()
    ACT0069 = bgelogic.ActionSetGameObjectGameProperty()
    CON0070 = bgelogic.ObjectPropertyOperator()
    CON0071 = bgelogic.ConditionAnd()
    CON0072 = bgelogic.ObjectPropertyOperator()
    CON0073 = bgelogic.ConditionKeyPressed()
    ACT0074 = bgelogic.ActionSetGameObjectGameProperty()
    ACT0075 = bgelogic.ActionSetGameObjectGameProperty()
    ACT0076 = bgelogic.ActionSetGameObjectGameProperty()
    CON0077 = bgelogic.ConditionAndList()
    CON0078 = bgelogic.ObjectPropertyOperator()
    CON0079 = bgelogic.ObjectPropertyOperator()
    ACT0080 = bgelogic.ActionSetGameObjectGameProperty()
    ACT0081 = bgelogic.ActionSetGameObjectGameProperty()
    CON0082 = bgelogic.ObjectPropertyOperator()
    CON0083 = bgelogic.ConditionAndList()
    CON0084 = bgelogic.ObjectPropertyOperator()
    CON0085 = bgelogic.ObjectPropertyOperator()
    CON0086 = bgelogic.ConditionAndList()
    CON0087 = bgelogic.ObjectPropertyOperator()
    ACT0088 = bgelogic.ActionSetGameObjectGameProperty()
    ACT0089 = bgelogic.ActionSetGameObjectGameProperty()
    CON0090 = bgelogic.ConditionAndList()
    CON0091 = bgelogic.ObjectPropertyOperator()
    CON0092 = bgelogic.ObjectPropertyOperator()
    ACT0093 = bgelogic.ActionSetGameObjectGameProperty()
    ACT0094 = bgelogic.ActionSetGameObjectGameProperty()
    CON0095 = bgelogic.ObjectPropertyOperator()
    CON0096 = bgelogic.ConditionAndList()
    CON0097 = bgelogic.ConditionAndList()
    CON0098 = bgelogic.ObjectPropertyOperator()
    ACT0099 = bgelogic.ActionSetGameObjectGameProperty()
    ACT0100 = bgelogic.ActionSetGameObjectGameProperty()
    CON0101 = bgelogic.ObjectPropertyOperator()
    CON0102 = bgelogic.ObjectPropertyOperator()
    ACT0103 = bgelogic.ActionSetGameObjectGameProperty()
    ACT0104 = bgelogic.ActionSetGameObjectGameProperty()
    CON0105 = bgelogic.ConditionAndList()
    CON0106 = bgelogic.ObjectPropertyOperator()
    ACT0107 = bgelogic.ActionSetGameObjectGameProperty()
    CON0108 = bgelogic.ObjectPropertyOperator()
    ACT0109 = bgelogic.ActionSetGameObjectGameProperty()
    CON0110 = bgelogic.ConditionAndList()
    CON0111 = bgelogic.ObjectPropertyOperator()
    CON0112 = bgelogic.ObjectPropertyOperator()
    ACT0113 = bgelogic.ActionSetGameObjectGameProperty()
    ACT0114 = bgelogic.ActionSetGameObjectGameProperty()
    CON0115 = bgelogic.ConditionKeyPressed()
    CON0116 = bgelogic.ConditionKeyPressed()
    CON0000.ca = CON0037
    CON0000.cb = True
    CON0000.cc = CON0020
    CON0000.cd = True
    CON0000.ce = True
    CON0000.cf = True
    CON0001.condition_a = CON0000
    CON0001.condition_b = CON0021
    CON0002.ca = CON0036
    CON0002.cb = CON0038
    CON0002.cc = CON0004
    CON0002.cd = True
    CON0002.ce = True
    CON0002.cf = True
    CON0003.game_object = "NLO:Cone"
    CON0003.property_name = "mat 3"
    CON0003.compare_value = True
    CON0003.operator = 0
    CON0004.game_object = "NLO:Cube"
    CON0004.property_name = "change mat"
    CON0004.compare_value = True
    CON0004.operator = 0
    CON0005.condition_a = CON0002
    CON0005.condition_b = CON0003
    ACT0006.condition = CON0005
    ACT0006.game_object = "NLO:Cone"
    ACT0006.property_name = "mat 3"
    ACT0006.property_value = False
    ACT0007.condition = CON0005
    ACT0007.game_object = "NLO:Cone"
    ACT0007.property_name = "mat 1"
    ACT0007.property_value = True
    CON0008.ca = CON0036
    CON0008.cb = CON0038
    CON0008.cc = CON0010
    CON0008.cd = True
    CON0008.ce = True
    CON0008.cf = True
    CON0009.game_object = "NLO:Cone"
    CON0009.property_name = "mat 2"
    CON0009.compare_value = True
    CON0009.operator = 0
    CON0010.game_object = "NLO:Cube"
    CON0010.property_name = "change mat"
    CON0010.compare_value = True
    CON0010.operator = 0
    CON0011.condition_a = CON0008
    CON0011.condition_b = CON0009
    ACT0012.condition = CON0011
    ACT0012.game_object = "NLO:Cone"
    ACT0012.property_name = "mat 2"
    ACT0012.property_value = False
    ACT0013.condition = CON0011
    ACT0013.game_object = "NLO:Cone"
    ACT0013.property_name = "mat 3"
    ACT0013.property_value = True
    CON0014.ca = CON0036
    CON0014.cb = CON0038
    CON0014.cc = CON0016
    CON0014.cd = True
    CON0014.ce = True
    CON0014.cf = True
    CON0015.game_object = "NLO:Cone"
    CON0015.property_name = "mat 1"
    CON0015.compare_value = True
    CON0015.operator = 0
    CON0016.game_object = "NLO:Cube"
    CON0016.property_name = "change mat"
    CON0016.compare_value = True
    CON0016.operator = 0
    CON0017.condition_a = CON0014
    CON0017.condition_b = CON0015
    ACT0018.condition = CON0017
    ACT0018.game_object = "NLO:Cone"
    ACT0018.property_name = "mat 2"
    ACT0018.property_value = True
    ACT0019.condition = CON0017
    ACT0019.game_object = "NLO:Cone"
    ACT0019.property_name = "mat 1"
    ACT0019.property_value = False
    CON0020.game_object = "NLO:Cube"
    CON0020.property_name = "change mat"
    CON0020.compare_value = True
    CON0020.operator = 0
    CON0021.game_object = "NLO:Cone"
    CON0021.property_name = "mat 3"
    CON0021.compare_value = True
    CON0021.operator = 0
    ACT0022.condition = CON0001
    ACT0022.game_object = "NLO:Cone"
    ACT0022.property_name = "mat 3"
    ACT0022.property_value = False
    ACT0023.condition = CON0001
    ACT0023.game_object = "NLO:Cone"
    ACT0023.property_name = "mat 2"
    ACT0023.property_value = True
    CON0024.game_object = "NLO:Cube"
    CON0024.property_name = "change mat"
    CON0024.compare_value = True
    CON0024.operator = 0
    CON0025.condition_a = CON0026
    CON0025.condition_b = CON0027
    CON0026.ca = CON0037
    CON0026.cb = True
    CON0026.cc = CON0024
    CON0026.cd = True
    CON0026.ce = True
    CON0026.cf = True
    CON0027.game_object = "NLO:Cone"
    CON0027.property_name = "mat 2"
    CON0027.compare_value = True
    CON0027.operator = 0
    ACT0028.condition = CON0025
    ACT0028.game_object = "NLO:Cone"
    ACT0028.property_name = "mat 2"
    ACT0028.property_value = False
    ACT0029.condition = CON0025
    ACT0029.game_object = "NLO:Cone"
    ACT0029.property_name = "mat 1"
    ACT0029.property_value = True
    CON0030.game_object = "NLO:Cube"
    CON0030.property_name = "change mat"
    CON0030.compare_value = True
    CON0030.operator = 0
    CON0031.ca = CON0037
    CON0031.cb = True
    CON0031.cc = CON0030
    CON0031.cd = True
    CON0031.ce = True
    CON0031.cf = True
    CON0032.condition_a = CON0031
    CON0032.condition_b = CON0033
    CON0033.game_object = "NLO:Cone"
    CON0033.property_name = "mat 1"
    CON0033.compare_value = True
    CON0033.operator = 0
    ACT0034.condition = CON0032
    ACT0034.game_object = "NLO:Cone"
    ACT0034.property_name = "mat 1"
    ACT0034.property_value = False
    ACT0035.condition = CON0032
    ACT0035.game_object = "NLO:Cone"
    ACT0035.property_name = "mat 3"
    ACT0035.property_value = True
    CON0036.key_code = bge.events.RIGHTARROWKEY
    CON0036.pulse = False
    CON0037.key_code = bge.events.LEFTARROWKEY
    CON0037.pulse = False
    CON0038.game_object = "NLO:Plane.002"
    CON0038.property_name = "1"
    CON0038.compare_value = True
    CON0038.operator = 0
    ACT0039.condition = CON0041
    ACT0039.game_object = "NLO:Cone"
    ACT0039.slot = 1
    ACT0039.mat_name = "green"
    ACT0040.condition = CON0042
    ACT0040.game_object = "NLO:Cone"
    ACT0040.slot = 1
    ACT0040.mat_name = "blue"
    CON0041.game_object = "NLO:Cone"
    CON0041.property_name = "mat 2"
    CON0041.compare_value = True
    CON0041.operator = 0
    CON0042.game_object = "NLO:Cone"
    CON0042.property_name = "mat 3"
    CON0042.compare_value = True
    CON0042.operator = 0
    ACT0043.condition = CON0044
    ACT0043.game_object = "NLO:Cone"
    ACT0043.slot = 1
    ACT0043.mat_name = "ruby"
    CON0044.game_object = "NLO:Cone"
    CON0044.property_name = "mat 1"
    CON0044.compare_value = True
    CON0044.operator = 0
    ACT0045.condition = CON0047
    ACT0045.xyz = {'x': True, 'y': True, 'z': True}
    ACT0045.game_object = "NLO:Plane"
    ACT0045.attribute_value = mathutils.Vector((1.900596022605896, 1.541003942489624, 1.5946309566497803))
    ACT0045.value_type = 'worldScale'
    ACT0046.condition = CON0047
    ACT0046.game_object = "NLO:Torus"
    ACT0046.visible = True
    ACT0046.recursive = False
    CON0047.game_object = "NLO:Plane"
    CON0047.property_name = "3"
    CON0047.compare_value = True
    CON0047.operator = 0
    ACT0048.condition = CON0049
    ACT0048.xyz = {'x': True, 'y': True, 'z': True}
    ACT0048.game_object = "NLO:Plane.001"
    ACT0048.attribute_value = mathutils.Vector((1.900596022605896, 1.541003942489624, 1.5946309566497803))
    ACT0048.value_type = 'worldScale'
    CON0049.game_object = "NLO:Plane.001"
    CON0049.property_name = "4"
    CON0049.compare_value = True
    CON0049.operator = 0
    CON0050.game_object = "NLO:Plane"
    CON0050.property_name = "3"
    CON0050.compare_value = False
    CON0050.operator = 0
    ACT0051.condition = CON0050
    ACT0051.xyz = {'x': True, 'y': True, 'z': True}
    ACT0051.game_object = "NLO:Plane"
    ACT0051.attribute_value = mathutils.Vector((0.900596022605896, 0.5410040020942688, 0.594631016254425))
    ACT0051.value_type = 'worldScale'
    ACT0052.condition = CON0050
    ACT0052.game_object = "NLO:Torus"
    ACT0052.visible = False
    ACT0052.recursive = False
    CON0053.game_object = "NLO:Plane.001"
    CON0053.property_name = "4"
    CON0053.compare_value = False
    CON0053.operator = 0
    ACT0054.condition = CON0053
    ACT0054.xyz = {'x': True, 'y': True, 'z': True}
    ACT0054.game_object = "NLO:Plane.001"
    ACT0054.attribute_value = mathutils.Vector((0.900596022605896, 0.5410040020942688, 0.594631016254425))
    ACT0054.value_type = 'worldScale'
    CON0055.game_object = "NLO:Plane.002"
    CON0055.property_name = "1"
    CON0055.compare_value = False
    CON0055.operator = 0
    ACT0056.condition = CON0055
    ACT0056.game_object = "NLO:Cone"
    ACT0056.visible = False
    ACT0056.recursive = False
    CON0057.game_object = "NLO:Plane.002"
    CON0057.property_name = "1"
    CON0057.compare_value = True
    CON0057.operator = 0
    ACT0058.condition = CON0057
    ACT0058.xyz = {'x': True, 'y': True, 'z': True}
    ACT0058.game_object = "NLO:Plane.002"
    ACT0058.attribute_value = mathutils.Vector((1.900596022605896, 1.541003942489624, 1.5946309566497803))
    ACT0058.value_type = 'worldScale'
    ACT0059.condition = CON0057
    ACT0059.game_object = "NLO:Cone"
    ACT0059.visible = True
    ACT0059.recursive = False
    ACT0060.condition = CON0055
    ACT0060.xyz = {'x': True, 'y': True, 'z': True}
    ACT0060.game_object = "NLO:Plane.002"
    ACT0060.attribute_value = mathutils.Vector((0.900596022605896, 0.5410040020942688, 0.594631016254425))
    ACT0060.value_type = 'worldScale'
    CON0061.game_object = "NLO:Plane.003"
    CON0061.property_name = "2"
    CON0061.compare_value = False
    CON0061.operator = 0
    ACT0062.condition = CON0061
    ACT0062.xyz = {'x': True, 'y': True, 'z': True}
    ACT0062.game_object = "NLO:Plane.003"
    ACT0062.attribute_value = mathutils.Vector((0.900596022605896, 0.5410040020942688, 0.594631016254425))
    ACT0062.value_type = 'worldScale'
    ACT0063.condition = CON0061
    ACT0063.game_object = "NLO:Icosphere"
    ACT0063.visible = False
    ACT0063.recursive = False
    CON0064.game_object = "NLO:Plane.003"
    CON0064.property_name = "2"
    CON0064.compare_value = True
    CON0064.operator = 0
    ACT0065.condition = CON0064
    ACT0065.game_object = "NLO:Icosphere"
    ACT0065.visible = True
    ACT0065.recursive = False
    ACT0066.condition = CON0064
    ACT0066.xyz = {'x': True, 'y': True, 'z': True}
    ACT0066.game_object = "NLO:Plane.003"
    ACT0066.attribute_value = mathutils.Vector((1.900596022605896, 1.541003942489624, 1.5946309566497803))
    ACT0066.value_type = 'worldScale'
    CON0067.key_code = bge.events.ENTERKEY
    CON0067.pulse = False
    CON0068.ca = True
    CON0068.cb = CON0070
    CON0068.cc = CON0067
    CON0068.cd = True
    CON0068.ce = True
    CON0068.cf = True
    ACT0069.condition = CON0068
    ACT0069.game_object = "NLO:Cube"
    ACT0069.property_name = "change mat"
    ACT0069.property_value = True
    CON0070.game_object = "NLO:Cube"
    CON0070.property_name = "change mat"
    CON0070.compare_value = False
    CON0070.operator = 0
    CON0071.condition_a = CON0072
    CON0071.condition_b = CON0073
    CON0072.game_object = "NLO:Cube"
    CON0072.property_name = "change mat"
    CON0072.compare_value = True
    CON0072.operator = 0
    CON0073.key_code = bge.events.QKEY
    CON0073.pulse = False
    ACT0074.condition = CON0071
    ACT0074.game_object = "NLO:Cube"
    ACT0074.property_name = "change mat"
    ACT0074.property_value = False
    ACT0075.condition = CON0083
    ACT0075.game_object = "NLO:Plane.002"
    ACT0075.property_name = "1"
    ACT0075.property_value = True
    ACT0076.condition = CON0083
    ACT0076.game_object = "NLO:Plane.003"
    ACT0076.property_name = "2"
    ACT0076.property_value = False
    CON0077.ca = CON0115
    CON0077.cb = CON0079
    CON0077.cc = CON0078
    CON0077.cd = True
    CON0077.ce = True
    CON0077.cf = True
    CON0078.game_object = "NLO:Cube"
    CON0078.property_name = "change mat"
    CON0078.compare_value = False
    CON0078.operator = 0
    CON0079.game_object = "NLO:Plane"
    CON0079.property_name = "3"
    CON0079.compare_value = True
    CON0079.operator = 0
    ACT0080.condition = CON0077
    ACT0080.game_object = "NLO:Plane.003"
    ACT0080.property_name = "2"
    ACT0080.property_value = True
    ACT0081.condition = CON0077
    ACT0081.game_object = "NLO:Plane"
    ACT0081.property_name = "3"
    ACT0081.property_value = False
    CON0082.game_object = "NLO:Cube"
    CON0082.property_name = "change mat"
    CON0082.compare_value = False
    CON0082.operator = 0
    CON0083.ca = CON0115
    CON0083.cb = CON0084
    CON0083.cc = CON0082
    CON0083.cd = True
    CON0083.ce = True
    CON0083.cf = True
    CON0084.game_object = "NLO:Plane.003"
    CON0084.property_name = "2"
    CON0084.compare_value = True
    CON0084.operator = 0
    CON0085.game_object = "NLO:Plane.002"
    CON0085.property_name = "1"
    CON0085.compare_value = True
    CON0085.operator = 0
    CON0086.ca = CON0115
    CON0086.cb = CON0085
    CON0086.cc = CON0087
    CON0086.cd = True
    CON0086.ce = True
    CON0086.cf = True
    CON0087.game_object = "NLO:Cube"
    CON0087.property_name = "change mat"
    CON0087.compare_value = False
    CON0087.operator = 0
    ACT0088.condition = CON0086
    ACT0088.game_object = "NLO:Plane.001"
    ACT0088.property_name = "4"
    ACT0088.property_value = True
    ACT0089.condition = CON0086
    ACT0089.game_object = "NLO:Plane.002"
    ACT0089.property_name = "1"
    ACT0089.property_value = False
    CON0090.ca = CON0115
    CON0090.cb = CON0092
    CON0090.cc = CON0091
    CON0090.cd = True
    CON0090.ce = True
    CON0090.cf = True
    CON0091.game_object = "NLO:Cube"
    CON0091.property_name = "change mat"
    CON0091.compare_value = False
    CON0091.operator = 0
    CON0092.game_object = "NLO:Plane.001"
    CON0092.property_name = "4"
    CON0092.compare_value = True
    CON0092.operator = 0
    ACT0093.condition = CON0090
    ACT0093.game_object = "NLO:Plane"
    ACT0093.property_name = "3"
    ACT0093.property_value = True
    ACT0094.condition = CON0090
    ACT0094.game_object = "NLO:Plane.001"
    ACT0094.property_name = "4"
    ACT0094.property_value = False
    CON0095.game_object = "NLO:Cube"
    CON0095.property_name = "change mat"
    CON0095.compare_value = False
    CON0095.operator = 0
    CON0096.ca = CON0116
    CON0096.cb = CON0098
    CON0096.cc = CON0095
    CON0096.cd = True
    CON0096.ce = True
    CON0096.cf = True
    CON0097.ca = CON0116
    CON0097.cb = CON0102
    CON0097.cc = CON0101
    CON0097.cd = True
    CON0097.ce = True
    CON0097.cf = True
    CON0098.game_object = "NLO:Plane.002"
    CON0098.property_name = "1"
    CON0098.compare_value = True
    CON0098.operator = 0
    ACT0099.condition = CON0096
    ACT0099.game_object = "NLO:Plane.003"
    ACT0099.property_name = "2"
    ACT0099.property_value = True
    ACT0100.condition = CON0096
    ACT0100.game_object = "NLO:Plane.002"
    ACT0100.property_name = "1"
    ACT0100.property_value = False
    CON0101.game_object = "NLO:Cube"
    CON0101.property_name = "change mat"
    CON0101.compare_value = False
    CON0101.operator = 0
    CON0102.game_object = "NLO:Plane.003"
    CON0102.property_name = "2"
    CON0102.compare_value = True
    CON0102.operator = 0
    ACT0103.condition = CON0097
    ACT0103.game_object = "NLO:Plane"
    ACT0103.property_name = "3"
    ACT0103.property_value = True
    ACT0104.condition = CON0097
    ACT0104.game_object = "NLO:Plane.003"
    ACT0104.property_name = "2"
    ACT0104.property_value = False
    CON0105.ca = CON0116
    CON0105.cb = CON0108
    CON0105.cc = CON0106
    CON0105.cd = True
    CON0105.ce = True
    CON0105.cf = True
    CON0106.game_object = "NLO:Cube"
    CON0106.property_name = "change mat"
    CON0106.compare_value = False
    CON0106.operator = 0
    ACT0107.condition = CON0105
    ACT0107.game_object = "NLO:Plane.002"
    ACT0107.property_name = "1"
    ACT0107.property_value = True
    CON0108.game_object = "NLO:Plane.001"
    CON0108.property_name = "4"
    CON0108.compare_value = True
    CON0108.operator = 0
    ACT0109.condition = CON0105
    ACT0109.game_object = "NLO:Plane.001"
    ACT0109.property_name = "4"
    ACT0109.property_value = False
    CON0110.ca = CON0116
    CON0110.cb = CON0112
    CON0110.cc = CON0111
    CON0110.cd = True
    CON0110.ce = True
    CON0110.cf = True
    CON0111.game_object = "NLO:Cube"
    CON0111.property_name = "change mat"
    CON0111.compare_value = False
    CON0111.operator = 0
    CON0112.game_object = "NLO:Plane"
    CON0112.property_name = "3"
    CON0112.compare_value = True
    CON0112.operator = 0
    ACT0113.condition = CON0110
    ACT0113.game_object = "NLO:Plane.001"
    ACT0113.property_name = "4"
    ACT0113.property_value = True
    ACT0114.condition = CON0110
    ACT0114.game_object = "NLO:Plane"
    ACT0114.property_name = "3"
    ACT0114.property_value = False
    CON0115.key_code = bge.events.LEFTARROWKEY
    CON0115.pulse = False
    CON0116.key_code = bge.events.RIGHTARROWKEY
    CON0116.pulse = False
    network.add_cell(CON0003)
    network.add_cell(CON0009)
    network.add_cell(CON0015)
    network.add_cell(CON0020)
    network.add_cell(CON0024)
    network.add_cell(CON0027)
    network.add_cell(CON0030)
    network.add_cell(CON0033)
    network.add_cell(CON0036)
    network.add_cell(CON0038)
    network.add_cell(CON0041)
    network.add_cell(CON0044)
    network.add_cell(CON0047)
    network.add_cell(CON0049)
    network.add_cell(CON0053)
    network.add_cell(CON0055)
    network.add_cell(CON0057)
    network.add_cell(ACT0059)
    network.add_cell(CON0061)
    network.add_cell(ACT0063)
    network.add_cell(CON0067)
    network.add_cell(CON0070)
    network.add_cell(CON0072)
    network.add_cell(CON0078)
    network.add_cell(CON0082)
    network.add_cell(CON0084)
    network.add_cell(CON0087)
    network.add_cell(CON0091)
    network.add_cell(CON0095)
    network.add_cell(CON0098)
    network.add_cell(CON0101)
    network.add_cell(CON0106)
    network.add_cell(CON0108)
    network.add_cell(CON0111)
    network.add_cell(CON0115)
    network.add_cell(CON0004)
    network.add_cell(CON0010)
    network.add_cell(CON0016)
    network.add_cell(CON0021)
    network.add_cell(CON0037)
    network.add_cell(CON0042)
    network.add_cell(ACT0045)
    network.add_cell(ACT0048)
    network.add_cell(ACT0054)
    network.add_cell(ACT0058)
    network.add_cell(ACT0062)
    network.add_cell(CON0068)
    network.add_cell(CON0073)
    network.add_cell(CON0079)
    network.add_cell(CON0083)
    network.add_cell(CON0092)
    network.add_cell(CON0102)
    network.add_cell(CON0112)
    network.add_cell(CON0116)
    network.add_cell(CON0000)
    network.add_cell(CON0002)
    network.add_cell(CON0008)
    network.add_cell(CON0014)
    network.add_cell(CON0026)
    network.add_cell(CON0031)
    network.add_cell(ACT0039)
    network.add_cell(ACT0043)
    network.add_cell(CON0050)
    network.add_cell(ACT0052)
    network.add_cell(ACT0060)
    network.add_cell(ACT0069)
    network.add_cell(ACT0075)
    network.add_cell(CON0077)
    network.add_cell(ACT0081)
    network.add_cell(CON0090)
    network.add_cell(ACT0094)
    network.add_cell(CON0097)
    network.add_cell(ACT0103)
    network.add_cell(CON0105)
    network.add_cell(ACT0109)
    network.add_cell(CON0001)
    network.add_cell(CON0011)
    network.add_cell(ACT0013)
    network.add_cell(ACT0022)
    network.add_cell(CON0025)
    network.add_cell(ACT0029)
    network.add_cell(ACT0040)
    network.add_cell(ACT0051)
    network.add_cell(CON0064)
    network.add_cell(ACT0066)
    network.add_cell(ACT0076)
    network.add_cell(CON0085)
    network.add_cell(ACT0093)
    network.add_cell(ACT0104)
    network.add_cell(CON0110)
    network.add_cell(ACT0114)
    network.add_cell(CON0005)
    network.add_cell(ACT0007)
    network.add_cell(CON0017)
    network.add_cell(ACT0019)
    network.add_cell(ACT0028)
    network.add_cell(ACT0046)
    network.add_cell(ACT0065)
    network.add_cell(ACT0080)
    network.add_cell(CON0096)
    network.add_cell(ACT0100)
    network.add_cell(ACT0113)
    network.add_cell(ACT0006)
    network.add_cell(ACT0018)
    network.add_cell(CON0032)
    network.add_cell(ACT0035)
    network.add_cell(CON0071)
    network.add_cell(CON0086)
    network.add_cell(ACT0089)
    network.add_cell(ACT0107)
    network.add_cell(ACT0012)
    network.add_cell(ACT0034)
    network.add_cell(ACT0074)
    network.add_cell(ACT0099)
    network.add_cell(ACT0023)
    network.add_cell(ACT0088)
    network.add_cell(ACT0056)
    owner["IGNLTree_change skin & skin mat"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NL__change skin & skin mat')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("IGNLTree_change skin & skin mat")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
