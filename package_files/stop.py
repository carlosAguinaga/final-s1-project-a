

from os import replace


conjugadas = ['ajena', 'ajeno', 'ajenas', 'ajenos', 'algún', 'alguna', 'algunas', 'alguno', 'algunos', 'allá', 'allí',
              'aquella', 'aquello', 'aquellas', 'aquellos', 'cierto', 'ciertos', 'cierta', 'ciertas', 'cualquier', 'cualquiera', 
              'cuanto', 'cuantos', 'cuanta', 'cuantas', 'demasiada', 'demasiadas', 'demasiado', 'demasiados',
              'ella', 'ellas', 'ello', 'ellos', 'era', 'eras', 'esa', 'esas', 'ese', 'eso', 'esos', 'esta', 'estas'
              'este', 'esto', 'estos', 'hace', 'haces', 'junto', 'juntos', 'la', 'las', 'lo', 'los', 'mi', 'mis', 'mía', 'mías'
              'mío', 'míos', 'misma', 'mismas', 'mismo', 'mismos', 'mucha', 'muchas', 'muchísima', 'muchísimas', 'muchísimo', 'muchísimos',
              'mucho', 'muchos', 'ningún', 'ninguna', 'ninguno', 'nosotras', 'nosotros', 'nuestra', 'nuestras', 'nuestro', 'nuestros',
              'otra', 'otras', 'otro', 'otros', 'poca', 'pocas', 'poco', 'pocos', 'podría', 'podrías', 'puede', 'pueden', 'quién', 'quiénes',
              'quizá', 'quizás', 'sabe', 'sabes', 'saben', 'su', 'sus', 'suya', 'suyas', 'suyo', 'suyos', 'tal', 'tales',
              'tanta', 'tantas', 'tanto', 'tantos', 'toda', 'todas', 'todo', 'todos', 'trabaja', 'trabajo', 'tuya', 'tuyas', 'tuyo', 'tuyos',
              'un', 'una', 'unas', 'uno', 'unos', 'usa', 'usas', 'usted', 'ustedes', 'va', 'van', 'varias', 'varios', 'vosotras', 'vosotros',
              'vuestros']



sw = []

def stop_words(namefile:str) -> list:

    with open(namefile, 'r') as words:
        lineas = words.readlines()
        lineas = [i.replace('\n', '') for i in lineas if '/' not in i]
        lineas = [*lineas, *conjugadas]

        return lineas

   

    # print(sw)
