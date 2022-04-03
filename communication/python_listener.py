
import threading, queue
from erlastic import port_connection, Atom as A
from pprint import pprint

def main():
    mailbox, port = port_connection()

    q = []

    for (tag, data) in mailbox:
        if tag == A("init_state"):
            set_initial_state(data)
        elif tag == A("update"):
            update_car(data, q)
            if len(q) > 100:
                dump_queue(q)

def set_initial_state(data: tuple) -> None:
    with open("output.txt", "a", encoding="utf-8") as f:
        print(f"got a state: {data}", file=f)

def update_car(update: tuple, work_queue: list) -> None:
    work_queue.append(update)

def dump_queue(jobs: list) -> None:
    with open("output.txt", "a", encoding="utf-8") as f:
        for job in jobs:
            print(f"crisis alert! {job}", file=f, flush=True)
    jobs.clear()

if __name__ == "__main__":
    main()
