
# Code Challenge:
# Print out all of the strings in the following array in alphabetical order,
# each on a separate line.

# The expected output is:
# 'Cha Cha'
# 'Foxtrot'
# 'Jive'
# 'Paso Doble'
# 'Rumba'
# 'Samba'
# 'Tango'
# 'Viennese Waltz'
# 'Waltz'
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code.
# Run through the UPER problem solving framework while going through your thought process.

array = [
    'Waltz',
    'Tango',
    'Viennese Waltz',
    'Foxtrot',
    'Cha Cha',
    'Samba',
    'Rumba',
    'Paso Doble',
    'Jive'
]


def print_each_line(array):
    #sort array 
    sorted_array = sorted(array)

    for i in sorted_array:
        print(i)


print_each_line(array)




