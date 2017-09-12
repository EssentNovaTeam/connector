# coding: utf-8
from openerp import api, SUPERUSER_ID
from openerp.tools import config

def set_connector_base_url(env):
    """ Add default connector.base.url when this module is newly installed or
    when we surpass this new version, set default to localhost to ensure
    that default behaviour keeps on working """

    connector_base_url = 'http://localhost:%s' % config['xmlrpc_port']

    env['ir.config_parameter'].set_param(
        'connector.base.url', connector_base_url)

def post_init_hook(cr, pool):
    env = api.Environment(cr, SUPERUSER_ID, {})

    set_connector_base_url(env)