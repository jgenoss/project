from db_manager import db_manager
class url_acc(object):
  def __init__(self) -> None:
    pass
  
  @classmethod
  def modulos(self,user_id):
    db = db_manager()
    rtn = db.fetch_all(f"""
        SELECT
        modulos.* 
      FROM
        roles AS r
        INNER JOIN usuario AS u ON r.id_rol = u.id_rol
        INNER JOIN roles_permisos_modulos ON r.id_rol = roles_permisos_modulos.id_rol
        INNER JOIN modulos ON roles_permisos_modulos.id_modulo = modulos.id_modulo
        INNER JOIN permisos ON roles_permisos_modulos.id_permiso = permisos.id_permiso 
      WHERE
        u.id = {user_id} 
      GROUP BY
        modulos.id_modulo""")
    if rtn:
      data = []
      for i in rtn:
        data.append({
          "id_modulo" : i[0],
          "titulo" : i[1],
          "icono" : i[2],
          "enlace" : i[3],
          "descripcion" : i[4],
          "estado" : i[5]
        })
      return data
    
    