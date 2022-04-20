file = open("/home/nzangi/employees", 'r')
contents = file.read()
print(contents)

# 1. employee dictionary
jack = {"name": "Ames",
        "id": 111452,
        "hours": [45],
        "payrate": [17.50],
        }

# 2. employee dictionary
james = {"name": "Sims",
         "id": 111657,
         "hours": [35],
         "payrate": [22.75],
         }

# 3. employee dictionary
dylan = {"name": "Manning",
         "id": 111932,
         "hours": [52],
         "payrate": [16.50],
         }
# 4. employee dictionary

cindy = {"name": "Carson",
         "id": 1117,
         "hours": [48],
         "payrate": [18.50],
         }

# 5. Jessica's dictionary
jess = {"name": "Jacobs",
        "id": 111873,
        "hours": [30],
        "payrate": [25],
        }

# 6. employee dictionary

tom = {"name": "Adrews",
       "id": 11262,
       "hours": [91],
       "payrate": [92]
       }

employes = [jack, james, dylan, jess, tom, cindy]


# calculating the payment of the employer
def get_average(payment):
    total_sum = sum(payment)
    total_sum = float(total_sum)
    return total_sum / len(payment)


# computing employee pay
def compute_pay(employes):
    test1 = get_average(employes["hours"])
    test2 = get_average(employes["payrate"])
    # checking if hours worked is greater than 40
    if test1 > 40:
        pay = test1 * 1.75 * test2
    else:
        pay = test1 * test2
    return pay


open('payfile.txt', 'w').close()
print('{a:^8}{b:^8}{c:^8}'.format(a='ID', b='Lastname', c='Pay'), file=open('payfile.txt', 'a'))
for i in employes:
    print(i["id"], '\t', i["name"], '\t', compute_pay(i), file=open('payfile.txt', 'a'))
