#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Bot:
    def __init__(self, command_data):
        self.command = command_data['command']
        self.data = command_data['data']
        self.hash = self.generate_hash()

    def generate_hash(self):
        command_ascii = Bot.to_ascii(self.command)
        data_ascii = Bot.to_ascii(self.data)
        command_science_notation = Bot.scientific_notation(int(command_ascii))
        data_science_notation = Bot.scientific_notation(int(data_ascii))
        sum_ascii = Bot.extract_character(command_science_notation) + Bot.extract_character(data_science_notation)
        result = hex(sum_ascii)[2:]
        return result

    @staticmethod
    def scientific_notation(num):
        data = "%.16e" % num
        result = data if (int(data.split("e+")[1]) > 20) else num
        return result

    @staticmethod
    def extract_character(value):
        result = value
        if isinstance(value, str):
            result = result[2:]
            result = result.replace('e+', '')
        return int(result)

    @staticmethod
    def to_ascii(value):
        return ''.join([str(ord(x)) for x in list(value)])
