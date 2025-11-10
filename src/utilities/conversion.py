from jpype import JClass # type: ignore

def py_dict_to_java_map(py_dict, java_map_name):
    Map = JClass(f"java.util.{java_map_name}")
    java_map = Map()
    
    for k, v in py_dict.items():
        java_map.put(k, v)
        
    return java_map
    