# This file was automatically created by FeynRules 2.3.32
# Mathematica version: 11.3.0 for Mac OS X x86 (64-bit) (March 7, 2018)
# Date: Wed 15 May 2019 10:43:19


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



GC_1 = Coupling(name = 'GC_1',
                value = '-(ee*complex(0,1))/3.',
                order = {'QED':1})

GC_2 = Coupling(name = 'GC_2',
                value = '(2*ee*complex(0,1))/3.',
                order = {'QED':1})

GC_3 = Coupling(name = 'GC_3',
                value = '-(ee*complex(0,1))',
                order = {'QED':1})

GC_4 = Coupling(name = 'GC_4',
                value = '-G',
                order = {'QCD':1})

GC_5 = Coupling(name = 'GC_5',
                value = 'complex(0,1)*G',
                order = {'QCD':1})

GC_6 = Coupling(name = 'GC_6',
                value = 'complex(0,1)*G**2',
                order = {'QCD':2})

GC_7 = Coupling(name = 'GC_7',
                value = '-(ee**2*complex(0,1)*Kb)/(8.*fa*cmath.pi**2)',
                order = {'NP':1,'QED':2})

GC_8 = Coupling(name = 'GC_8',
                value = '-(complex(0,1)*G**2*Kg)/(32.*fa*cmath.pi**2)',
                order = {'NP':1,'QCD':2})

GC_9 = Coupling(name = 'GC_9',
                value = '-(G**3*Kg)/(16.*fa*cmath.pi**2)',
                order = {'NP':1,'QCD':3})

GC_10 = Coupling(name = 'GC_10',
                 value = '(ee*complex(0,1)*sw)/(3.*cw)',
                 order = {'QED':1})

GC_11 = Coupling(name = 'GC_11',
                 value = '(-2*ee*complex(0,1)*sw)/(3.*cw)',
                 order = {'QED':1})

GC_12 = Coupling(name = 'GC_12',
                 value = '(ee*complex(0,1)*sw)/cw',
                 order = {'QED':1})

GC_13 = Coupling(name = 'GC_13',
                 value = '(ee**2*complex(0,1)*Kb*sw)/(8.*cw*fa*cmath.pi**2)',
                 order = {'NP':1,'QED':2})

GC_14 = Coupling(name = 'GC_14',
                 value = '-(ee**2*complex(0,1)*Kb*sw**2)/(8.*cw**2*fa*cmath.pi**2)',
                 order = {'NP':1,'QED':2})

GC_15 = Coupling(name = 'GC_15',
                 value = '-(ee**2*vev)/(4.*sw**2)',
                 order = {'QED':1})

GC_16 = Coupling(name = 'GC_16',
                 value = '-(ee**2*complex(0,1)*vev)/(4.*sw**2)',
                 order = {'QED':1})

GC_17 = Coupling(name = 'GC_17',
                 value = '(ee**2*vev)/(4.*sw**2)',
                 order = {'QED':1})

GC_18 = Coupling(name = 'GC_18',
                 value = '-(ee**2*vev)/(2.*sw)',
                 order = {'QED':1})

GC_19 = Coupling(name = 'GC_19',
                 value = '(ee**2*vev)/(2.*sw)',
                 order = {'QED':1})

GC_20 = Coupling(name = 'GC_20',
                 value = '-(ee**2*vev)/(4.*cw) - (cw*ee**2*vev)/(4.*sw**2)',
                 order = {'QED':1})

GC_21 = Coupling(name = 'GC_21',
                 value = '(ee**2*vev)/(4.*cw) - (cw*ee**2*vev)/(4.*sw**2)',
                 order = {'QED':1})

GC_22 = Coupling(name = 'GC_22',
                 value = '-(ee**2*vev)/(4.*cw) + (cw*ee**2*vev)/(4.*sw**2)',
                 order = {'QED':1})

GC_23 = Coupling(name = 'GC_23',
                 value = '(ee**2*vev)/(4.*cw) + (cw*ee**2*vev)/(4.*sw**2)',
                 order = {'QED':1})

GC_24 = Coupling(name = 'GC_24',
                 value = '-(ee**2*complex(0,1)*vev)/2. - (cw**2*ee**2*complex(0,1)*vev)/(4.*sw**2) - (ee**2*complex(0,1)*sw**2*vev)/(4.*cw**2)',
                 order = {'QED':1})

