class Company:
    def __init__(self, name, type, direction, *pers):
        self.name = name
        self.type = type
        self.direction = direction
        self.pers = pers

    def get_phone(self):
        phone = self.direction.get('contact', None)
        if not phone:
            for elem in self.pers:
                phone = elem.direct.get('work', None)
                if phone:
                    return phone
        if not phone:
            return None
        return phone

    def get_name(self):
        return self.name

    def get_sms_text(self):
        return 'Для компании {} есть суперпредложение! Примите участие в нашем беспроигрышном конкурсе для {}.'.format(
            self.name, self.type)


class Person:
    def __init__(self, name, otch, fam, direct, ):
        self.name = name
        self.otch = otch
        self.fam = fam
        self.direct = direct

    def get_phone(self, ):
        return self.direct.get('private', None)

    def get_name(self):
        return '{} {} {}'.format(self.fam, self.name, self.otch)

    def get_work_phone(self):
        return self.direct.get('work', None)

    def get_sms_text(self):
        return 'Уважаемый {} {}! Примите участие внашем беспроигрышном конкурсе для физических лиц.'.format(self.name,
                                                                                                            self.otch)


def send_sms(*pers):
    for elem in pers:
        if elem.get_phone():
            print('Отправлено СМС на номер {} с текстом: {}'.format(elem.get_phone(), elem.get_sms_text()))
        else:
            print('Не удалось отправить сообщение абоненту: {}'.format(elem.get_name()))
