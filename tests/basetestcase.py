# -*- coding: utf-8 -*-
from openerp import SUPERUSER_ID
from openerp.tests.common import TransactionCase


class BaseTestCase(TransactionCase):
    def testA(self):
        cr, uid = self.cr, self.uid

	test = True

	self.assertEqual(test, True, "TEST OK")