GC_25 = Coupling(name = 'GC_25',
                 value = '-(complex(0,1)*yup)',
                 order = {'PRIVATE`GetIntOrder[Eps[Index[SU2D, Ext[3]], Index[SU2D, Ext[1]]]]':1,'PRIVATE`GetIntOrder[yu[Index[Generation, Ext[1]], 1]]':1})

GC_26 = Coupling(name = 'GC_26',
                 value = '-(complex(0,1)*complexconjugate(yu(1,2)))',
                 order = {'PRIVATE`GetIntOrder[Eps[Index[SU2D, Ext[3]], Index[SU2D, Ext[1]]]]':1,'PRIVATE`GetIntOrder[yu[Index[Generation, Ext[1]], 2]]':1})

GC_27 = Coupling(name = 'GC_27',
                 value = '-(complex(0,1)*complexconjugate(yu(1,3)))',
                 order = {'PRIVATE`GetIntOrder[Eps[Index[SU2D, Ext[3]], Index[SU2D, Ext[1]]]]':1,'PRIVATE`GetIntOrder[yu[Index[Generation, Ext[1]], 3]]':1})

GC_28 = Coupling(name = 'GC_28',
                 value = '-((Cf*vev*yup)/(fa*cmath.sqrt(2)))',
                 order = {'NP':1,'QED':-1,'PRIVATE`GetIntOrder[Eps[Index[SU2D, Ext[4]], Index[SU2D, Ext[1]]]]':1,'PRIVATE`GetIntOrder[yu[Index[Generation, Ext[1]], 1]]':1})

GC_29 = Coupling(name = 'GC_29',
                 value = '-((Cf*vev*complexconjugate(yu(1,2)))/(fa*cmath.sqrt(2)))',
                 order = {'NP':1,'QED':-1,'PRIVATE`GetIntOrder[Eps[Index[SU2D, Ext[4]], Index[SU2D, Ext[1]]]]':1,'PRIVATE`GetIntOrder[yu[Index[Generation, Ext[1]], 2]]':1})

GC_30 = Coupling(name = 'GC_30',
                 value = '-((Cf*vev*complexconjugate(yu(1,3)))/(fa*cmath.sqrt(2)))',
                 order = {'NP':1,'QED':-1,'PRIVATE`GetIntOrder[Eps[Index[SU2D, Ext[4]], Index[SU2D, Ext[1]]]]':1,'PRIVATE`GetIntOrder[yu[Index[Generation, Ext[1]], 3]]':1})

GC_31 = Coupling(name = 'GC_31',
                 value = '-(ee**3*Kw)/(16.*fa*cmath.pi**2*sw**3)',
                 order = {'NP':1,'QED':3,'PRIVATE`GetIntOrder[Eps[Index[SU2W, Ext[1]], Index[SU2W, Ext[2]], Index[SU2W, Ext[3]]]]':1})

GC_32 = Coupling(name = 'GC_32',
                 value = '-(ee/sw)',
                 order = {'QED':1,'PRIVATE`GetIntOrder[Eps[Index[SU2W, Ext[1]], Index[SU2W, Ext[2]], Index[SU2W, Ext[3]]]]':1})

GC_33 = Coupling(name = 'GC_33',
                 value = '(-3*Cf**2*complex(0,1)*kt*MT**2*cmath.log(2))/(fa**2*cmath.pi**2*vev) - (3*Cf**2*complex(0,1)*kt*MT**2*cmath.log(fa))/(2.*fa**2*cmath.pi**2*vev) - (3*Cf**2*complex(0,1)*kt*MT**2*cmath.log(cmath.pi))/(2.*fa**2*cmath.pi**2*vev) + (3*Cf**2*complex(0,1)*kt*MT**2*cmath.log(MT))/(2.*fa**2*cmath.pi**2*vev)',
                 order = {'NP':2,'QED':1})

GC_34 = Coupling(name = 'GC_34',
                 value = '(3*Cf*ee*kt*MT**2*cmath.log(2))/(2.*cw*fa*cmath.pi**2*sw*vev) - (3*Cf*ee*kV*MT**2*cmath.log(2))/(2.*cw*fa*cmath.pi**2*sw*vev) + (3*Cf*ee*kt*MT**2*cmath.log(fa))/(4.*cw*fa*cmath.pi**2*sw*vev) - (3*Cf*ee*kV*MT**2*cmath.log(fa))/(4.*cw*fa*cmath.pi**2*sw*vev) + (3*Cf*ee*kt*MT**2*cmath.log(cmath.pi))/(4.*cw*fa*cmath.pi**2*sw*vev) - (3*Cf*ee*kV*MT**2*cmath.log(cmath.pi))/(4.*cw*fa*cmath.pi**2*sw*vev) - (3*Cf*ee*kt*MT**2*cmath.log(MT))/(4.*cw*fa*cmath.pi**2*sw*vev) + (3*Cf*ee*kV*MT**2*cmath.log(MT))/(4.*cw*fa*cmath.pi**2*sw*vev)',
                 order = {'NP':1,'QED':2})

