from db_manager import db_manager
class url_acc(object):
  def __init__(self) -> None:
    pass
  
  @classmethod
  def modulos(self,user_id):
    db = db_manager()
    rtn = db.fetch_all(f"SELECT m.id_modulo, m.titulo, m.icono, m.enlace, m.descripcion, m.estado, p.VIEW, p.INSERT, p.UPDATE, p.DELETE FROM modulos AS m INNER JOIN permisos AS p ON m.id_modulo = p.id_modulos WHERE p.id_usuario = '{user_id}' ORDER BY p.id_modulos ASC")
    if rtn:
      data = []
      for i in rtn:
        data.append({
          "id_modulo" : i[0],
          "titulo" : i[1],
          "icono" : i[2],
          "enlace" : i[3],
          "descripcion" : i[4],
          "estado" : i[5],
          "view" : i[6],
          "insert" : i[7],
          "update" : i[8],
          "delete" : i[9]
        })
      return data
    
    