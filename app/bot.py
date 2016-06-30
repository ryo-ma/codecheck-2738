#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Bot:
    def __init__(self, command_data):
        self.command = command_data['command']
        self.data = command_data['data']
        self.hash = self.generate_hash()

    def generate_hash(self):
        command_ascii = ''.join([str(ord(x)) for x in list(self.command)])
        data_ascii = ''.join([str(ord(x)) for x in list(self.data)])
        result_command = Bot.scientific_notation(int(command_ascii))
        result_data = Bot.scientific_notation(int(data_ascii))
        sum_ascii = Bot.extract_character(result_command) + Bot.extract_character(result_data)
        return hex(sum_ascii)[2:]

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