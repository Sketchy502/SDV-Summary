from sdv import app

sql_escape = app.sqlesc

GET_TODO_TASKS = """
UPDATE 
  todo 
SET 
  currently_processing={sql_escape} 
WHERE 
  id=(
    SELECT 
      id 
    FROM 
      todo 
    WHERE 
      task={sql_escape}
      AND 
      currently_processing IS NOT TRUE 
    LIMIT 1
  )
RETURNING *;
""".format(
    sql_escape=sql_escape
)

DELETE_TASK = """
  DELETE FROM 
    todo 
  WHERE
    id={sql_escape};
""".format(
    sql_escape=sql_escape
)

UPDATE_PLAYER_IMAGE_URLS = """
  UPDATE 
    playerinfo 
  SET
    farm_url={sql_escape},
    avatar_url={sql_escape},
    portrait_url={sql_escape},
    map_url={sql_escape},
    thumb_url={sql_escape},
    base_path={sql_escape}
  WHERE 
    id={sql_escape};
""".format(
    sql_escape=sql_escape
)

UPDATE_FARMHANDS = """
    UPDATE playerinfo SET farmhands = {sql_escape} WHERE id = {sql_escape}; 
""".format(
    sql_escape=sql_escape
)
