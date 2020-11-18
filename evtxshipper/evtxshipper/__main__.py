import asyncio
import logging
import argparse

handler = logging.StreamHandler()
handler.setFormatter(
    logging.Formatter(
        style="{",
        fmt="[{name}:{filename}] {levelname} - {message}"
    )
)

log = logging.getLogger("evtxshipper")
log.setLevel(logging.INFO)
log.addHandler(handler)

def main():
    parser = argparse.ArgumentParser()
    #parser.add_argument('evtxfile', help="Evtx file to parse")
    #parser.add_argument('elk_ip', default="localhost", help="IP (and port) of ELK instance")
    #parser.add_argument('-i', default="hostlogs", help="ELK index to load data into")
    #parser.add_argument('-s', default=500, help="Size of queue")
    #parser.add_argument('-meta', default={}, type=json.loads, help="Metadata to add to records")
    # Parse arguments and call evtx to elk class
    args = parser.parse_args()
    EvtxToElk.evtx_to_elk(args.evtxfile, args.elk_ip, elk_index=args.i, bulk_queue_len_threshold=int(args.s), metadata=args.meta)
    return