GC_35 = Coupling(name = 'GC_35',
                 value = '-(ee*complex(0,1)*I2(2)*I3(3)*I4(1)*PauliSigma(a$7399,i$7399,ii))/(2.*sw)',
                 order = {'QED':1,'PRIVATE`GetIntOrder[I2[Index[SU2D, Ext[2]]]]':1,'PRIVATE`GetIntOrder[I3[Index[SU2D, Ext[3]]]]':1,'PRIVATE`GetIntOrder[I4[Index[SU2W, Ext[1]]]]':1,'PRIVATE`GetIntOrder[PauliSigma[a$7399, i$7399, ii]]':1})

GC_36 = Coupling(name = 'GC_36',
                 value = '-(ee**2*complex(0,1)*I2(3)*I3(4)*I4(1)*PauliSigma(a$7399,i$7399,ii))/(4.*cw)',
                 order = {'QED':2,'PRIVATE`GetIntOrder[I2[Index[SU2D, Ext[3]]]]':1,'PRIVATE`GetIntOrder[I3[Index[SU2D, Ext[4]]]]':1,'PRIVATE`GetIntOrder[I4[Index[SU2W, Ext[1]]]]':1,'PRIVATE`GetIntOrder[PauliSigma[a$7399, i$7399, ii]]':1})

GC_37 = Coupling(name = 'GC_37',
                 value = '(ee**2*complex(0,1)*I5(3)*I6(4)*I7(2)*PauliSigma(a$7399,i$7399,ii))/(4.*sw)',
                 order = {'QED':2,'PRIVATE`GetIntOrder[I5[Index[SU2D, Ext[3]]]]':1,'PRIVATE`GetIntOrder[I6[Index[SU2D, Ext[4]]]]':1,'PRIVATE`GetIntOrder[I7[Index[SU2W, Ext[2]]]]':1,'PRIVATE`GetIntOrder[PauliSigma[a$7399, i$7399, ii]]':1})

GC_38 = Coupling(name = 'GC_38',
                 value = '(ee**2*complex(0,1)*I2(3)*I3(4)*I4(1)*I8(2)*PauliSigma(a$7399,i$7399,1)*PauliSigma(a$7400,1,i$7400))/(2.*sw**2)',
                 order = {'QED':2,'PRIVATE`GetIntOrder[I2[Index[SU2D, Ext[3]]]]':1,'PRIVATE`GetIntOrder[I3[Index[SU2D, Ext[4]]]]':1,'PRIVATE`GetIntOrder[I4[Index[SU2W, Ext[1]]]]':1,'PRIVATE`GetIntOrder[I8[Index[SU2W, Ext[2]]]]':1,'PRIVATE`GetIntOrder[PauliSigma[a$7399, i$7399, 1]]':1,'PRIVATE`GetIntOrder[PauliSigma[a$7400, 1, i$7400]]':1})

GC_39 = Coupling(name = 'GC_39',
                 value = '(ee**2*complex(0,1)*I2(3)*I3(4)*I4(1)*I8(2)*PauliSigma(a$7399,i$7399,2)*PauliSigma(a$7400,2,i$7400))/(2.*sw**2)',
                 order = {'QED':2,'PRIVATE`GetIntOrder[I2[Index[SU2D, Ext[3]]]]':1,'PRIVATE`GetIntOrder[I3[Index[SU2D, Ext[4]]]]':1,'PRIVATE`GetIntOrder[I4[Index[SU2W, Ext[1]]]]':1,'PRIVATE`GetIntOrder[I8[Index[SU2W, Ext[2]]]]':1,'PRIVATE`GetIntOrder[PauliSigma[a$7399, i$7399, 2]]':1,'PRIVATE`GetIntOrder[PauliSigma[a$7400, 2, i$7400]]':1})

