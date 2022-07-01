# This is a testcase file for epos.py, it should not crash with an error and exit normally.
import epos


def testcase_main():
    print('pre-testcase...')
    e = epos.EposClient()
    e2 = epos.EposClient()

    # achtung paroli!!!
    login = input("Login (E-Mail): ")
    password = input("Password: ")

    eposok = e.auth_epos_student()
    epossessions = e.epos_get_sessions()
    myuserid = epossessions['id']
    myprofid = epossessions['profiles'][0]['id']
    eposacadem = e.epos_get_academic_years(myprofid)
    eposmessages = e.epos_get_system_messages(myprofid, True, True)
    eposprogress = e.epos_get_progress(myprofid, eposacadem[-1]['id'], True)
    eposnotifs = e.epos_get_notifications(myprofid)
    # ?????????????????
    eposusers = e.epos_get_users([myuserid, myuserid], myprofid)
    # print results
    print(f'{e.login_password(login, password)=}')
    print(f'{e.check_agreement()=}')
    print('eposOk=', eposok)
    print('eposSessions=', epossessions)
    print('eposAcademYears=', eposacadem)
    print('eposMessages=', eposmessages)
    print('eposUserData=', eposusers)
    print('eposNotifs=', eposnotifs)
    print('eposProgress=', eposprogress)
    eposlogout = e.epos_logout()
    rsaaglogout = e.logout()
    print('eposLogout=', eposlogout)
    print('rsaagLogout=', rsaaglogout)
    print('Student testcase PASS :D')

    # Teacher login test
    login = input("Login (E-Mail): ")
    password = input("Password: ")

    myuserid = epossessions['id']
    myprofid = epossessions['profiles'][0]['id']
    eposacadem = e2.epos_get_academic_years(myprofid)
    eposmessages = e2.epos_get_system_messages(myprofid, True, True)
    eposnotifs = e2.epos_get_notifications(myprofid)
    eposusers = e2.epos_get_users([myuserid, myuserid], myprofid)
    # Print results
    print(f'{e2.auth_epos_teacher(login, password)=}')
    print(f'{e2.epos_get_sessions()=}')
    print('eposAcademYears=', eposacadem)
    print('eposMessages=', eposmessages)
    print('eposUserData=', eposusers)
    print('eposNotifs=', eposnotifs)
    eposlogout = e.epos_logout()
    print('eposLogout=', eposlogout)
    print('Teacher testcase PASS :D')


# the fun starts here
if __name__ == '__main__':
    testcase_main()
