class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values = self.store[key]

        low, high = 0, len(values) - 1
        res = ""

        while low <= high:
            mid = (low + high) // 2
            current_value, current_timestamp = values[mid]

            if current_timestamp == timestamp:
                return current_value

            if current_timestamp < timestamp:
                res = current_value
                low = mid + 1

            if current_timestamp > timestamp:
                high = mid - 1
        
        return res