GC_40 = Coupling(name = 'GC_40',
                 value = '(ee*complex(0,1)*I2(2)*I3(3)*I4(1)*PauliSigma(a$7400,ii,i$7400))/(2.*sw)',
                 order = {'QED':1,'PRIVATE`GetIntOrder[I2[Index[SU2D, Ext[2]]]]':1,'PRIVATE`GetIntOrder[I3[Index[SU2D, Ext[3]]]]':1,'PRIVATE`GetIntOrder[I4[Index[SU2W, Ext[1]]]]':1,'PRIVATE`GetIntOrder[PauliSigma[a$7400, ii, i$7400]]':1})

GC_41 = Coupling(name = 'GC_41',
                 value = '-(ee**2*complex(0,1)*I2(3)*I3(4)*I4(1)*PauliSigma(a$7400,ii,i$7400))/(4.*cw)',
                 order = {'QED':2,'PRIVATE`GetIntOrder[I2[Index[SU2D, Ext[3]]]]':1,'PRIVATE`GetIntOrder[I3[Index[SU2D, Ext[4]]]]':1,'PRIVATE`GetIntOrder[I4[Index[SU2W, Ext[1]]]]':1,'PRIVATE`GetIntOrder[PauliSigma[a$7400, ii, i$7400]]':1})

GC_42 = Coupling(name = 'GC_42',
                 value = '(ee**2*complex(0,1)*I5(3)*I6(4)*I7(2)*PauliSigma(a$7400,ii,i$7400))/(4.*sw)',
                 order = {'QED':2,'PRIVATE`GetIntOrder[I5[Index[SU2D, Ext[3]]]]':1,'PRIVATE`GetIntOrder[I6[Index[SU2D, Ext[4]]]]':1,'PRIVATE`GetIntOrder[I7[Index[SU2W, Ext[2]]]]':1,'PRIVATE`GetIntOrder[PauliSigma[a$7400, ii, i$7400]]':1})

GC_43 = Coupling(name = 'GC_43',
                 value = '0',
                 order = {'QED':1,'PRIVATE`GetIntOrder[PauliSigma[Index[SU2W, Ext[3]], Index[SU2D, Ext[2]], Index[SU2D, Ext[1]]]]':1,'PRIVATE`GetIntOrder[P$IndexDelta[Index[Generation, Ext[1]], Index[Generation, Ext[2]]]]':1})

GC_44 = Coupling(name = 'GC_44',
                 value = '(ee*complex(0,1)*P$IndexDelta(1,2)**2)/6.',
                 order = {'QED':1,'PRIVATE`GetIntOrder[P$IndexDelta[Index[Generation, Ext[1]], Index[Generation, Ext[2]]]]':1,'PRIVATE`GetIntOrder[P$IndexDelta[Index[SU2D, Ext[1]], Index[SU2D, Ext[2]]]]':1})

GC_45 = Coupling(name = 'GC_45',
                 value = '-(ee*complex(0,1)*P$IndexDelta(1,2)**2)/2.',
                 order = {'QED':1,'PRIVATE`GetIntOrder[P$IndexDelta[Index[Generation, Ext[1]], Index[Generation, Ext[2]]]]':1,'PRIVATE`GetIntOrder[P$IndexDelta[Index[SU2D, Ext[1]], Index[SU2D, Ext[2]]]]':1})

GC_46 = Coupling(name = 'GC_46',
                 value = 'complex(0,1)*G*P$IndexDelta(1,2)**2',
                 order = {'QCD':1,'PRIVATE`GetIntOrder[P$IndexDelta[Index[Generation, Ext[1]], Index[Generation, Ext[2]]]]':1,'PRIVATE`GetIntOrder[P$IndexDelta[Index[SU2D, Ext[1]], Index[SU2D, Ext[2]]]]':1})

GC_47 = Coupling(name = 'GC_47',
                 value = '-(ee*complex(0,1)*sw*P$IndexDelta(1,2)**2)/(6.*cw)',
                 order = {'QED':1,'PRIVATE`GetIntOrder[P$IndexDelta[Index[Generation, Ext[1]], Index[Generation, Ext[2]]]]':1,'PRIVATE`GetIntOrder[P$IndexDelta[Index[SU2D, Ext[1]], Index[SU2D, Ext[2]]]]':1})

GC_48 = Coupling(name = 'GC_48',
                 value = '(ee*complex(0,1)*sw*P$IndexDelta(1,2)**2)/(2.*cw)',
                 order = {'QED':1,'PRIVATE`GetIntOrder[P$IndexDelta[Index[Generation, Ext[1]], Index[Generation, Ext[2]]]]':1,'PRIVATE`GetIntOrder[P$IndexDelta[Index[SU2D, Ext[1]], Index[SU2D, Ext[2]]]]':1})

