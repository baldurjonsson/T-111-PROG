FILE_NAME = "active_customers_by_month.csv"


def main():
    file_obj = open_file(FILE_NAME)
    if file_obj:
        csv = parse_csv(file_obj)
        month_dict = get_month_dict_from_csv(csv)
        show_customer_list('Premium customers', find_premium_customers(month_dict))
        show_customer_list('New customers', find_new_customers(month_dict))
        show_customer_list('Dormant customers', find_dormant_customers(month_dict))


def open_file(filename):
    try:
        return open(filename, 'r')
    except FileNotFoundError:
        pass


def find_premium_customers(month_dict):
    """ Listi af settum með kúnnum, intersectar svo fremsta settið við restina """
    customer_sets = list(month_dict.values())
    return customer_sets[0].intersection(*customer_sets[1:])


def find_new_customers(month_dict):
    """ Listi af settum með kúnnum, diffar síðasta mánuð með hinum """
    customer_sets = list(month_dict.values())
    return customer_sets[-1].difference(*customer_sets[0:-1])


def find_dormant_customers(month_dict):
    """ Listi af settum með kúnnum, diffar allt framar en 2 með fremstu 2"""
    customer_sets = list(month_dict.values())
    earlier = set().union(*customer_sets[0:-2])
    two_months = customer_sets[-1] | customer_sets[-2]
    return earlier.difference(two_months)


def get_month_dict_from_csv(csv):
    month_dict = dict()
    for line in csv:
        month = line[0]
        customer = line[1]
        if month not in month_dict:
            month_dict[month] = set()
        month_dict[month].add(customer)
    return month_dict


def parse_csv(file_obj):
    data = []
    for line in file_obj.readlines():
        entries = list(map(str.strip, line.split(',')))
        data.append(entries)
    return data

# Here's a re-usable method for showing a set of customer names, sorted alphabetically


def show_customer_list(heading: str, customers: set):
    print(heading)
    print("-" * 40)
    for customer in sorted(customers):
        print(customer)
    print()


if __name__ == '__main__':
    main()