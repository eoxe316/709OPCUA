import csv
from opcua import Client

def print_children_to_csv(node, writer, level=0):
    # Write the node's browse name and node id to the CSV file
    writer.writerow(["  " * level + f"{node.get_browse_name()}", f"{node.nodeid}"])

    # Recursively print children nodes
    for child in node.get_children():
        print_children_to_csv(child, writer, level + 1)

url = "localhost"
port = 7001

# Assemble endpoint url
end_point = "opc.tcp://{}:{}".format(url, port)

# Connect to the OPC UA server
client = Client(end_point)
client.connect()

# Browse the address space starting from the root node
root_node = client.get_root_node()

# Open a CSV file for writing
csv_file = "opcua_nodes.csv"
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Node Name", "Node ID"])
    
    print("Writing node information to CSV file...")
    print_children_to_csv(root_node, writer)

print("Node information has been written to", csv_file)


# Disconnect from the server
client.disconnect()
