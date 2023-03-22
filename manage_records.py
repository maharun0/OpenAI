import csv

def set_records_in_csv(user_id, message, response):
    f = open ("record.csv", "a", newline="", encoding='utf-8')
    writer = csv.writer(f)
    
    name = get_name(user_id)

    tup1 = (name, message, response)
    writer.writerow(tup1)

    f.close()

userlist = {'6244089272278185': 'Maharun Afroz',
            '5913841015371102': 'Fariha Tasnim',
            '6143663159019724': 'Ananna Saha',
            '5950191955069291': 'Tahsina Tabassum',
            '6329544143743351': 'Mahian Maanmeet',
            '9643265699024238': 'Ahnaf Ojayer',
            '6047135592070983': 'Satavisa Borno',
            '6042976589117681': 'Tan Vir',
            '5914748435310280': 'Mahir Shahriar Tamim',
            '5856479801116592': 'Umme Habiba'}

def get_name(user_id):
    return userlist.get(user_id, user_id)