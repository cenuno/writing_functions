from typing import List, Dict

# load example data
J = [4, 4, 4, 9, 10, 11, 12]
p = 3


def gen_seq(j_list: List[int], p: int) -> Dict[str, float]:
    """Generates a sequence of tuples from a list & returns the min-max means
    """
    sequences = []
    for ind, _ in enumerate(j_list):
        end_range = ind + p
        sequence = j_list[ind:end_range]
        if len(sequence) == p:
            sequences.append(sequence)

    avgs = [sum(sequence) / len(sequence) for sequence in sequences]

    output = {}
    output["min"] = min(avgs)
    output["max"] = max(avgs)
    return output


assert gen_seq(j_list=[1, 2, 3, 4, 5, 6], p=2) == {"min": 1.5, "max": 5.5}

print(gen_seq(j_list=[1, 2, 3, 4, 5, 6], p=2))

# end of script #
