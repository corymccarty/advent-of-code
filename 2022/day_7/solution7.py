from __future__ import annotations

from dataclasses import dataclass
from typing import Dict


@dataclass
class File:
    name: str
    size: int


class Directory:
    def __init__(self, parent: Directory | None, name: str):
        self.parent = parent
        self.name = name
        self.files: Dict[str, File] = {}
        self.subdirectories: Dict[str, Directory] = {}

    @property
    def size(self) -> int:
        file_sizes = [file.size for file in self.files.values()]
        total_file_size = sum(file_sizes)
        return total_file_size + self._get_total_subdirectory_size()

    def get_or_create_subdirectory(self, name: str) -> Directory:
        if name not in self.subdirectories.keys():
            # Might not be necessary if an ls always preceeds cd, but can't hurt
            new_directory = Directory(self, name)
            return new_directory
        return self.subdirectories[name]

    def contains_file(self, name: str) -> bool:
        return name in self.files.keys()

    def add_file(self, file: File):
        self.files[file.name] = file

    def _get_total_subdirectory_size(self) -> int:
        size = 0
        for subdirectory in self.subdirectories.values():
            size += subdirectory.size
        return size


class Filesystem:
    def __init__(self):
        self.root_directory = Directory(None, "/")
        self.current_directory = self.root_directory
        self.read_input_file()

    def read_input_file(self) -> None:
        with open("2022/day_7/input.txt") as file:
            lines = file.readlines()
        lines = [line.strip() for line in lines]
        for line in lines:
            if line.startswith("$"):
                command = line.strip("$").strip()
                self.process_command(command)
            else:
                self.process_command_output(line)

    def process_command(self, command: str) -> None:
        if command.startswith("cd"):
            target = command.split()[1]
            if target == "/":
                self.current_directory = self.root_directory
            else:
                self.current_directory = (
                    self.current_directory.get_or_create_subdirectory(target)
                )
        # We don't need to take action on any other commands

    def process_command_output(self, line: str) -> None:
        parts = line.split()
        if parts[0].isdigit():
            # It's a file
            filename = parts[1]
            file_size = int(parts[0])
            if not self.current_directory.contains_file(filename):
                self.current_directory.add_file(File(filename, file_size))
        elif parts[0] == "dir":
            # It's a directory
            directory_name = parts[1]
            self.current_directory.get_or_create_subdirectory(directory_name)
        else:
            raise Exception(f"Unexpected command output: {line}")


filesystem = Filesystem()
print(f"Total filesystem size: {filesystem.root_directory.size}")
