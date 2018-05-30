class Company(object):
    name = '汉口测试'
    numbers = '88888888'
    location = '营房村'
    portal = 'pra'
    das = 600
    dpc = '1.3.25'
    remarks = ""
    created_by = "Andy"
    circuits = "1-3-25-1"

    def __init__(self, **company):
        if len(company):
            self.name = company['Name']
            self.portal = company['Portal']
            self.numbers = company['Numbers']
            self.dpc = company['DPC']
            self.das = company['Das']
            self.created_by = company['Creater']

    def make_pra_script(self):
        print(ADD_ADJOFC(trunk='701', name='aaa',  mgcf='MGCF11', dpc='255.1.1', net='49', module='4'))

    def make_isup_script(self):
        print(self.name, self.portal)

    def make_tup_script(self):
        print(self.name, self.portal)

    def make_script(self):
        if self.portal == 'pra':
            self.make_pra_script()
        elif self.portal == 'tup':
            self.make_tup_script()
        elif self.portal == 'isup':
            self.make_isup_script()


def ADD_ADJOFC(trunk, name, module, net, mgcf, dpc):
    return 'ADD ADJOFC:ID=' + trunk + ',NAME="' + mgcf + '_武汉_' + name + '",MODULE=' + module + ',NET=' + net + ',OFCTYPE="LOCAL"&"PSTN",SPCTYPE="24",DPC="' + dpc + '",RC="27";'

def ADD_TG_PRA():
    return '''ADD TG PRA:TG=701,OFC=701,NODE=361,MODULE=11,NAME="MGCF21_武汉_aaa_1",TPDAS=1204,CICSEL="EVEN",IOI="MGCF21-WH_TGID-701-1.hb.ctcims.cn";'''


def ADD_SPCM():
    return '''ADD SPCM:TG=701,PCM=1,MGWPCM=256;'''


if __name__ == '__main__':
    # c = {'name': 'alibaba', 'portal': 'isup'}
    Company().make_script()
