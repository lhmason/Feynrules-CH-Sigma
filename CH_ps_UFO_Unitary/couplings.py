# This file was automatically created by FeynRules 2.3.32
# Mathematica version: 11.3.0 for Mac OS X x86 (64-bit) (March 7, 2018)
# Date: Sat 4 May 2019 15:32:53


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



GC_1 = Coupling(name = 'GC_1',
                value = '-(ee**2*complex(0,1)*Kb)/(4.*fa*cmath.pi**2) - (ee**2*complex(0,1)*Kw)/(4.*fa*cmath.pi**2)',
                order = {'NP':1,'QED':2})

GC_2 = Coupling(name = 'GC_2',
                value = '-(complex(0,1)*G**2*Kg)/(16.*fa*cmath.pi**2)',
                order = {'NP':1,'QCD':2})

GC_3 = Coupling(name = 'GC_3',
                value = '-(G**3*Kg)/(8.*fa*cmath.pi**2)',
                order = {'NP':1,'QCD':3})

GC_4 = Coupling(name = 'GC_4',
                value = '(cw*ee**3*complex(0,1)*Kw)/(2.*fa*cmath.pi**2*sw**3)',
                order = {'NP':1,'QED':3})

GC_5 = Coupling(name = 'GC_5',
                value = '-(ee**2*complex(0,1)*Kw)/(4.*fa*cmath.pi**2*sw**2)',
                order = {'NP':1,'QED':2})

GC_6 = Coupling(name = 'GC_6',
                value = '(ee**3*complex(0,1)*Kw)/(2.*fa*cmath.pi**2*sw**2)',
                order = {'NP':1,'QED':3})

GC_7 = Coupling(name = 'GC_7',
                value = '-(cw*ee**2*complex(0,1)*Kw)/(4.*fa*cmath.pi**2*sw) + (ee**2*complex(0,1)*Kb*sw)/(4.*cw*fa*cmath.pi**2)',
                order = {'NP':1,'QED':2})

GC_8 = Coupling(name = 'GC_8',
                value = '-(cw**2*ee**2*complex(0,1)*Kw)/(4.*fa*cmath.pi**2*sw**2) - (ee**2*complex(0,1)*Kb*sw**2)/(4.*cw**2*fa*cmath.pi**2)',
                order = {'NP':1,'QED':2})

GC_9 = Coupling(name = 'GC_9',
                value = '-(Cf*vev*yb)/(2.*fa)',
                order = {'NP':1})

GC_10 = Coupling(name = 'GC_10',
                 value = '-(Cf*vev**2*yb)/(2.*fa)',
                 order = {'NP':1,'QED':-1})

GC_11 = Coupling(name = 'GC_11',
                 value = '-(Cf*vev*yc)/(2.*fa)',
                 order = {'NP':1})

GC_12 = Coupling(name = 'GC_12',
                 value = '-(Cf*vev**2*yc)/(2.*fa)',
                 order = {'NP':1,'QED':-1})

GC_13 = Coupling(name = 'GC_13',
                 value = '-(Cf*vev*ydo)/(2.*fa)',
                 order = {'NP':1})

GC_14 = Coupling(name = 'GC_14',
                 value = '-(Cf*vev**2*ydo)/(2.*fa)',
                 order = {'NP':1,'QED':-1})

GC_15 = Coupling(name = 'GC_15',
                 value = '-(Cf*vev*ye)/(2.*fa)',
                 order = {'NP':1})

GC_16 = Coupling(name = 'GC_16',
                 value = '-(Cf*vev**2*ye)/(2.*fa)',
                 order = {'NP':1,'QED':-1})

GC_17 = Coupling(name = 'GC_17',
                 value = '-(Cf*vev*ym)/(2.*fa)',
                 order = {'NP':1})

GC_18 = Coupling(name = 'GC_18',
                 value = '-(Cf*vev**2*ym)/(2.*fa)',
                 order = {'NP':1,'QED':-1})

GC_19 = Coupling(name = 'GC_19',
                 value = '-(Cf*vev*ys)/(2.*fa)',
                 order = {'NP':1})

GC_20 = Coupling(name = 'GC_20',
                 value = '-(Cf*vev**2*ys)/(2.*fa)',
                 order = {'NP':1,'QED':-1})

GC_21 = Coupling(name = 'GC_21',
                 value = '-(Cf*vev*yt)/(2.*fa)',
                 order = {'NP':1})

GC_22 = Coupling(name = 'GC_22',
                 value = '-(Cf*vev**2*yt)/(2.*fa)',
                 order = {'NP':1,'QED':-1})

GC_23 = Coupling(name = 'GC_23',
                 value = '-(Cf*vev*ytau)/(2.*fa)',
                 order = {'NP':1})

GC_24 = Coupling(name = 'GC_24',
                 value = '-(Cf*vev**2*ytau)/(2.*fa)',
                 order = {'NP':1,'QED':-1})

GC_25 = Coupling(name = 'GC_25',
                 value = '-(Cf*vev*yup)/(2.*fa)',
                 order = {'NP':1})

GC_26 = Coupling(name = 'GC_26',
                 value = '-(Cf*vev**2*yup)/(2.*fa)',
                 order = {'NP':1,'QED':-1})

GC_27 = Coupling(name = 'GC_27',
                 value = '(-3*Cf**2*complex(0,1)*kt*MT**2*cmath.log(2))/(fa**2*cmath.pi**2*vev) - (3*Cf**2*complex(0,1)*kt*MT**2*cmath.log(fa))/(2.*fa**2*cmath.pi**2*vev) - (3*Cf**2*complex(0,1)*kt*MT**2*cmath.log(cmath.pi))/(2.*fa**2*cmath.pi**2*vev) + (3*Cf**2*complex(0,1)*kt*MT**2*cmath.log(MT))/(2.*fa**2*cmath.pi**2*vev)',
                 order = {'NP':2,'QED':1})

GC_28 = Coupling(name = 'GC_28',
                 value = '(-3*Cf*ee*kt*MT**2*cmath.log(2))/(2.*cw*fa*cmath.pi**2*sw*vev) + (3*Cf*ee*kV*MT**2*cmath.log(2))/(2.*cw*fa*cmath.pi**2*sw*vev) - (3*Cf*ee*kt*MT**2*cmath.log(fa))/(4.*cw*fa*cmath.pi**2*sw*vev) + (3*Cf*ee*kV*MT**2*cmath.log(fa))/(4.*cw*fa*cmath.pi**2*sw*vev) - (3*Cf*ee*kt*MT**2*cmath.log(cmath.pi))/(4.*cw*fa*cmath.pi**2*sw*vev) + (3*Cf*ee*kV*MT**2*cmath.log(cmath.pi))/(4.*cw*fa*cmath.pi**2*sw*vev) + (3*Cf*ee*kt*MT**2*cmath.log(MT))/(4.*cw*fa*cmath.pi**2*sw*vev) - (3*Cf*ee*kV*MT**2*cmath.log(MT))/(4.*cw*fa*cmath.pi**2*sw*vev)',
                 order = {'NP':1,'QED':2})

