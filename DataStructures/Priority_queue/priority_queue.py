
from DataStructures.Priority_queue import pq_entry as pq
from DataStructures.List import array_list as al

def new_heap(is_min_pq=True):
    """Crea un cola de prioridad indexada orientada a menor o mayor dependiendo del valor de is_min_pq. Se crea una cola de prioridad con los siguientes atributos:
        elements: Lista de elementos. Se inicializa como una lista vacia de tipo array_list.
        size: Tamaño de la cola de prioridad. Se inicializa en 0.
        cmp_function: La funcion de comparacion. Si es una cola de prioridad orientada a menor is_min_pq = True, se inicializa con la funcion default_compare_lower_value. Si es una cola de prioridad orientada a mayor is_min_pq = False, se inicializa con la funcion default_compare_higher_value.

    Args:
        is_min_pq (bool, optional): Indica si la cola de prioridad es orientada a menor o mayor. Por defecto es True.
    
    Returns:
        my_heap(priority_queue): Una nueva cola de prioridad indexada
    """
    my_heap = {"elements" : al.new_list(),
               "size" : 0,
               "cmp_function" : default_compare_lower_value if is_min_pq else default_compare_higher_value
    }
    
    al.add_first(my_heap["elements"], None)
    
    return my_heap

def default_compare_higher_value(father_node, child_node):
    """Función de comparación por defecto para el heap orientado a mayor. Compara la prioridad priority de los nodos father_node y child_node.
       Si el nodo padre tiene mayor o igual prioridad que el nodo hijo, retorna True. En caso contrario, retorna False.

    Args:
        father_node (pq_entry): El nodo padre
        child_node (pq_entry): El nodo hijo

    Returns:
        bool: True si el nodo padre tiene mayor prioridad que el nodo hijo. False en caso contrario.
    """
    if pq.get_priority(father_node) >= pq.get_priority(child_node):
        return True
    return False

def default_compare_lower_value(father_node, child_node):
    """Función de comparación por defecto para el heap orientado a menor. Compara la prioridad priority de los nodos father_node y child_node.
       Si el nodo padre tiene menor o igual prioridad que el nodo hijo, retorna True. En caso contrario, retorna False.

    Args:
        father_node (pq_entry): El nodo padre
        child_node (pq_entry): El nodo hijo

    Returns:
        bool: True si el nodo padre tiene menor prioridad que el nodo hijo. False en caso contrario.
    """
    if pq.get_priority(father_node) <= pq.get_priority(child_node):
        return True
    return False

def priority(my_heap, parent, child):
    """Indica si el parent tiene mayor prioridad que child.

    Args:
        my_heap (priority_queue): El heap a revisar
        parent (any): El elemento padre
        child (any): El elemento hijo a comparar
        
    Returns:
        bool: True si el parent tiene mayor prioridad que el child. False en caso contrario.
    """
    return my_heap["cmp_function"](parent, child)

def insert(my_heap, priority, value):
    """Agrega una nueva entrada prioridad-valor al heap. Inserta la prioridad priority con valor value en el heap al final de la lista de elementos y luego se hace swim para dejar el elemento en la posición correcta.

    Args:
        my_heap (priority_queue): El heap sobre el cual se realiza la operación
        priority (int): La prioridad a insertar
        value (any): El valor de la nueva entrada
    
    Returns:
        my_heap (priority_queue): El heap con la nueva entrada insertada
    """
    entry = pq.new_pq_entry(priority, value)
    
    if is_empty(my_heap):
        al.add_last(my_heap["elements"], entry)
        my_heap["size"] += 1
        return my_heap
    
    al.add_last(my_heap["elements"], entry)
    swim(my_heap, al.size(my_heap["elements"])-1)
    my_heap["size"] += 1
    return my_heap

def swim(my_heap, pos):
    """Deja en la posición correcta un elemento ubicado en la última posición del heap. Se realiza un recorrido hacia arriba en el heap,
       comparando el elemento con su padre. Si el elemento tiene mayor prioridad que su padre, se intercambian los elementos y se continúa el recorrido hacia arriba.

    Args:
        my_heap (priority_queue): El heap sobre el cual se realiza la operación
        pos (int): La posición del elemento a revisar
    
    Returns:
        my_heap (priority_queue): El heap con la nueva entrada insertada en la posicion correcta
    """
    lista = my_heap["elements"]
    
    while pos>1:
        parent = pos//2
        if priority(my_heap, al.get_element(lista, parent), al.get_element(lista, pos)):
            break
        al.exchange(lista, parent, pos)
        pos=parent
    
    return my_heap

def size(my_heap):
    """Obtiene el número de elementos en el heap.

    Args:
        my_heap (priority_queue): El heap del cual se quiere saber la cantidad de elementos
    
    Returns:
        int: El número de elementos
    """
    return my_heap["size"]

def is_empty(my_heap):
    """Verifica si la cola de prioridad está vacía.Retorna True si el heap está vacío, False en caso contrario. Si el heap tiene un tamaño de 0, se considera vacío.

    Args:
        my_heap (priority_queue): El heap del cual se quiere saber si está vacío
        
    Returns:
        bool: True si el heap está vacío, False en caso contrario.
    """
    return size(my_heap) == 0

