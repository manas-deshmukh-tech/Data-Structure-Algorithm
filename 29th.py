# Hospital Emergency Management using Priority Queue
class node:
    def __init__(self, pid, name, pr):
        self.pid = pid
        self.name = name
        self.priority = pr
        self.next = None

class priority_queue:
    def __init__(self):
        self.front = self.rear = None

    # 1. Add Patient
    def enqueue(self, newnode):

        # Case 1: Queue is empty
        if self.front is None:
            self.front = self.rear = newnode
            print("Patient added successfully!")
            return

        # Case 2: Insert at beginning
        if newnode.priority < self.front.priority:
            newnode.next = self.front
            self.front = newnode
            print("Patient added successfully!")
            return

        # Case 3: Insert at correct position
        temp = self.front

        while temp.next and temp.next.priority <= newnode.priority:
            temp = temp.next

        newnode.next = temp.next
        temp.next = newnode

        if newnode.next is None:
            self.rear = newnode

        print("Patient added successfully!")

    # 2. Display Next Patient
    def display_next(self):
        if self.front is None:
            print("Queue is empty!")
        else:
            print("Next Patient:")
            print("Patient ID:", self.front.pid)
            print("Patient Name:", self.front.name)
            print("Priority:", self.front.priority)

    # 3. Remove Patient
    def dequeue(self):
        if self.front is None:
            print("Queue is empty!")
        else:
            temp = self.front
            print("Patient treated:", temp.name)
            self.front = self.front.next

            if self.front is None:
                self.rear = None

    # 4. Display All Patients
    def display_all(self):
        if self.front is None:
            print("Queue is empty!")
        else:
            temp = self.front

            print("\nID\tName\tPriority")
            while temp:
                print(temp.pid, "\t", temp.name, "\t", temp.priority)
                temp = temp.next

pq = priority_queue()

while True:
    print("\n--- Hospital Emergency Management ---")
    print("1. Add Patient")
    print("2. Display Next Patient")
    print("3. Remove Patient")
    print("4. Display All Patients")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        pid = int(input("Enter Patient ID: "))
        name = input("Enter Patient Name: ")
        pr = int(input("Enter Priority (1-Critical, 2-Serious, 3-Normal): "))

        if pr >= 1 and pr <= 3:
            pq.enqueue(node(pid, name, pr))
        else:
            print("Invalid Priority!")

    elif choice == "2":
        pq.display_next()

    elif choice == "3":
        pq.dequeue()

    elif choice == "4":
        pq.display_all()

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")
