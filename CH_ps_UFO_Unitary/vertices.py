# This file was automatically created by FeynRules 2.3.32
# Mathematica version: 11.3.0 for Mac OS X x86 (64-bit) (March 7, 2018)
# Date: Sat 4 May 2019 15:32:53


from object_library import all_vertices, Vertex
import particles as P
import couplings as C
import lorentz as L


V_1 = Vertex(name = 'V_1',
             particles = [ P.a, P.a, P.eta ],
             color = [ '1' ],
             lorentz = [ L.VVS2 ],
             couplings = {(0,0):C.GC_1})

V_2 = Vertex(name = 'V_2',
             particles = [ P.a, P.Z, P.eta ],
             color = [ '1' ],
             lorentz = [ L.VVS2 ],
             couplings = {(0,0):C.GC_7})

V_3 = Vertex(name = 'V_3',
             particles = [ P.Z, P.Z, P.eta ],
             color = [ '1' ],
             lorentz = [ L.VVS2 ],
             couplings = {(0,0):C.GC_8})

V_4 = Vertex(name = 'V_4',
             particles = [ P.W__minus__, P.W__plus__, P.eta ],
             color = [ '1' ],
             lorentz = [ L.VVS2 ],
             couplings = {(0,0):C.GC_5})

V_5 = Vertex(name = 'V_5',
             particles = [ P.g, P.g, P.eta ],
             color = [ 'Identity(1,2)' ],
             lorentz = [ L.VVS1 ],
             couplings = {(0,0):C.GC_2})

V_6 = Vertex(name = 'V_6',
             particles = [ P.g, P.g, P.g, P.eta ],
             color = [ 'f(1,2,3)' ],
             lorentz = [ L.VVVS2 ],
             couplings = {(0,0):C.GC_3})

V_7 = Vertex(name = 'V_7',
             particles = [ P.eta, P.eta, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSS1 ],
             couplings = {(0,0):C.GC_27})

V_8 = Vertex(name = 'V_8',
             particles = [ P.d__tilde__, P.d, P.eta, P.H ],
             color = [ 'Identity(1,2)' ],
             lorentz = [ L.FFSS1 ],
             couplings = {(0,0):C.GC_13})

V_9 = Vertex(name = 'V_9',
             particles = [ P.s__tilde__, P.s, P.eta, P.H ],
             color = [ 'Identity(1,2)' ],
             lorentz = [ L.FFSS1 ],
             couplings = {(0,0):C.GC_19})

V_10 = Vertex(name = 'V_10',
              particles = [ P.b__tilde__, P.b, P.eta, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS1 ],
              couplings = {(0,0):C.GC_9})

V_11 = Vertex(name = 'V_11',
              particles = [ P.d__tilde__, P.d, P.eta ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_14})

V_12 = Vertex(name = 'V_12',
              particles = [ P.s__tilde__, P.s, P.eta ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_20})

V_13 = Vertex(name = 'V_13',
              particles = [ P.b__tilde__, P.b, P.eta ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_10})

V_14 = Vertex(name = 'V_14',
              particles = [ P.e__plus__, P.e__minus__, P.eta, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFSS1 ],
              couplings = {(0,0):C.GC_15})

V_15 = Vertex(name = 'V_15',
              particles = [ P.mu__plus__, P.mu__minus__, P.eta, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFSS1 ],
              couplings = {(0,0):C.GC_17})

V_16 = Vertex(name = 'V_16',
              particles = [ P.ta__plus__, P.ta__minus__, P.eta, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFSS1 ],
              couplings = {(0,0):C.GC_23})

V_17 = Vertex(name = 'V_17',
              particles = [ P.e__plus__, P.e__minus__, P.eta ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_16})

V_18 = Vertex(name = 'V_18',
              particles = [ P.mu__plus__, P.mu__minus__, P.eta ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_18})

V_19 = Vertex(name = 'V_19',
              particles = [ P.ta__plus__, P.ta__minus__, P.eta ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_24})

V_20 = Vertex(name = 'V_20',
              particles = [ P.u__tilde__, P.u, P.eta, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS1 ],
              couplings = {(0,0):C.GC_25})

V_21 = Vertex(name = 'V_21',
              particles = [ P.c__tilde__, P.c, P.eta, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS1 ],
              couplings = {(0,0):C.GC_11})

V_22 = Vertex(name = 'V_22',
              particles = [ P.t__tilde__, P.t, P.eta, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS1 ],
              couplings = {(0,0):C.GC_21})

V_23 = Vertex(name = 'V_23',
              particles = [ P.u__tilde__, P.u, P.eta ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_26})

V_24 = Vertex(name = 'V_24',
              particles = [ P.c__tilde__, P.c, P.eta ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_12})

V_25 = Vertex(name = 'V_25',
              particles = [ P.t__tilde__, P.t, P.eta ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_22})

V_26 = Vertex(name = 'V_26',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.eta ],
              color = [ '1' ],
              lorentz = [ L.VVVS1 ],
              couplings = {(0,0):C.GC_6})

V_27 = Vertex(name = 'V_27',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.eta ],
              color = [ '1' ],
              lorentz = [ L.VVVS1 ],
              couplings = {(0,0):C.GC_4})

V_28 = Vertex(name = 'V_28',
              particles = [ P.Z, P.eta, P.H ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_28})

