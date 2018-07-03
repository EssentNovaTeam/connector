# coding: utf-8

from openerp import api, SUPERUSER_ID
from openerp.addons.connector.hooks import set_connector_base_url

def migrate(cr, version):
    if not version:
        return
    env = api.Environment(cr, SUPERUSER_ID, {})
    set_connector_base_url(env)