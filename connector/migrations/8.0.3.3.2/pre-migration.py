# coding: utf-8
import logging


def migrate(cr, version):
    if not version:
        return
    cr.execute(
        """
        SELECT count(attname) FROM pg_attribute
        WHERE attrelid = (
            SELECT oid FROM pg_class WHERE relname = 'queue_job')
        AND attname = 'db_load'""")
    if cr.fetchone()[0]:
        logging.getLogger(__name__).info(
            "Column db_load already found in table queue_job")
        return
    logging.getLogger(__name__).info(
        "Preemptively add column db_load to prevent its computation for "
        "every job in the system.")
    cr.execute("ALTER TABLE queue_job ADD COLUMN db_load FLOAT")
