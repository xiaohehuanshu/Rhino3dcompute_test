import compute_rhino3d.Util
import compute_rhino3d.Grasshopper as gh
import rhino3dm
import json

compute_rhino3d.Util.url = "http://localhost:8081/"
#compute_rhino3d.Util.apiKey = ""

#input parameters
GEO1_IN_PX = 0
GEO1_IN_PY = 0
GEO1_IN_DX = 20
GEO1_IN_DY = 20

GEO2_IN_PX = 15
GEO2_IN_PY = 15
GEO2_IN_DX = 20
GEO2_IN_DY = 20

#create list of input trees
#rectangle1
room1_px_tree = gh.DataTree("GEO1_IN_PX")
room1_px_tree.Append([0], [GEO1_IN_PX])
print(room1_px_tree.data)

room1_py_tree = gh.DataTree("GEO1_IN_PY")
room1_py_tree.Append([0], [GEO1_IN_PY])

room1_dx_tree = gh.DataTree("GEO1_IN_DX")
room1_dx_tree.Append([0], [GEO1_IN_DX])

room1_dy_tree = gh.DataTree("GEO1_IN_DY")
room1_dy_tree.Append([0], [GEO1_IN_DY])

#rectangle2
room2_px_tree = gh.DataTree("GEO2_IN_PX")
room2_px_tree.Append([0], [GEO2_IN_PX])

room2_py_tree = gh.DataTree("GEO2_IN_PY")
room2_py_tree.Append([0], [GEO2_IN_PY])

room2_dx_tree = gh.DataTree("GEO2_IN_DX")
room2_dx_tree.Append([0], [GEO2_IN_DX])

room2_dy_tree = gh.DataTree("GEO2_IN_DY")
room2_dy_tree.Append([0], [GEO2_IN_DY])

trees = [room1_px_tree, room1_py_tree, room1_dx_tree, room1_dy_tree, room2_px_tree, room2_py_tree, room2_dx_tree, room2_dy_tree]

output = gh.EvaluateDefinition('My_test.gh', trees)
print(output)

# decode results
branch = output['values'][0]['InnerTree']['{ 0; }']