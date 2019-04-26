import binascii
import re

import requests
import xmltodict

from django.apps import apps
from django.conf import settings as django_settings
from django.template.loader import render_to_string


class PvbkiService:

    def __init__(self, *args, **kwargs):
        self.subject_object = None
        # Test domain: test.pvbki.com
        self.domain = 'secure.pvbki.com'  # Prod domain
        self.passed_keys = ['@protection', '@generated', '@powered']

    def get_key(self):
        """
        Convert list of digits:
            [79, 33, 61, 42, 37, 42, 51, 31,
             31, 66, 54, 31, 83, 63, 43, 51,
             51, 33, 54, 31, 111,79, 111,98,
             33, 37,105, 53, 31, 79, 102,98
            ]
        as HEX string:
        4f213d2a252a333030423130533f2b33332536306f4f6f6221256935304f1112
        """

        key = ''.join(
            ['{:x}'.format(int(digit)) for digit in django_settings.PVBKI_KEY]
        )

        return key

    def get_params(self, identification):
        """
        Make request params for XML document
        """

        return {
            'username': django_settings.PVBKI_USERNAME,
            'password': django_settings.PVBKI_PASSWORD,
            'endpoint': django_settings.PVBKI_ENDPOINT,
            'key': self.get_key(),
            'identification': identification
        }

    def get_statement_report(self, identification):
        """
        Get standard report with Address, Collateral,
        Communication, Contract, Dependant, Event,
        Identification, MonthlyIncome, Record,
        Subject and Summary objects

        Parameters
        ----------
        identification : str
            Должно содержать одно из:
            - ИНН (10 цифр):
                ІПН (Індивідуальний податковий номер)
                РНОКПП (Реєстраційний номер облікової картки платника податків)
            - ЕДРПОУ (8 цифр):
                Номер юридического лица
            - Паспорт(AA-012013):
                Паспорт физ. лица

        Returns
        -------
        saved_objects_count_dict: dict
            Number of objects created by each block

        Docs:
        https://secure.pvbki.com/reverse-service/default.asmx?op=Report-Statement
        """

        params = self.get_params(identification)

        # Set params to XML file
        xml = render_to_string(
            "pvbki/request_report_statement.xml",
            params
        ).encode('utf-8')

        r = requests.post(
            url='https://{0}/reverse-service/default.asmx'.format(
                self.domain
            ),
            data=xml,
            headers={'Content-Type': 'application/soap+xml'}
        )

        parsed_response = self._parse_response(r.text, 'Statement')
        parsed_report = self._parse_report(parsed_response)
        saved_objects_count_dict = self._save(parsed_report)

        return saved_objects_count_dict

    def get_statementplus_report(self, identification):
        """
        Get standard report with Address, Collateral,
        Communication, Contract, Dependant, Event,
        Identification, MonthlyIncome, Record,
        Subject and Summary objects + Scoring object

        Parameters
        ----------
        identification : str
            Должно содержать одно из:
            - ИНН (10 цифр):
                ІПН (Індивідуальний податковий номер)
                РНОКПП (Реєстраційний номер облікової картки платника податків)
            - ЕДРПОУ (8 цифр):
                Номер юридического лица
            - Паспорт(AA-012013):
                Паспорт физ. лица

        Returns
        -------
        saved_objects_count_dict: dict
            Number of objects created by each block

        Docs:
        https://secure.pvbki.com/reverse-service/default.asmx?op=Report-StatementPlus
        """

        params = self.get_params(identification)

        # Set params to XML file
        xml = render_to_string(
            "pvbki/request_report_statementplus.xml",
            params
        ).encode('utf-8')

        r = requests.post(
            url='https://{0}/reverse-service/default.asmx'.format(
                self.domain
            ),
            data=xml,
            headers={'Content-Type': 'application/soap+xml'}
        )

        parsed_response = self._parse_response(r.text, 'StatementPlus')
        parsed_report = self._parse_report(parsed_response)
        saved_objects_count_dict = self._save(parsed_report)

        return saved_objects_count_dict

    def get_statement2017_report(self, identification):
        """
        Get standard report with Address, Collateral,
        Communication, Contract, Dependant, Event,
        Identification, MonthlyIncome, Record,
        Subject and Summary objects
        + Scoring, MVSCheckup, ERBCheckup, EDR objects

        Parameters
        ----------
        identification : str
            Должно содержать одно из:
            - ИНН (10 цифр):
                ІПН (Індивідуальний податковий номер)
                РНОКПП (Реєстраційний номер облікової картки платника податків)
            - ЕДРПОУ (8 цифр):
                Номер юридического лица
            - Паспорт(AA-012013):
                Паспорт физ. лица

        Returns
        -------
        saved_objects_count_dict: dict
            Number of objects created by each block

        Docs:
        https://secure.pvbki.com/reverse-service/default.asmx?op=Report-Statement2017
        """

        params = self.get_params(identification)

        # Set params to XML file
        xml = render_to_string(
            "pvbki/request_report_statement_2017.xml",
            params
        ).encode('utf-8')

        r = requests.post(
            url='https://{0}/reverse-service/default.asmx'.format(
                self.domain
            ),
            data=xml,
            headers={'Content-Type': 'application/soap+xml'}
        )

        parsed_response = self._parse_response(r.text, 'Statement2017')
        parsed_report = self._parse_report(parsed_response)
        saved_objects_count_dict = self._save(parsed_report)

        return saved_objects_count_dict

    def _parse_response(self, response, report_name):
        """
        Example of XML
        --------------
        <?xml version="1.0" encoding="utf-8"?>
        <soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
                       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                       xmlns:xsd="http://www.w3.org/2001/XMLSchema">
            <soap:Header>
                <BackError xmlns="https://service.pvbki.com/reverse">
                    ...
                </BackError>
                <InvokeReflection xmlns="https://service.pvbki.com/reverse">
                    ...
                </InvokeReflection>
            </soap:Header>
            <soap:Body>
                <Report-StatementPlusResponse xmlns="...">
                    <Report-StatementPlusResult>
                        3C3F786D6C2076657273696F6...
                    </Report-StatementPlusResult>
                </Report-StatementPlusResponse>
            </soap:Body>
        </soap:Envelope>


        Parameters
        ----------
            response : XML document

        Returns
        -------
        str
            Decoded data (from Report-{report_name}Result tag of XML document)
        """

        # Convert response XML to dict
        resp = xmltodict.parse(response)

        envelope = resp.get('soap:Envelope', None)
        if not envelope:
            raise Exception(
                'Invalid report (hasn\'t soap:Envelope key)'
            )

        body = envelope.get('soap:Body', None)
        if not body:
            raise Exception(
                'Invalid report (hasn\'t soap:Body key)'
            )

        report_resp = body.get(
            'Report-{0}Response'.format(report_name),
            None
        )
        if not report_resp:
            raise Exception(
                'Invalid report (hasn\'t Report-{0}Response key)'.format(
                    report_name
                )
            )

        report_hex = report_resp.get(
            'Report-{0}Result'.format(report_name),
            None
        )
        if not report_hex:
            return ''

        # return decoded report
        return binascii.unhexlify(report_hex)

    def _parse_report(self, report):
        """
        Parse all blocks of report:
            <Statement>
                <Subject>
                <Identification>
                <Identification>
                <Address>
                ...
            </Statement>

        Parameters
        ----------
            report : str
                Decoded part of XML document

        Returns
        -------
        dict
            Return dictionary with data that ready for saving
        """

        parsed_dict = {}
        try:
            parsed_file = xmltodict.parse(report)
        except Exception:
            return parsed_dict

        for block in parsed_file["Statement"].keys():
            if block not in self.passed_keys:  # Pass particular keys
                parsed_dict[block] = []

                # Parse all blocks one by one; save in parsed_dict
                self._parse_recursively(
                    parsed_file["Statement"][block],
                    parsed_dict[block]
                )

        return parsed_dict

    def _parse_recursively(self, block, parsed):
        """
        Parse block by block:
            {"Statement": {
                "Subject: dict(...),
                "Identification": list(
                    dict(...),
                    dict(...),
                    ...
                ),
                "Address: dict(...),
                ...
            }

        Parameters
        ----------
            block : dict or list
                Block that will be parsed and saved in parsed list
            parsed : list
                Contains all parsed blocks: [dict(), dict(), ...]
        """
        if isinstance(block, dict):
            items = {}
            for key in block:
                langs = ['ua', 'ru', 'en']

                # Check keys as 'firstNameEN', 'firstNameUA', 'firstNameRU'
                # excluding 'when' key
                if any(l in key.lower()[-2:] for l in langs) and key != 'when':
                    # firstNameEN -> firstName_en
                    keyname = key[:-2] + '_' + key.lower()[-2:]
                    # Split by A-Z letters
                    splitted_key = re.sub(r"([A-Z])", r" \1", keyname).split()
                else:
                    # Split by A-Z letters
                    splitted_key = re.sub(r"([A-Z])", r" \1", key).split()\

                # Make new key:
                # ['fathers', 'Name_ua'] -> fathers_name_ua
                # ['rest', 'Instalment', 'Count'] -> rest_instalment_count
                new_key = "_".join(splitted_key).lower()

                items[new_key] = block[key]

            parsed.append(items)
        elif isinstance(block, list):
            # Parse list of blocks
            for item in block:
                self._parse_recursively(item, parsed)
        else:
            raise Exception('Invalid report (not [list, dict])')

    def _save(self, parsed):
        """
        Returns
        -------
        dict
            Return saved objects count dict with all
            block names: {Subject: 1, Address: 5, ...}
        """

        saved = {}

        model_name = 'Subject'
        try:
            SubjectModel = apps.get_model(
                app_label='pvbki',
                model_name=model_name
            )
        except Exception:
            return saved

        subject_list = parsed.pop('Subject', None)

        if subject_list:
            # Check object is already created
            self.subject_object, created = SubjectModel.objects.get_or_create(
                requestid=subject_list[0]['requestid'],
                defaults=subject_list[0]
            )

            if created:
                # Update Subject counter
                if model_name in saved.keys():
                    saved[model_name] += 1
                else:
                    saved[model_name] = 1

        # Save other blocks
        for block_name in parsed.keys():
            saved.update(
                self._save_block(
                    object_list=parsed[block_name],
                    model_name=block_name,
                    root=self.subject_object
                )
            )

        return saved

    def _save_block(self, object_list, model_name, root=None):
        """
        Returns
        -------
        dict
            Return saved objects count dict with all
            block names: {Identification: 1, Address: 5, ...}
        """

        saved = {}

        try:
            Model = apps.get_model(app_label='pvbki', model_name=model_name)
        except Exception:
            return saved

        # All model fields names
        model_fields = [field.name for field in Model._meta.get_fields()]

        for object_dict in object_list:
            temp_dict = object_dict.copy()

            # Remove excess data
            for object_field in temp_dict:
                if object_field not in model_fields:
                    object_dict.pop(object_field, None)

            # Set related FK object (Subject)
            if 'subject' in model_fields:
                object_dict.update({'subject': root})

            if not Model.objects.filter(**object_dict).exists():
                Model.objects.create(**object_dict)

                if model_name in saved.keys():
                    saved[model_name] += 1
                else:
                    saved[model_name] = 1

        return saved
