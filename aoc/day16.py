import os

current_dir = os.getcwd()
filename = "data/day16.txt"
#filename = "test.txt"

path = os.path.join(current_dir, filename)

prog = []
with open(path) as f:
    for line in f:
        prog.append(line.strip())

size = len(prog)
idx_list = [idx + 1 for idx, val in enumerate(prog) if val == ""]
res = [prog[i: j] for i, j in zip([0] + idx_list, idx_list + ([size] if idx_list[-1] != size else []))]
all_fields = res[0][:-1]
my_ticket = res[1][1:-1]
other_tickets = res[2][1:]


def define_fields(fields):
    separated = {}
    for f in fields:
        data = f.split(": ")
        name = data[0]
        ranges = data[1]
        regions = ranges.split(" or ")
        sections = []
        for r in regions:
            start, stop = r.split("-")
            sections.append((int(start), int(stop)))
        separated[name] = sections
    return separated


def total_range(fields):
    ranges = []
    for f in fields:
        data = f.split(": ")[1]
        regions = data.split(" or ")
        for reg in regions:
            start, stop = reg.split("-")
            ranges.append((int(start), int(stop)))

    all_ranges = set()
    for r in ranges:
        for i in range(r[0], r[1]+1):
            all_ranges.add(int(i))
    return all_ranges


def scanning_error_rate(ranges, tickets):
    missed = []
    for ticket in tickets:
        numbers = ticket.split(",")
        for nr in numbers:
            if int(nr) not in ranges:
                missed.append(int(nr))
    return sum(missed)


def valid_tickets(ranges, tickets):
    invalid = []
    for ticket in tickets:
        valid = True
        numbers = ticket.split(",")
        for nr in numbers:
            if int(nr) not in ranges:
                invalid.append(ticket)
                valid = False
                continue
    return list(set(tickets).difference(set(invalid)))


def fields_for_value(value, fields):
    matches = []
    for field in fields:
        for ranges in fields[field]:
            if value in range(ranges[0], ranges[1]+1):
                matches.append(field)
                continue
    return matches


def map_fields(fields, tickets):
    possible_fields = []
    for ticket in tickets:
        this_ticket = []
        numbers = ticket.split(",")
        for nr in numbers:
            this_ticket.append(fields_for_value(int(nr), fields))
        possible_fields.append(this_ticket)
    return possible_fields


def possible_field_positions(mapped_fields):
    final_positions = []
    for i in range(len(mapped_fields[0])):
        all_in_same_pos = []
        for l in mapped_fields:
            all_in_same_pos.append(l[i])
        final_positions.append(list(set.intersection(*[set(x) for x in all_in_same_pos])))
    return final_positions


def final_positions(possible_positions):
    final = [""]*len(possible_positions)
    while "" in final:
        val = ""
        for i, pos in enumerate(possible_positions):
            if len(pos) == 1:
                final[i] = pos[0]
                val = pos[0]
                break
        if val != "":
            for l in possible_positions:
                if val in l:
                    l.remove(val)
    return final

def find_departures(fields):
    departures = []
    for field in fields:
        if "departure" in field:
            departures.append(field)
    return departures


def mul_departures(final_positions, ticket, departures):
    ticket_vals = [int(x) for x in ticket[0].split(",")]
    tot = 1
    for dep in departures:
        idx = final_positions.index(dep)
        tot *= ticket_vals[idx]
    return tot


### A
print(scanning_error_rate(total_range(all_fields), other_tickets))

### B
ok_tickets = valid_tickets(total_range(all_fields),other_tickets)
def_fields = define_fields(all_fields)
mapped_fields = map_fields(def_fields, ok_tickets)
possible_pos = possible_field_positions(mapped_fields)
final_positions = final_positions(possible_pos)
departures = find_departures(def_fields)
print(mul_departures(final_positions, my_ticket, departures))