GC_49 = Coupling(name = 'GC_49',
                 value = '-(complex(0,1)*ye*P$IndexDelta(1,3))',
                 order = {'PRIVATE`GetIntOrder[P$IndexDelta[Index[SU2D, Ext[1]], Index[SU2D, Ext[3]]]]':1,'PRIVATE`GetIntOrder[yl[Index[Generation, Ext[1]], 1]]':1})

GC_50 = Coupling(name = 'GC_50',
                 value = '-(complex(0,1)*complexconjugate(yl(1,2))*P$IndexDelta(1,3))',
                 order = {'PRIVATE`GetIntOrder[P$IndexDelta[Index[SU2D, Ext[1]], Index[SU2D, Ext[3]]]]':1,'PRIVATE`GetIntOrder[yl[Index[Generation, Ext[1]], 2]]':1})

GC_51 = Coupling(name = 'GC_51',
                 value = '-(complex(0,1)*complexconjugate(yl(1,3))*P$IndexDelta(1,3))',
                 order = {'PRIVATE`GetIntOrder[P$IndexDelta[Index[SU2D, Ext[1]], Index[SU2D, Ext[3]]]]':1,'PRIVATE`GetIntOrder[yl[Index[Generation, Ext[1]], 3]]':1})

GC_52 = Coupling(name = 'GC_52',
                 value = '-(complex(0,1)*I1(1,1)*P$IndexDelta(1,3))',
                 order = {'PRIVATE`GetIntOrder[I1[1, Index[Generation, Ext[1]]]]':1,'PRIVATE`GetIntOrder[P$IndexDelta[Index[SU2D, Ext[1]], Index[SU2D, Ext[3]]]]':1})

GC_53 = Coupling(name = 'GC_53',
                 value = '-(complex(0,1)*I1(2,1)*P$IndexDelta(1,3))',
                 order = {'PRIVATE`GetIntOrder[I1[2, Index[Generation, Ext[1]]]]':1,'PRIVATE`GetIntOrder[P$IndexDelta[Index[SU2D, Ext[1]], Index[SU2D, Ext[3]]]]':1})

GC_54 = Coupling(name = 'GC_54',
                 value = '-(complex(0,1)*I1(3,1)*P$IndexDelta(1,3))',
                 order = {'PRIVATE`GetIntOrder[I1[3, Index[Generation, Ext[1]]]]':1,'PRIVATE`GetIntOrder[P$IndexDelta[Index[SU2D, Ext[1]], Index[SU2D, Ext[3]]]]':1})

GC_55 = Coupling(name = 'GC_55',
                 value = '-((Cf*vev*ye*P$IndexDelta(1,4))/(fa*cmath.sqrt(2)))',
                 order = {'NP':1,'QED':-1,'PRIVATE`GetIntOrder[P$IndexDelta[Index[SU2D, Ext[1]], Index[SU2D, Ext[4]]]]':1,'PRIVATE`GetIntOrder[yl[Index[Generation, Ext[1]], 1]]':1})

GC_56 = Coupling(name = 'GC_56',
                 value = '-((Cf*vev*complexconjugate(yl(1,2))*P$IndexDelta(1,4))/(fa*cmath.sqrt(2)))',
                 order = {'NP':1,'QED':-1,'PRIVATE`GetIntOrder[P$IndexDelta[Index[SU2D, Ext[1]], Index[SU2D, Ext[4]]]]':1,'PRIVATE`GetIntOrder[yl[Index[Generation, Ext[1]], 2]]':1})

GC_57 = Coupling(name = 'GC_57',
                 value = '-((Cf*vev*complexconjugate(yl(1,3))*P$IndexDelta(1,4))/(fa*cmath.sqrt(2)))',
                 order = {'NP':1,'QED':-1,'PRIVATE`GetIntOrder[P$IndexDelta[Index[SU2D, Ext[1]], Index[SU2D, Ext[4]]]]':1,'PRIVATE`GetIntOrder[yl[Index[Generation, Ext[1]], 3]]':1})

GC_58 = Coupling(name = 'GC_58',
                 value = '-((Cf*vev*I1(1,1)*P$IndexDelta(1,4))/(fa*cmath.sqrt(2)))',
                 order = {'NP':1,'QED':-1,'PRIVATE`GetIntOrder[I1[1, Index[Generation, Ext[1]]]]':1,'PRIVATE`GetIntOrder[P$IndexDelta[Index[SU2D, Ext[1]], Index[SU2D, Ext[4]]]]':1})

