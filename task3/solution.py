from typing import List, Dict


tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
                   'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
                   'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
     },
    {'intervals': {'lesson': [1594702800, 1594706400],
                   'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564,
                             1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096,
                             1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500,
                             1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
                   'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
     'answer': 3577
     },
    {'intervals': {'lesson': [1594692000, 1594695600],
                   'pupil': [1594692033, 1594696347],
                   'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
     'answer': 3565
     },
]


def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    """
    Объединяет пересекающиеся интервалы.

    :param intervals: Список интервалов [start, end].
    :return: Список объединённых интервалов.
    """
    if not intervals:
        return []
    intervals.sort()
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end:
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])
    return merged


def clip_intervals(intervals: List[int], lesson_start: int, lesson_end: int) -> List[List[int]]:
    """
    Обрезает интервалы по границам урока.

    :param intervals: Список таймстемпов (чётное количество, попарно [start, end]).
    :param lesson_start: Начало урока.
    :param lesson_end: Конец урока.
    :return: Список обрезанных интервалов [start, end].
    """
    result = []
    for i in range(0, len(intervals), 2):
        start = max(intervals[i], lesson_start)
        end = min(intervals[i + 1], lesson_end)
        if start < end:
            result.append([start, end])
    return result


def intersect_intervals(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
    """
    Находит пересечения двух списков интервалов.

    :param a: Первый список интервалов [start, end].
    :param b: Второй список интервалов [start, end].
    :return: Список пересечений [start, end].
    """
    i = j = 0
    result = []
    while i < len(a) and j < len(b):
        start = max(a[i][0], b[j][0])
        end = min(a[i][1], b[j][1])
        if start < end:
            result.append([start, end])
        if a[i][1] < b[j][1]:
            i += 1
        else:
            j += 1
    return result


def appearance(intervals: Dict[str, List[int]]) -> int:
    """
    Возвращает время общего присутствия ученика и учителя на уроке.

    :param intervals: Словарь с ключами 'lesson', 'pupil', 'tutor' и списками таймстемпов.
    :return: Общее время одновременного присутствия (в секундах).
    """
    lesson_start, lesson_end = intervals['lesson']
    pupil = clip_intervals(intervals['pupil'], lesson_start, lesson_end)
    tutor = clip_intervals(intervals['tutor'], lesson_start, lesson_end)
    pupil = merge_intervals(pupil)
    tutor = merge_intervals(tutor)
    both = intersect_intervals(pupil, tutor)
    return sum(end - start for start, end in both)


if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['intervals'])
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
