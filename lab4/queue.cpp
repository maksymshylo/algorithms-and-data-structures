#include <iostream>
#include <cstdlib>
#include <ctime>
#include <chrono>

using namespace std;

struct Node {
    int data;
    Node* next;
    Node(int value = 0) : data(value), next(nullptr) {}
};

struct Queue {
    int size;
    Node* first;
    Node* last;
};

void create(Queue* Q);
bool isfull(Queue* Q);
int first(Queue* Q);
void addelement(Queue* Q, int value);
void Delete(Queue* Q);
int size(Queue* Q);
void showq(Queue* Q);
void initialq(Queue* Q, int n);


void create(Queue* Q) {
    Q->first = new Node();
    Q->last = Q->first;
    Q->size = 0;
}

bool isfull(Queue* Q) {
    return Q->first == Q->last;
}

int first(Queue* Q) {
    if (Q->first == Q->last || Q->first->next == nullptr) {
        return -1;
    }
    return Q->first->next->data;
}

void addelement(Queue* Q, int value) {
    Q->last->next = new Node(value);
    Q->last = Q->last->next;
    Q->size++;
    cout << "element added to queue" << endl;
}

void Delete(Queue* Q) {
    if (Q->first == Q->last || Q->first->next == nullptr) {
        cout << "queue is empty" << endl;
        return;
    }

    Node* temp = Q->first->next;
    Q->first->next = temp->next;

    if (temp == Q->last) {
        Q->last = Q->first;
    }

    delete temp;
    Q->size--;
    cout << "delete from queue" << endl;
}

int size(Queue* Q) {
    return Q->size;
}

void initialq(Queue* Q, int n) {
    srand(static_cast<unsigned>(time(nullptr)));
    for (int i = 0; i < n; i++) {
        addelement(Q, (rand() % 100) + 1);
    }
}

void showq(Queue* Q) {
    Node* temp = Q->first->next;
    cout << "Queue:" << endl;

    while (temp != nullptr) {
        cout << temp->data << " ";
        temp = temp->next;
    }
    cout << endl;
}

int main() {
    auto start = chrono::high_resolution_clock::now();

    Queue Q;
    create(&Q);
    initialq(&Q, 4);
    addelement(&Q, 8);
    showq(&Q);

    if (Q.size > 0) {
        cout << first(&Q) << endl;
    }

    Delete(&Q);
    showq(&Q);

    auto end = chrono::high_resolution_clock::now();
    auto duration = chrono::duration_cast<chrono::microseconds>(end - start);
    cout << "Execution time: " << duration.count() / 1000.0 << " ms" << endl;

    return 0;
}
