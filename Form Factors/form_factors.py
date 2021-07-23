from object_library import all_form_factors, FormFactor
import cmath 
from function_library import complexconjugate, re, im, csc, sec, acsc, asec, theta_function

Fgg = FormFactor(name = 'Fgg',
                 type = 'real',
                 #value = (lambda t,b: 'Kg - Cf * ' + t + ' * (cmath.asin(1/cmath.sqrt('+t+')))**2 + Cf * ' + b +'/4. * ( cmath.log( (1 + cmath.sqrt(1 - '+ b +' )) / (1 - cmath.sqrt(1 - ' + b + '))) - complex(0.0,1.0) * cmath.pi )**2')('taut','taub')   )
                 #value = (lambda t: 'Kg - Cf * ' + t + ' * (cmath.asin(1/cmath.sqrt('+t+')))**2 ')('taut')   )
                 value = '1'   )
                 #value = 'complex(0.0,1.0)'   )

Faa = FormFactor(name = 'Faa',
                 type = 'real',
                 #value = (lambda t,b: 'Kaa - Cf * 3 * (2/3)**2 * ' + t + ' * (cmath.asin(1/cmath.sqrt('+t+')))**2 + Cf * ' + b +'/4.* 3 * (1/3)**2 * ( cmath.log( (1 + cmath.sqrt(1 - '+ b +' )) / (1 - cmath.sqrt(1 - ' + b + '))) -  complex(0.0,1.0) * cmath.pi)**2')('taut','taub')   )
                 #value = (lambda t: 'Kaa - Cf *(2/3)**2 * ' + t + ' * (cmath.asin(1/cmath.sqrt('+t+')))**2 ')('taut')   )
                 value = '1'   )
                 #value = '1 + complex(0.0,1.0)'   )


