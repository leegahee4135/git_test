from collections import defaultdict


def solution(genres, plays):
    answer = []

    total = defaultdict(int)  # key= genre, value= sum of plays of key genre
    individual = defaultdict(list)  # key= genre, value = list of plays of key genre

    for i in range(len(genres)):
        total[genres[i]] += plays[i]
        individual[genres[i]].append([i, plays[i]])  # {genre : [i, plays]}

    sorted_total = sorted(total.items(), key=lambda item: item[1], reverse=True)

    for k, v in sorted_total:
        songs = individual[k]
        sorted_songs = sorted(songs, key=lambda val: val[1], reverse=True)
        if len(sorted_songs) != 1:
            first = sorted_songs[0][0]
            second = sorted_songs[1][0]
            answer.append(max(first, second))
            answer.append(min(first, second))
        elif len(sorted_songs) == 1:
            answer.append(sorted_songs[0][0])

    return answer


def solution(genres, plays):
    answer = []

    gen_dict = {}
    plays_dict = {}

    for i in range(len(genres)):

        if genres[i] not in gen_dict:
            gen_dict[genres[i]] = plays[i]
        else:
            gen_dict[genres[i]] += plays[i]

        if genres[i] not in plays_dict:
            plays_dict[genres[i]] = [[plays[i], i]]
        else:
            plays_dict[genres[i]].append([plays[i], i])

    sorted_gen_dict = sorted(gen_dict.items(), key=lambda item: item[1], reverse=True)

    for key_value in sorted_gen_dict:

        plays_value = plays_dict[key_value[0]]
        new_value = sorted(plays_value, key=lambda x: x[0], reverse=True)[:2]

        for nv in new_value:
            answer.append(nv[1])

    return answer
