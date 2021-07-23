from object_library import all_form_factors, FormFactor
  
from function_library import complexconjugate, re, im, csc, sec, acsc, asec#, HeavTheta

#formfa = lambda t,b : (2/3)**2 loopq(t) + (1/3)**2 loopq(b) 

#formfg = lambda t,b : loopq(t) + loopq(b) 

#loopq = lambda q : - qtau(MT) (ArcTan[Sqrt[ 1/qloop(MT) ])**2 if qloop(MT) > 1 else qloop(MT)/4 (Log[ (1 + Sqrt[1 - qloop(MT) ]) / (1 - Sqrt[1 - qloop(MT) ]) ])**2

#qtau = lambda mf : 4 mf**2 / Mpsa**2


Fgg = FormFactor(name = 'Fgg',
                 type = 'real',
                 value = 'Cf' )
                                    
Faa = FormFactor(name = 'Faa',
                 type = 'real',
                 value = '3 Cf' )
