import pandas
import vart
import xir
import os

data = pandas.read_csv("vitis-testing/Direct_Kernel_Set_I_Classifications.csv")
g = xir.Graph.deserialize("test.xmodel")
root_subgraph = g.get_root_subgraph()
child_subgraphs = root_subgraph.toposort_child_subgraph()

child_subgraphs = [
    cs
    for cs in child_subgraphs
    if cs.has_attr("device") and cs.get_attr("device").upper() == "DPU"
]


test = vart.Runner.create_runner(child_subgraphs[2], "run")
