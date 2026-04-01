#include <iostream>

using namespace std;

class Node {
public:
    int data;
    Node* next;

    explicit Node(int value) : data(value), next(nullptr) {}
};

class CQueue {
private:
    Node* front;
    Node* rear;

public:
    CQueue() : front(nullptr), rear(nullptr) {}
    ~CQueue() {
        while (front != nullptr) {
            deleteFront();
        }
    }

    void insertion();
    void deletion();
    void display();
    void showTailNext();
    void deleteFront();
};

int main() {
    CQueue cqobj;
    int ch;

    do {
        cout << "\n\n\tMain Menu";
        cout << "\n##########################";
        cout << "\n1. Insert\n2. Delete\n3. Display\n4. Show tail->next\n5. Exit\n\nEnter Your Choice: ";
        cin >> ch;

        switch (ch) {
            case 1:
                cqobj.insertion();
                cqobj.display();
                break;
            case 2:
                cqobj.deletion();
                break;
            case 3:
                cqobj.display();
                break;
            case 4:
                cqobj.showTailNext();
                break;
            case 5:
                break;
            default:
                cout << "\n\nWrong Choice!!! Try Again.";
        }
    } while (ch != 5);

    return 0;
}

void CQueue::insertion() {
    int value;
    cout << "\nEnter the Element: ";
    cin >> value;

    Node* n = new Node(value);

    if (front == nullptr) {
        front = rear = n;
        rear->next = front;
    } else {
        rear->next = n;
        rear = n;
        rear->next = front;
    }
}

void CQueue::deleteFront() {
    if (front == nullptr) {
        return;
    }

    if (front == rear) {
        delete front;
        front = rear = nullptr;
    } else {
        Node* temp = front;
        front = front->next;
        rear->next = front;
        delete temp;
    }
}

void CQueue::deletion() {
    if (front == nullptr) {
        cout << "\nCircular Queue Empty!!!";
        return;
    }

    int x = front->data;
    deleteFront();
    cout << "\nElement " << x << " is Deleted";
    display();
}

void CQueue::display() {
    if (front == nullptr) {
        cout << "\n\nCircular Queue Empty!!!";
        return;
    }

    cout << "\n\nCircular Queue Elements are:\n\n";
    Node* temp = front;

    do {
        cout << temp->data << "  ";
        temp = temp->next;
    } while (temp != front);
}

void CQueue::showTailNext() {
    if (rear == nullptr) {
        cout << "Queue is empty" << endl;
        return;
    }

    cout << "Tail->Next->data: " << rear->next->data << endl;
}