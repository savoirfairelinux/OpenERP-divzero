# -*- coding: utf-8 -*-
###############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2010 - 2014 Savoir-faire Linux
#    (<http://www.savoirfairelinux.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

{
    'name': "Div Zero",

    'summary': "Error invocation",

    'description': """
Div Zero
========

Returns the result of a division by zero.
Installs a table without error.
Calculates 1/0 on object creation.

Contributors
------------
* Sandy Carter <sandy.carter@savoirfairelinux.com>
    """,

    'author': "Savoir-faire Linux",
    'website': "http://www.savoirfairelinux.com",

    # Categories can be used to filter modules in modules listing
    # Check <odoo>/addons/base/module/module_data.xml of the full list
    'category': 'Extra Tools',
    'version': '2.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website'],
    'data': [
        'div_zero_view.xml',
    ],

    'demo': [
    ],

    'tests': [
    ],
}