GC_59 = Coupling(name = 'GC_59',
                 value = '-((Cf*vev*I1(2,1)*P$IndexDelta(1,4))/(fa*cmath.sqrt(2)))',
                 order = {'NP':1,'QED':-1,'PRIVATE`GetIntOrder[I1[2, Index[Generation, Ext[1]]]]':1,'PRIVATE`GetIntOrder[P$IndexDelta[Index[SU2D, Ext[1]], Index[SU2D, Ext[4]]]]':1})

GC_60 = Coupling(name = 'GC_60',
                 value = '-((Cf*vev*I1(3,1)*P$IndexDelta(1,4))/(fa*cmath.sqrt(2)))',
                 order = {'NP':1,'QED':-1,'PRIVATE`GetIntOrder[I1[3, Index[Generation, Ext[1]]]]':1,'PRIVATE`GetIntOrder[P$IndexDelta[Index[SU2D, Ext[1]], Index[SU2D, Ext[4]]]]':1})

GC_61 = Coupling(name = 'GC_61',
                 value = '-(ee*complex(0,1)*P$IndexDelta(2,3))/2.',
                 order = {'QED':1,'PRIVATE`GetIntOrder[P$IndexDelta[Index[SU2D, Ext[2]], Index[SU2D, Ext[3]]]]':1})

GC_62 = Coupling(name = 'GC_62',
                 value = '(ee*complex(0,1)*sw*P$IndexDelta(2,3))/(2.*cw)',
                 order = {'QED':1,'PRIVATE`GetIntOrder[P$IndexDelta[Index[SU2D, Ext[2]], Index[SU2D, Ext[3]]]]':1})

GC_63 = Coupling(name = 'GC_63',
                 value = '-(complex(0,1)*I9(2,1)*P$IndexDelta(2,3))',
                 order = {'PRIVATE`GetIntOrder[I9[Index[Generation, Ext[2]], 1]]':1,'PRIVATE`GetIntOrder[P$IndexDelta[Index[SU2D, Ext[2]], Index[SU2D, Ext[3]]]]':1})

GC_64 = Coupling(name = 'GC_64',
                 value = '-(complex(0,1)*I9(2,2)*P$IndexDelta(2,3))',
                 order = {'PRIVATE`GetIntOrder[I9[Index[Generation, Ext[2]], 2]]':1,'PRIVATE`GetIntOrder[P$IndexDelta[Index[SU2D, Ext[2]], Index[SU2D, Ext[3]]]]':1})

GC_65 = Coupling(name = 'GC_65',
                 value = '-(complex(0,1)*I9(2,3)*P$IndexDelta(2,3))',
                 order = {'PRIVATE`GetIntOrder[I9[Index[Generation, Ext[2]], 3]]':1,'PRIVATE`GetIntOrder[P$IndexDelta[Index[SU2D, Ext[2]], Index[SU2D, Ext[3]]]]':1})

GC_66 = Coupling(name = 'GC_66',
                 value = '-2*complex(0,1)*lam*P$IndexDelta(1,4)*P$IndexDelta(2,3)',
                 order = {'QED':2,'PRIVATE`GetIntOrder[P$IndexDelta[Index[SU2D, Ext[1]], Index[SU2D, Ext[4]]]]':1,'PRIVATE`GetIntOrder[P$IndexDelta[Index[SU2D, Ext[2]], Index[SU2D, Ext[3]]]]':1})

GC_67 = Coupling(name = 'GC_67',
                 value = '(Cf*vev*I9(2,1)*P$IndexDelta(2,4))/(fa*cmath.sqrt(2))',
                 order = {'NP':1,'QED':-1,'PRIVATE`GetIntOrder[I9[Index[Generation, Ext[2]], 1]]':1,'PRIVATE`GetIntOrder[P$IndexDelta[Index[SU2D, Ext[2]], Index[SU2D, Ext[4]]]]':1})

GC_68 = Coupling(name = 'GC_68',
                 value = '(Cf*vev*I9(2,2)*P$IndexDelta(2,4))/(fa*cmath.sqrt(2))',
                 order = {'NP':1,'QED':-1,'PRIVATE`GetIntOrder[I9[Index[Generation, Ext[2]], 2]]':1,'PRIVATE`GetIntOrder[P$IndexDelta[Index[SU2D, Ext[2]], Index[SU2D, Ext[4]]]]':1})

