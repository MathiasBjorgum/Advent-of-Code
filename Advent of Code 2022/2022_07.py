from data.data_util import get_data


def main():
    data = [command for command in get_data().split("\n")[1:]]

    filesystem = {"": 0}
    pwd = ""

    for command in data:

        if ".." in command:
            pwd = pwd[:pwd.rindex("/")]

        elif "$ cd" in command:
            pwd = pwd + "/" + command[5:]
            filesystem[pwd] = 0

        elif command.split(" ")[0].isnumeric():
            size = int(command.split(" ")[0])
            filesystem[""] += size

            cur = pwd
            while cur:
                filesystem[cur] += size
                cur = cur[:cur.rindex("/")] if "/" in cur else ""

    print("Part 1")
    print(sum(size for size in filesystem.values() if size <= 100000))

    av_disk_space = 70000000
    req_space = 30000000
    used_space = filesystem[""]
    unused_space = av_disk_space - used_space
    need_to_free = req_space - unused_space

    print("Part 2")
    print(sorted(size for size in filesystem.values()
          if size > need_to_free)[0])


if __name__ == "__main__":
    main()
