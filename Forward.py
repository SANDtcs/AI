def forward_algorithm(sequence, states, emissions, transitions, initial_distribution):
    
    # Initialize the forward probabilities with zeros
    forward_probs = [{} for _ in range(len(sequence))]
    
    # Initialize the first forward probabilities using the initial distribution
    for state in states:
        forward_probs[0][state] = initial_distribution[state] * emissions[state][sequence[0]]
    
    # Recursively calculate the remaining forward probabilities
    for t in range(1, len(sequence)):
        for state in states:
            forward_probs[t][state] = emissions[state][sequence[t]] * sum(
                forward_probs[t-1][prev_state] * transitions[prev_state][state] for prev_state in states
            )
    
    # Calculate the total probability of the sequence as the sum of the final forward probabilities
    total_prob = sum(forward_probs[-1][state] for state in states)
    
    return forward_probs, total_prob


# Define the states, emissions, transitions, and initial distribution
states = ['h', 'l']
emissions = {
    'h': {'A': 0.2, 'C': 0.3, 'G': 0.3, 'T': 0.2},
    'l': {'A': 0.3, 'C': 0.2, 'G': 0.2, 'T': 0.3},
}
transitions = {
    'h': {'h': 0.5, 'l': 0.5},
    'l': {'h': 0.4, 'l': 0.6},
}
initial_distribution = {'h': 0.5, 'l': 0.5}

# Generate the gene sequence GGCA
sequence = 'GGCA'

# Run the forward algorithm
forward_probs, total_prob = forward_algorithm(sequence, states, emissions, transitions, initial_distribution)

# Print the results
print('Forward probabilities:')
for t in range(len(sequence)):
    print(f't = {t}:', forward_probs[t])
print('Total probability of the sequence:', total_prob)