GC_69 = Coupling(name = 'GC_69',
                 value = '(Cf*vev*I9(2,3)*P$IndexDelta(2,4))/(fa*cmath.sqrt(2))',
                 order = {'NP':1,'QED':-1,'PRIVATE`GetIntOrder[I9[Index[Generation, Ext[2]], 3]]':1,'PRIVATE`GetIntOrder[P$IndexDelta[Index[SU2D, Ext[2]], Index[SU2D, Ext[4]]]]':1})

GC_70 = Coupling(name = 'GC_70',
                 value = '-2*complex(0,1)*lam*P$IndexDelta(1,3)*P$IndexDelta(2,4)',
                 order = {'QED':2,'PRIVATE`GetIntOrder[P$IndexDelta[Index[SU2D, Ext[1]], Index[SU2D, Ext[3]]]]':1,'PRIVATE`GetIntOrder[P$IndexDelta[Index[SU2D, Ext[2]], Index[SU2D, Ext[4]]]]':1})

GC_71 = Coupling(name = 'GC_71',
                 value = '(ee**2*complex(0,1)*P$IndexDelta(3,4))/2.',
                 order = {'QED':2,'PRIVATE`GetIntOrder[P$IndexDelta[Index[SU2D, Ext[3]], Index[SU2D, Ext[4]]]]':1})

GC_72 = Coupling(name = 'GC_72',
                 value = '-(ee**2*complex(0,1)*sw*P$IndexDelta(3,4))/(2.*cw)',
                 order = {'QED':2,'PRIVATE`GetIntOrder[P$IndexDelta[Index[SU2D, Ext[3]], Index[SU2D, Ext[4]]]]':1})

GC_73 = Coupling(name = 'GC_73',
                 value = '(ee**2*complex(0,1)*sw**2*P$IndexDelta(3,4))/(2.*cw**2)',
                 order = {'QED':2,'PRIVATE`GetIntOrder[P$IndexDelta[Index[SU2D, Ext[3]], Index[SU2D, Ext[4]]]]':1})

GC_74 = Coupling(name = 'GC_74',
                 value = '-(ee**2*complex(0,1)*Kw*P$IndexDelta(1,2))/(32.*fa*cmath.pi**2*sw**2)',
                 order = {'NP':1,'QED':2,'PRIVATE`GetIntOrder[P$IndexDelta[Index[SU2W, Ext[1]], Index[SU2W, Ext[2]]]]':1})

GC_75 = Coupling(name = 'GC_75',
                 value = '(-2*ee**2*complex(0,1)*P$IndexDelta(1,4)*P$IndexDelta(2,3))/sw**2',
                 order = {'QED':2,'PRIVATE`GetIntOrder[P$IndexDelta[Index[SU2W, Ext[1]], Index[SU2W, Ext[4]]]]':1,'PRIVATE`GetIntOrder[P$IndexDelta[Index[SU2W, Ext[2]], Index[SU2W, Ext[3]]]]':1})

GC_76 = Coupling(name = 'GC_76',
                 value = '(ee**2*complex(0,1)*P$IndexDelta(1,3)*P$IndexDelta(2,4))/sw**2',
                 order = {'QED':2,'PRIVATE`GetIntOrder[P$IndexDelta[Index[SU2W, Ext[1]], Index[SU2W, Ext[3]]]]':1,'PRIVATE`GetIntOrder[P$IndexDelta[Index[SU2W, Ext[2]], Index[SU2W, Ext[4]]]]':1})

GC_77 = Coupling(name = 'GC_77',
                 value = '(ee**2*complex(0,1)*P$IndexDelta(1,2)*P$IndexDelta(3,4))/sw**2',
                 order = {'QED':2,'PRIVATE`GetIntOrder[P$IndexDelta[Index[SU2W, Ext[1]], Index[SU2W, Ext[2]]]]':1,'PRIVATE`GetIntOrder[P$IndexDelta[Index[SU2W, Ext[3]], Index[SU2W, Ext[4]]]]':1})

GC_78 = Coupling(name = 'GC_78',
                 value = '-(complex(0,1)*P$IndexDelta(2,3)*yl(2,1))',
                 order = {'PRIVATE`GetIntOrder[P$IndexDelta[Index[SU2D, Ext[2]], Index[SU2D, Ext[3]]]]':1,'PRIVATE`GetIntOrder[yl[Index[Generation, Ext[2]], 1]]':1})

