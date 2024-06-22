import mesop as me
import mesop.labs as mel
import duckdb


con = duckdb.connect("md:")

# print(con.sql("SELECT DISTINCT Cohort FROM experiments_rpe_2023_q4.Experiments").show())

@me.page(
  security_policy=me.SecurityPolicy(
    allowed_iframe_parents=None
  ),
  path="/sqlchat",
  title="SQL Chat Demo",
)

def app():
  mel.text_to_text(
    execute_sql,
    title="DuckDB SQL Chat",
  )

def execute_sql(sql_query):
    return str(con.sql(sql_query).show())