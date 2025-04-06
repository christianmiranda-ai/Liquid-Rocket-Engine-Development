# Design Document
# by: Christian Miranda

# ---------------------------------------------------------------------------------------------------
# commit?
# Library Import:
import numpy as np
import scipy as spi
import math
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------------------------------

# Section 1:

g_0 = 9.81
rho = 1
A = 1 # cross-sectional area (m^2)
v = 1 # fluid velocity (m/s)

# m_dot = rho * v * A

# -----

class Pump:
    def __init__(self,p_inlet,p_outlet,v_inlet,v_outlet,efficiency)
    self.p_inlet = p_inlet
    self.p_outlet = p_outlet
    self.v_inlet = v_inlet
    self.v_outlet = v_outlet
    self.efficiency = efficiency

    def head(self,)

# -----



m_dot_ox = 1
m_dot_fuel = 1
m_dot_total = m_dot_ox + m_dot_fuel

NPSH_a = ((p_inlet / rho*g_0) - h_vap - h_fric) # net positive suction head (units?)

H = ((p_outlet - p_inlet) / rho*g_0) + ((v_outlet**2) - (v_inlet**2) / (2*g_0) ) # pump head (m)

p_useful = 1 # useful power delivered to fluid (kW)
p_input = 1 # total mechanical power input (kW)

n_mech = p_useful / p_input # mechanical efficiency of a pump (unitless)

s_in = 1 # entropy generation at inlet
s_out = 1 # entropy generation at outlet
s_gen = m_dot_total(s_out - s_in) # entropy generated across a section (J/(kg*K))

W_out = 1 # work output by turbine (kW)
W_in = 1 # work input by turbine (kW)
n_turb = W_out / W_in # mechanical efficiency of turbine (unitless)

h_in = None # enthalpy at inlet 
h_out = None #

delta_h = h_in - h_out # change in enthalpy for turbine (J/kg)

mixR = m