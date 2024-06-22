import mesop as me
import mesop.labs as mel
import duckdb


con = duckdb.connect("md:")

print(con.sql("SELECT DISTINCT Cohort FROM experiments_rpe_2023_q4.Experiments").show())

@me.page(
  security_policy=me.SecurityPolicy(
    allowed_iframe_parents=None
  ),
  path="/sqlchat",
  title="SQL Chat Demo",
)
def page():
  mel.chat(execute_sql, title="DuckDB SQL Chat", bot_user="SQL")


def execute_sql(sql_query: str, history: list[mel.ChatMessage]):
    yield con.sql(sql_query).show()
    #yield "constant_output"