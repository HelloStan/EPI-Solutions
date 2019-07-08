from test_framework import generic_test


def num_combinations_for_final_score(final_score, individual_play_scores):
    # TODO - you fill in here.
    combinations_for_score = [[1] + [0] * final_score for _ in range(len(individual_play_scores))]

    for i in range(1, final_score + 1):
        for j, score in enumerate(individual_play_scores):
            if j > 0:
                # Combinations of plays with total score i using play scores up to excluding the current score
                combinations_for_score[j][i] += combinations_for_score[j - 1][i]
            if i >= score:
                # Combinations of plays for total score i-score using play scores up to including the current score
                combinations_for_score[j][i] += combinations_for_score[j][i - score]

    return combinations_for_score[-1][-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_score_combinations.py",
                                       "number_of_score_combinations.tsv",
                                       num_combinations_for_final_score))