GC_79 = Coupling(name = 'GC_79',
                 value = '(Cf*vev*P$IndexDelta(2,4)*yl(2,1))/(fa*cmath.sqrt(2))',
                 order = {'NP':1,'QED':-1,'PRIVATE`GetIntOrder[P$IndexDelta[Index[SU2D, Ext[2]], Index[SU2D, Ext[4]]]]':1,'PRIVATE`GetIntOrder[yl[Index[Generation, Ext[2]], 1]]':1})

GC_80 = Coupling(name = 'GC_80',
                 value = '-(complex(0,1)*ym*P$IndexDelta(2,3))',
                 order = {'PRIVATE`GetIntOrder[P$IndexDelta[Index[SU2D, Ext[2]], Index[SU2D, Ext[3]]]]':1,'PRIVATE`GetIntOrder[yl[Index[Generation, Ext[2]], 2]]':1})

GC_81 = Coupling(name = 'GC_81',
                 value = '(Cf*vev*ym*P$IndexDelta(2,4))/(fa*cmath.sqrt(2))',
                 order = {'NP':1,'QED':-1,'PRIVATE`GetIntOrder[P$IndexDelta[Index[SU2D, Ext[2]], Index[SU2D, Ext[4]]]]':1,'PRIVATE`GetIntOrder[yl[Index[Generation, Ext[2]], 2]]':1})

GC_82 = Coupling(name = 'GC_82',
                 value = '-(complex(0,1)*P$IndexDelta(2,3)*yl(2,3))',
                 order = {'PRIVATE`GetIntOrder[P$IndexDelta[Index[SU2D, Ext[2]], Index[SU2D, Ext[3]]]]':1,'PRIVATE`GetIntOrder[yl[Index[Generation, Ext[2]], 3]]':1})

GC_83 = Coupling(name = 'GC_83',
                 value = '(Cf*vev*P$IndexDelta(2,4)*yl(2,3))/(fa*cmath.sqrt(2))',
                 order = {'NP':1,'QED':-1,'PRIVATE`GetIntOrder[P$IndexDelta[Index[SU2D, Ext[2]], Index[SU2D, Ext[4]]]]':1,'PRIVATE`GetIntOrder[yl[Index[Generation, Ext[2]], 3]]':1})

GC_84 = Coupling(name = 'GC_84',
                 value = '-(complex(0,1)*yu(2,1))',
                 order = {'PRIVATE`GetIntOrder[Eps[Index[SU2D, Ext[3]], Index[SU2D, Ext[2]]]]':1,'PRIVATE`GetIntOrder[yu[Index[Generation, Ext[2]], 1]]':1})

GC_85 = Coupling(name = 'GC_85',
                 value = '(Cf*vev*yu(2,1))/(fa*cmath.sqrt(2))',
                 order = {'NP':1,'QED':-1,'PRIVATE`GetIntOrder[Eps[Index[SU2D, Ext[4]], Index[SU2D, Ext[2]]]]':1,'PRIVATE`GetIntOrder[yu[Index[Generation, Ext[2]], 1]]':1})

GC_86 = Coupling(name = 'GC_86',
                 value = '-(complex(0,1)*yc)',
                 order = {'PRIVATE`GetIntOrder[Eps[Index[SU2D, Ext[3]], Index[SU2D, Ext[2]]]]':1,'PRIVATE`GetIntOrder[yu[Index[Generation, Ext[2]], 2]]':1})

GC_87 = Coupling(name = 'GC_87',
                 value = '(Cf*vev*yc)/(fa*cmath.sqrt(2))',
                 order = {'NP':1,'QED':-1,'PRIVATE`GetIntOrder[Eps[Index[SU2D, Ext[4]], Index[SU2D, Ext[2]]]]':1,'PRIVATE`GetIntOrder[yu[Index[Generation, Ext[2]], 2]]':1})

GC_88 = Coupling(name = 'GC_88',
                 value = '-(complex(0,1)*yu(2,3))',
                 order = {'PRIVATE`GetIntOrder[Eps[Index[SU2D, Ext[3]], Index[SU2D, Ext[2]]]]':1,'PRIVATE`GetIntOrder[yu[Index[Generation, Ext[2]], 3]]':1})

GC_89 = Coupling(name = 'GC_89',
                 value = '(Cf*vev*yu(2,3))/(fa*cmath.sqrt(2))',
                 order = {'NP':1,'QED':-1,'PRIVATE`GetIntOrder[Eps[Index[SU2D, Ext[4]], Index[SU2D, Ext[2]]]]':1,'PRIVATE`GetIntOrder[yu[Index[Generation, Ext[2]], 3]]':1})

