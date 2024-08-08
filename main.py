import create_graph as cga

# Print output to file
done = False

while not done:
    # Since this Hamiltonian path problem is NP-complete and may not always succeed on the first run, we may need to try multiple times
    try:
        # Create network
        G = cga.create_nodes_from_csv('data.csv')
        G = cga.create_edges(G)

        print("calculating...")
        # Calculate the send-receive pairs
        results = cga.get_hamiltonian_path(G)

        with open('results.tsv', 'w') as f:
            print('FROM\tTO\tMATCH\tRECV_GROUPS', file=f)
            for idx, x in enumerate(results):
                if idx < len(results) - 1:
                    edge = G.get_edge_data(results[idx],results[idx+1])
                    print('{}\t{}\t{}\t{}\t{}'.format(idx, results[idx], results[idx+1], edge['groups'], edge['dest_groups']), file=f)
                else:
                    edge = G.get_edge_data(results[idx],results[0])
                    print('{}\t{}\t{}\t{}\t{}'.format(idx, results[idx], results[0], edge['groups'], edge['dest_groups']), file=f)
            done = True
    except TypeError:
        print("Attempting calculation again...")
        continue

print("Complete! See results.tsv for output.")