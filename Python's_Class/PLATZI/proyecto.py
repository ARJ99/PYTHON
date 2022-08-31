#FILTRADO DE DATOS USANDO COMPRENHENSIONS,LAMBDAS.


DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
    
    #..lIST COMPRENHENSION:
    #- Filtrado de datos del diccionario. Ejemplo 1
    
    all_python_devs = [worker["name"] for worker in DATA if worker["language"]=="python"]
    
    #- Filtrado de datos del diccionario. Ejemplo 2
    all_platzi_workers = [worker["name"] for worker in DATA if worker["organization"]=="Platzi"]
    
    #- Filtrado de datos del diccionario. Ejemplo 3
    elders = [worker["name"]for worker in DATA if worker["age"]>32]

    print(all_python_devs,"\t")
    print(all_platzi_workers)
    print(elders)
  #-----------------------------------------------------------
    #.. USANDO LAMBDA
    #- Filtrado de datos del diccionario. Ejemplo 1
    """ La funcion filter nos filtra los dicc que no son > 18,
    pero nos muestra toda la info de esos dicc."""
    
    adults= list(filter(lambda worker:worker["age"]>18,DATA)) 
    
    #- Filtrado de datos del diccionario. Ejemplo 2
    """La funcion map nos filtra los dicc anteriores y nos retorna solo las personas > 18"""
    adults= list(map(lambda worker:worker["name"],adults))
    
    # for worker in adults:
    #     print(worker)

if __name__=='__main__':
    run()