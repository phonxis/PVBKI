from django.test import TestCase

from pvbki.utils import PvbkiService


class ParseStatementTest(TestCase):

    def setUp(self):
        ps = PvbkiService()
        ps.get_statement_report('1928100592')
        self.subj = ps.subject_object

    def test_full(self):
        self.assertEquals(
            self.subj.requestid,
            '1928100592'
        )
        self.assertEquals(
            self.subj.pvbki_addresses.all()[0].type_id,
            1
        )
        self.assertEquals(
            self.subj.pvbki_communications.all()[0].value,
            '+380667808080'
        )
        self.assertEquals(
            self.subj.pvbki_communications.all()[1].value,
            '+380668900077'
        )

        self.assertEquals(
            self.subj.pvbki_contracts.all()[0].currency,
            'UAH'
        )
        self.assertEquals(
            self.subj.pvbki_contracts.all()[1].type,
            'instalment'
        )

        self.assertEquals(
            self.subj.pvbki_events.all()[0].provider,
            1
        )
        self.assertEquals(
            self.subj.pvbki_events.all()[3].event,
            'request'
        )


class ParseStatementPlusTest(TestCase):

    def setUp(self):
        ps = PvbkiService()
        ps.get_statementplus_report('1928100592')
        self.subj = ps.subject_object

    def test_full(self):
        self.assertEquals(
            self.subj.requestid,
            '1928100592'
        )
        self.assertEquals(
            self.subj.pvbki_addresses.all()[0].type_id,
            1
        )
        self.assertEquals(
            self.subj.pvbki_communications.all()[0].value,
            '+380667808080'
        )
        self.assertEquals(
            self.subj.pvbki_communications.all()[1].value,
            '+380668900077'
        )

        self.assertEquals(
            self.subj.pvbki_contracts.all()[0].currency,
            'UAH'
        )
        self.assertEquals(
            self.subj.pvbki_contracts.all()[1].type,
            'instalment'
        )

        self.assertEquals(
            self.subj.pvbki_events.all()[0].provider,
            1
        )
        self.assertEquals(
            self.subj.pvbki_events.all()[3].event,
            'request'
        )

        self.assertEquals(
            self.subj.pvbki_scoring.all()[0].degree,
            'B+'
        )
        self.assertEquals(
            self.subj.pvbki_scoring.all()[0].score,
            555
        )


class ParseStatement2017Test(TestCase):

    def setUp(self):
        ps = PvbkiService()
        ps.get_statement2017_report('1928100592')
        self.subj = ps.subject_object

    def test_full(self):
        self.assertEquals(
            self.subj.requestid,
            '1928100592'
        )
        self.assertEquals(
            self.subj.pvbki_addresses.all()[0].type_id,
            1
        )
        self.assertEquals(
            self.subj.pvbki_communications.all()[0].value,
            '+380667808080'
        )
        self.assertEquals(
            self.subj.pvbki_communications.all()[1].value,
            '+380668900077'
        )

        self.assertEquals(
            self.subj.pvbki_contracts.all()[0].currency,
            'UAH'
        )
        self.assertEquals(
            self.subj.pvbki_contracts.all()[1].type,
            'instalment'
        )

        self.assertEquals(
            self.subj.pvbki_events.all()[0].provider,
            1
        )
        self.assertEquals(
            self.subj.pvbki_events.all()[3].event,
            'request'
        )
        self.assertEquals(
            self.subj.pvbki_scoring.all()[0].degree,
            'B+'
        )
        self.assertEquals(
            self.subj.pvbki_scoring.all()[0].score,
            588
        )

        self.assertEquals(
            self.subj.pvbki_erb.all()[0].data_register,
            4
        )
        self.assertEquals(
            self.subj.pvbki_edr.all()[0].state,
            '200'
        )
