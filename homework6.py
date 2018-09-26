import re
import argparse

# Task1

vowels = re.compile(r'\b[уеыаоэяиюё]+\w+')
print(vowels.findall("опе ирирыв выо лывир выа обcе"))

# Task2

ping = re.compile(r'(icmp_seq=\d+) (ttl=\d+) (time=\d+.\d+\s+\w+)')
print(ping.findall('''
64 bytes from 192.168.0.200: icmp_seq=1 ttl=128 time=2.28 ms
64 bytes from 192.168.0.200: icmp_seq=2 ttl=128 time=0.740 ms
64 bytes from 192.168.0.200: icmp_seq=3 ttl=128 time=0.673 ms
64 bytes from 192.168.0.200: icmp_seq=4 ttl=128 time=0.640 ms
64 bytes from 192.168.0.200: icmp_seq=5 ttl=128 time=1.86 ms
'''))

# Task3

text = input("Введите текст: ")

parser = argparse.ArgumentParser()
parser.add_argument('-N', required=True, dest='N', type=str, help='Print file name')
file_name = parser.parse_args()

quit_prog = re.compile(r'%quit')

if quit_prog.findall(text) == ['%quit']:
    file = open(file_name.N, 'w')
    file.write(re.sub('%quit', '', text))
    file.close()
