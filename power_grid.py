import pandapower as pp

#create empty net
net = pp.create_empty_network()

#create buses
b1 = pp.create_bus(net, vn_kv=20., name="Bus 1")
b2 = pp.create_bus(net, vn_kv=0.4, name="Bus 2")
b3 = pp.create_bus(net, vn_kv=0.4, name="Bus 3")
b4 = pp.create_bus(net, vn_kv=0.4,name="Bus 4")
b5 = pp.create_bus(net, vn_kv=0.4,name="Bus 5")
b6 = pp.create_bus(net, vn_kv=0.4,name="Bus 6")


#create bus elements
pp.create_ext_grid(net, bus=b1, vm_pu=1.02, name="Grid Connection")
pp.create_ext_grid(net, bus=b6, vm_pu=1.02, name="Grid Connection1")
pp.create_load(net, bus=b3, p_mw=0.1, q_mvar=0.05, name="Load")
pp.create_load(net, bus=b4, p_mw=0.1, q_mvar=0.05, name="Load1")
pp.create_sgen(net, bus=b5, p_mw = 120,name="PV1")
pp.create_sgen(net, bus=b5, p_mw = 120,name="PV2")
pp.create_sgen(net, bus=b5, p_mw = 120,name="PV3")
pp.create_sgen(net, bus=b5, p_mw = 120,name="PV4")
pp.create_sgen(net, bus=b5, p_mw = 120,name="PV5")




#create branch elements
pp.create_transformer(net, hv_bus=b1, lv_bus=b2, std_type="0.4 MVA 20/0.4 kV", name="Trafo")
pp.create_transformer(net, hv_bus=b1, lv_bus=b4, std_type="0.4 MVA 20/0.4 kV", name="Trafo1")
pp.create_line(net, from_bus=b2, to_bus=b3, length_km=0.1, name="Line",std_type="NAYY 4x50 SE")
pp.create_line(net, from_bus=b4, to_bus=b5, length_km=0.1, name="Line1",std_type="NAYY 4x50 SE")
pp.create_line(net, from_bus=b5, to_bus=b6, length_km=0.1, name="Line2",std_type="NAYY 4x50 SE")

print(net)
print(net.res_load)
print(net.res_bus)
print(net.res_trafo)

def run_simulation():
    pp.runpp(net)
    return net
