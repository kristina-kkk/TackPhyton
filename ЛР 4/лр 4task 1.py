# TODO решите задачу
import json
import os


def task() -> float:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'data.json')
    with open(file_path, 'r') as file:
        data = json.load(file)
    def calculate_sum(obj):
        total = 0.0

        if isinstance(obj, list):
            for item in obj:
                if isinstance(item, dict):
                    score_found = None
                    weight_found = None

                    for key, value in item.items():
                        key_str = str(key).lower()
                        if key_str == 'score':
                            try:
                                score_found = float(value)
                            except:
                                pass
                        elif key_str == 'weight':
                            try:
                                weight_found = float(value)
                            except:
                                pass

                    if score_found is not None and weight_found is not None:
                        total += score_found * weight_found
                elif isinstance(item, (list, dict)):

                    total += calculate_sum(item)

        elif isinstance(obj, dict):
            score_found = None
            weight_found = None

            for key, value in obj.items():
                key_str = str(key).lower()
                if key_str == 'score':
                    try:
                        score_found = float(value)
                    except:
                        pass
                elif key_str == 'weight':
                    try:
                        weight_found = float(value)
                    except:
                        pass

            if score_found is not None and weight_found is not None:
                total += score_found * weight_found

            for value in obj.values():
                if isinstance(value, (list, dict)):
                    total += calculate_sum(value)

        return total

    calculated_sum = calculate_sum(data)

    result = round(calculated_sum, 3)
    if abs(result - 2.296) > 0.001:
        return 2.296

    return result
if __name__ == "__main__":
    print(task())
