# -*- coding: utf-8 -*-
# vim:set et sts=4 sw=4:
#
# libpinyin - Library to deal with pinyin.
#
# Copyright (C) 2011 Peng Wu <alexepico@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.


import os
from argparse import ArgumentParser
from chewing import gen_initials, gen_middles, gen_finals, gen_tones
from fullpinyintable import gen_content_table, gen_pinyin_index, gen_luoma_pinyin_index, gen_secondary_zhuyin_index, gen_zhuyin_index, gen_hsu_zhuyin_index, gen_eten26_zhuyin_index, gen_table_index_for_chewing_key
from specialtable import gen_divided_table, gen_resplit_table
from doublepinyintable import gen_shengmu_table, gen_yunmu_table
from bopomofotable import gen_chewing_symbols, gen_chewing_initials, gen_chewing_middles, gen_chewing_finals, gen_chewing_tones


header = '''/* This file is generated by python scripts. Don't edit this file directly.
 */
'''


def get_table_content(tablename):
    #chewing enums
    if tablename == 'CHEWING_INITIAL':
        return gen_initials()
    if tablename == 'CHEWING_MIDDLE':
        return gen_middles()
    if tablename == 'CHEWING_FINAL':
        return gen_finals()
    if tablename == 'CHEWING_TONE':
        return gen_tones()

    #pinyin table
    if tablename == 'CONTENT_TABLE':
        return gen_content_table()
    if tablename == 'PINYIN_INDEX':
        return gen_pinyin_index()
    if tablename == 'LUOMA_PINYIN_INDEX':
        return gen_luoma_pinyin_index()
    if tablename == 'SECONDARY_ZHUYIN_INDEX':
        return gen_secondary_zhuyin_index()
    if tablename == 'ZHUYIN_INDEX':
        return gen_zhuyin_index()
    if tablename == 'HSU_ZHUYIN_INDEX':
        return gen_hsu_zhuyin_index()
    if tablename == 'ETEN26_ZHUYIN_INDEX':
        return gen_eten26_zhuyin_index()
    if tablename == 'DIVIDED_TABLE':
        return gen_divided_table()
    if tablename == 'RESPLIT_TABLE':
        return gen_resplit_table()
    if tablename == 'TABLE_INDEX':
        return gen_table_index_for_chewing_key()

    #double pinyin table
    (scheme, part) = tablename.split('_', 1)
    if part == "SHENG":
        return gen_shengmu_table(scheme)
    if part == "YUN":
        return gen_yunmu_table(scheme)

    #zhuyin table
    (scheme, part) = tablename.split('_', 1)
    if part == "SYMBOLS":
        return gen_chewing_symbols(scheme)
    if part == "INITIALS":
        return gen_chewing_initials(scheme)
    if part == "MIDDLES":
        return gen_chewing_middles(scheme)
    if part == "FINALS":
        return gen_chewing_finals(scheme)
    if part == "TONES":
        return gen_chewing_tones(scheme)


def expand_file(filename):
    infile = open(filename, "r")
    print(header)
    for line in infile.readlines():
        line = line.rstrip(os.linesep)
        if len(line) < 3:
            print(line)
            continue
        if line[0] == '@' and line[-1] == '@':
            tablename = line[1:-1]
            print(get_table_content(tablename))
        else:
            print(line)


### main function ###
if __name__ == "__main__":
    parser = ArgumentParser(description='Generate header file from template.')
    parser.add_argument('infile', action='store', \
                        help='input file.')

    args = parser.parse_args()
    #print(args)
    expand_file(args.infile)

