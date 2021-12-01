import json

import requests

requests.packages.urllib3.disable_warnings()

cookies = {
    'REC_T_ID': '6eb4fb29-30ab-11ec-814d-2cea7fb11219',
    'SPC_F': 'rq905bqr10Aws8HgehEuDjb2q7U9uH7V',
    '_gcl_au': '1.1.585658490.1634627343',
    '_fbp': 'fb.1.1634627345349.655915607',
    'SPC_IA': '-1',
    'csrftoken': 'woGiEkoebedf6dc7CfqpRNyV5GueiXKg',
    'SPC_SI': 'bfftocsg9.MDTzNv9jDXugLwGaehOrmLYUyeAlwdWc',
    'G_ENABLED_IDPS': 'google',
    '_QPWSDCXHZQA': '=a98b84af-3108-41b7-d7a9-70ff939ce94c',
    '_gid': 'GA1.2.597331637.1638349133',
    'welcomePkgShown': 'true',
    'language': 'zhHans',
    'cto_bundle': '3mwpgV9NNkppNlVINTl5UUhTd2dzR1NBM0p0M0tXYjVmRVBpQ0Q1ZDBuQ3lJc1NyVEpOS0xGekdyY0xQWmxYblZOVzRRN1JXVzdmNVlpdGJVMHpyWVg2eVB3RDNLYXBCWG1SOEVzblFHNGwlMkJUQ3JlUFZLZEVCbDFtMmkwYXh1V1olMkZDcVY1dWppUmM0bzhHWXdFbzN2WWlPSjd3JTNEJTNE',
    'shopee_webUnique_ccd': 'd4eEcm8BJR9qJEflD9ONcg==|oXk7qDyfzd/udbMHxWUuSxu/puqsrAHKbvvUbEhSU50Y2aAp5LjuVqXDVjfIvrV+o9wFSFy1WeImEASnRys=|zOlZew9MqumZS7Qf|03|3',
    'SPC_ST': '".VWNjY00zTklzRFhlMERTTDdwlMRXJQDFo+8RT2OD3t0XzWefNxYChb2u8NcE+yjRzPU10ZVoXR2u3d1dcjEFiYWLBQm8JWsCQLe5ifJL8bNnsW5wnwOm5zexqF1MLV+uGXvgVXvbN4yN5Ok6QZp4RSBJosQvuO21IQgqev61ORg9oAzZeEDKvDXnVx4OFSQGrhRStI/wb3cO4NTAXnuxCA=="',
    'SPC_U': '609189515',
    'SPC_CLIENTID': 'cnE5MDVicXIxMEF3ogrovfpcnbertzju',
    'SPC_EC': 'WnNzMmluVkk4M0hoSHhDeIwTCrvhA0BdwavKEJ1oX/P4RXeMeI3kh/t1+8FKRCVdDKMgeEKuEY+gn3sGTnA0/N5TdvB7Iz948GbudB+ckZCGImffCXL4+/kllQ7ilUsT6Q1aNNwPwBTkvD1lD5CsQwu3mt6x3x4BfgYmkFuHfdY=',
    'SPC_T_IV': '"ztDV+xJ+oqkglJTeuRZgqQ=="',
    'SPC_T_ID': '"kT8lZlyrWXY62xfYIwbLHrsi3uUF1q928rkcWsciD0dLIQABxYpNvQQiQtqPQJw8usz8vpQVOJvgzygmcjGY6ItKuFNCP3rt/vwfZ5Odl74="',
    '_ga_CB0044GVTM': 'GS1.1.1638349115.2.1.1638349739.59',
    'SPC_R_T_ID': 'kT8lZlyrWXY62xfYIwbLHrsi3uUF1q928rkcWsciD0dLIQABxYpNvQQiQtqPQJw8usz8vpQVOJvgzygmcjGY6ItKuFNCP3rt/vwfZ5Odl74=',
    'SPC_R_T_IV': 'ztDV+xJ+oqkglJTeuRZgqQ==',
    'SPC_T_ID': 'kT8lZlyrWXY62xfYIwbLHrsi3uUF1q928rkcWsciD0dLIQABxYpNvQQiQtqPQJw8usz8vpQVOJvgzygmcjGY6ItKuFNCP3rt/vwfZ5Odl74=',
    'SPC_T_IV': 'ztDV+xJ+oqkglJTeuRZgqQ==',
    '_ga': '=GA1.2.1561240551.1634627347',
}


def fetch_division_sub(sub):
    url = 'https://shopee.ph/api/v4/location/get_child_division_list?division_id=%s' % sub
    params = {}
    r = requests.get(url, params=params, verify=False, cookies=cookies)
    res_obj = json.loads(r.text, encoding='utf-8-sig')
    print('fetch division[%s]' % sub)
    return res_obj['data']['divisions']


def save_json(name, obj):
    f = open('./%s.json' % name, 'w')
    json.dump(obj, f)
    f.close()


levels = [[], [], [], []]


def fetch_by_depth(level, father):
    if level > 3:
        return
    print('start level: [%s][%s]' % (level, father))
    divs = fetch_division_sub(father)
    for sub in divs:
        sub['parent'] = father
        levels[level].append(sub)
        fetch_by_depth(level + 1, sub['id'])


def do_fetch_all():
    fetch_by_depth(0, 0)
    for idx, lev in enumerate(levels):
        save_json('level%s' % (idx + 1), lev)


do_fetch_all()
