# Secret Santa

## Parameters
- Number of participants: 23
- Each participant have 1-N group(s) that they want to send and they want to receive
  - The group they want to send/receive can be different
- Participants are in US and Canada only
  - Some participants want to only send to US
- Each participant can only exchange a gift with another participant exaclty once
- Source and destination participants cannot exchange gifts with each other

## BONUS - Special Node (Magic M)
- M node can receive 0 or 1 cards
- M node can send any group to anyone in any location
- M node can send 0 - N cards

### Groups available
- Seventeen
- NCT
- Stray Kids
- ATEEZ
- TXT
- The Boyz

# Approach

- Write in Python for ease of understanding
- Using Conda to manage depencies
- Use the `networkx` library for graph data representation an manipulation

## Phase I - Graph building

### Data Preprocessing
- Individuals are 

**Task**: Given each group's preferences and geo-locations, build the Directed Graph of all the possible ways each person can send to another
- Person - Node
- Sending gift to another person - Edge

## Phase II - Constraint checking
**Task**: Prepare the graph(s) to meet algorithmic constraints
- Identify the islands
- For each island with odd people, add the M node

### Phase III - Hamiltonian Path Proposal
**Task**: Find the Hamiltonian Path -> this is the gift exchange solution