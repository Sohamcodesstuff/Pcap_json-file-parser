# C:/Users/soham/Desktop/net_cap.json

import sys
import json

print("time_epoch ip proto src dst srcport dstport plength")
for packet in json.load(open('C:/Users/soham/Desktop/net_cap.json')):
	layers = packet["_source"]["layers"]
	frame = layers["frame"]
	eth = layers["eth"]

	row = {}

	if "ipv6" in layers:
		row["ip"] = "v6"
		row["src"] = layers["ipv6"]["ipv6.src"]
		row["dst"] = layers["ipv6"]["ipv6.dst"]
		row["plen"] = layers["ipv6"]["ipv6.plen"]
	elif "ip" in layers:
		row["ip"] = "v4"
		row["src"] = layers["ip"]["ip.src"]
		row["dst"] = layers["ip"]["ip.dst"]
		row["plen"] = layers["ip"]["ip.len"]
		# row[]
	else:
		continue

	if "tcp" in layers:
		row["proto"] = "tcp"
		row["srcport"] = layers["tcp"]["tcp.srcport"]
		row["dstport"] = layers["tcp"]["tcp.dstport"]
	elif "udp" in layers:
		row["proto"] = "udp"
		row["srcport"] = layers["udp"]["udp.srcport"]
		row["dstport"] = layers["udp"]["udp.dstport"]
	else:
		continue

	time_epoch = frame["frame.time_epoch"]
	time_delta = frame["frame.time_delta"]
	print(time_epoch, time_delta, row["ip"], row["proto"], row["src"], row["dst"], row["srcport"], row["dstport"], row["plen"],sep=',')