def get_first_priority(my_heap):
    """Obtiene el elemento de mayor prioridad del heap sin eliminarlo.
       Retorna el primer elemento del heap, es decir el elemento con mayor prioridad sin eliminarlo.

    Args:
        my_heap (priority_queue): El heap del cual se quiere obtener el primer elemento
        
    Returns:
        any: El value asociada elemento de mayor prioridad. Si el heap está vacío, retorna None.
    """
    if is_empty(my_heap):
        return None  # O lanzar excepción

    # Siempre retorna el valor en la raíz, que está en la posición 1
    first_entry = al.get_element(my_heap["elements"], 1)
    return pq.get_value(first_entry)

def remove(my_heap):
    """Retorna el elemento del heap de mayor prioridad y lo elimina. Se reemplaza el primer elemento del heap por el último elemento y se hace sink para dejar el elemento en la posición correcta.

    Args:
        my_heap (priority_queue): El heap a revisar
        
    Returns:
        any: value del elemento de mayor prioridad. Si el heap está vacío, retorna None.
    """
    if is_empty(my_heap):
        return None
    
    # 1. Obtener el valor de mayor prioridad (raíz en posición 1)
    first_entry = al.get_element(my_heap["elements"], 1)
    value_to_return = pq.get_value(first_entry)
    
    # 2. Obtener el último elemento
    last_pos = al.size(my_heap["elements"]) - 1
    
    # 3. Intercambiar raíz con último elemento
    al.exchange(my_heap["elements"], 1, last_pos)
    
    # 4. Eliminar el último elemento (que ahora es la raíz original)
    al.delete_element(my_heap["elements"], last_pos)
    my_heap["size"] -= 1
    
    # 5. Si el heap no está vacío, hacer sink desde la raíz
    if not is_empty(my_heap):
        sink(my_heap, 1)
    
    return value_to_return

def sink(my_heap, pos):
    """Deja en la posición correcta un elemento ubicado en la raíz del heap

    Args:
        my_heap (priority_queue): El heap sobre el cual se realiza la operación
        pos (int): La posición del elemento a revisar
    
    Returns:
        my_heap (priority_queue): El heap con la poscicion correcta
    """
    lista = my_heap["elements"]
    size_heap = al.size(lista) - 1  # -1 porque el índice 0 está vacío
    
    while pos * 2 <= size_heap:  # Mientras tenga al menos un hijo
        child_1 = pos * 2
        child_2 = pos * 2 + 1
        
        # Encontrar el hijo con mayor prioridad (menor en min-heap)
        if child_2 <= size_heap:
            # Tiene ambos hijos, elegir el de mayor prioridad
            if priority(my_heap, al.get_element(lista, child_1), al.get_element(lista, child_2)):
                priority_child = child_1
            else:
                priority_child = child_2
        else:
            # Solo tiene hijo izquierdo
            priority_child = child_1
        
        # Comparar padre con el hijo de mayor prioridad
        if priority(my_heap, al.get_element(lista, pos), al.get_element(lista, priority_child)):
            break  # Ya está en la posición correcta
        
        # Intercambiar y continuar desde la nueva posición
        al.exchange(lista, pos, priority_child)
        pos = priority_child
    
    return my_heap

def is_present_value(my_heap, value):
    """Busca si ya existe una entrada en el heap cuyo valor sea el value. Si existe se retorna la posición de la entrada que contiene el value. Si No existe se retorna el valor -1.

    Args:
        my_heap (priority_queue): El heap a revisar
        value (any): La parte valor de la entrada del heap que se esta buscando
    
    Returns:
        int: Posición de la entrada si value está presente, -1 en caso contrario.
    """
    for i in range(1, al.size(my_heap["elements"])):
        if pq.get_value(al.get_element(my_heap["elements"], i)) == value:
            return i
    
    return -1

def contains(my_heap, value):
    """Busca si ya existe una entrada en el heap cuyo valor sea el value. Si existe se retorna True. En caso contrario, False.

    Args:
        my_heap (priority_queue): El heap a revisar
        value (any): La parte valor de la entrada del heap que se esta buscando
    
    Returns:
        bool: Si existe se retorna True. En caso contrario, False.
    """
    return is_present_value(my_heap, value) != -1

def improve_priority(my_heap, priority, value):
    """Mejorar la prioridad de la pq_entry que tenga el value dado. Funciona para MinPQ y MaxPQ.

    Args:
        my_heap (priority_queue): El heap a revisar
        priority (int): La nueva prioridad de la pq_entry del heap. Esta prioridad debe ser mejor que la actual.
        value (any): El value de referencia de la pq_entry del heap que se quiere actualizar
        
    Returns:
        my_heap (priority_queue): El heap con la nueva pq_entry actualizada
    """
    value_pos = is_present_value(my_heap, value)
    if value_pos == -1:
        return my_heap
    
    current_entry = al.get_element(my_heap["elements"], value_pos)
    new_entry = pq.new_pq_entry(priority, value)
    
    if not my_heap["cmp_function"](new_entry, current_entry):
        return my_heap
    
    pq.set_priority(current_entry, priority)
    
    swim(my_heap, value_pos)
    
    return my_heap
    

