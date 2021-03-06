from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LoadDimensionOperator(BaseOperator):

    ui_color = '#80BD9E'

    @apply_defaults
    def __init__(self,
                 redshift_conn_id= "",
                 sql_query= "",
                 table= "",
                 truncate= "",
                 *args, **kwargs):

        super(LoadDimensionOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id
        self.sql_query = sql_query
        self.table = table
        self.truncate = truncate
    def execute(self, context):
        self.log.info('LoadDimensionOperator not implemented yet')

        from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LoadDimensionOperator(BaseOperator):

    ui_color = '#80BD9E'

    @apply_defaults
    def __init__(self,
                 redshift_conn_id="",
                 query = '',
                 table = '',
                 truncate = False,
                 *args, **kwargs):

        super(LoadDimensionOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id
        self.sql_query = query
        self.table = table,
        self.truncate = truncate

    def execute(self, context):
        """
        Inserting data into the various dimension tables
        """
        redshift_conn = PostgresHook(self.redshift_conn_id)
        if self.truncate == True:
            redshift_conn.run(f"TRUNCATE TABLE {self.table}")
        redshift_conn.run(str(self.sql_query))
