class CowMilkRecorder:
    def __init__(self):
        self.herd_size = 0
        self.cow_records = {}

    def record_yield(self, cow_id, yield_amount):
        if cow_id not in self.cow_records:
            self.cow_records[cow_id] = []
        self.cow_records[cow_id].append(yield_amount)

    def calculate_statistics(self):
        total_volume = 0
        total_cows = len(self.cow_records) 

        for cow_id, yields in self.cow_records.items():
            total_volume += sum(yields)

        average_yield = total_volume / total_cows
        return total_volume, average_yield

    def identify_most_productive_cow(self):
        max_yield = 0
        most_productive_cow_id = None

        for cow_id, yields in self.cow_records.items():
            if sum(yields) > max_yield:
                max_yield = sum(yields)
                most_productive_cow_id = cow_id

        return most_productive_cow_id, max_yield

    def identify_low_yield_cows(self):
        low_yield_cows = []

        for cow_id, yields in self.cow_records.items():
            low_days = sum(1 for yield_amount in yields if yield_amount < 12)
            if low_days >= 4:
                low_yield_cows.append(cow_id)

        return low_yield_cows


def main():
    recorder = CowMilkRecorder()

    # Task 1: Record the yield
    recorder.herd_size = int(input("Enter the size of the herd: "))

    for _ in range(recorder.herd_size):
        cow_id = input("Enter cow's 3-digit identity code: ")
        for _ in range(14):  # Twice a day for 7 days
            yield_amount = float(input(f"Enter yield for cow {cow_id}: "))
            recorder.record_yield(cow_id, yield_amount)

    # Task 2: Calculate statistics
    total_volume, average_yield = recorder.calculate_statistics()
    print(f"Total weekly volume of milk: {round(total_volume)} litres")
    print(f"Average yield per cow: {round(average_yield)} litres")

    # Task 3: Identify the most productive cow and low yield cows
    most_productive_cow_id, max_yield = recorder.identify_most_productive_cow()
    print(f"Most productive cow: {most_productive_cow_id} with {max_yield} litres")

    low_yield_cows = recorder.identify_low_yield_cows()
    if low_yield_cows:
        print("Cows with low yield (less than 12 litres for 4 or more days):", low_yield_cows)
    else:
        print("No cows with consistently low yield found.")


if __name__ == "__main__":
    main()
