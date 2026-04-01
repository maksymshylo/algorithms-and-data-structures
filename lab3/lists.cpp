#include <iostream>
#include <string>
#include <chrono>

using namespace std;

struct Node {
    string key;
    Node* Next;
    Node* Prev;

    Node(const string& value) : key(value), Next(nullptr), Prev(nullptr) {}
};

class List {
    Node* Tail;
    Node* Head;

public:
    List() : Head(nullptr), Tail(nullptr) {}
    ~List();

    void show_s();
    void show_e();
    void add_s(string key);
    void add_e(string key);
    void type_list();
    void del_list();
    Node* search_element(string key);
    void del_tail();
};

List::~List() {
    del_list();
}

void List::show_s() {
    Node* temp = Head;
    cout << "Your list now is (from start): " << endl;

    while (temp != nullptr) {
        cout << temp->key << " ";
        temp = temp->Next;
    }
    cout << endl;
}

void List::show_e() {
    Node* temp = Tail;
    cout << "Your list now is (from end): " << endl;

    while (temp != nullptr) {
        cout << temp->key << " ";
        temp = temp->Prev;
    }
    cout << endl;
}

void List::add_s(string key) {
    Node* temp = new Node(key);
    temp->Next = Head;

    if (Head != nullptr) {
        Head->Prev = temp;
    } else {
        Tail = temp;
    }

    Head = temp;
}

void List::add_e(string key) {
    Node* temp = new Node(key);
    temp->Prev = Tail;

    if (Tail != nullptr) {
        Tail->Next = temp;
    } else {
        Head = temp;
    }

    Tail = temp;
}

void List::type_list() {
    cout << "Type count of elements: ";
    int c;
    cin >> c;

    for (int i = 0; i < c; i++) {
        string s;
        cin >> s;
        add_e(s);
    }
}

void List::del_list() {
    Node* temp = Head;
    while (temp != nullptr) {
        Node* next = temp->Next;
        delete temp;
        temp = next;
    }
    Head = nullptr;
    Tail = nullptr;
}

Node* List::search_element(string key) {
    Node* temp = Head;
    while (temp != nullptr && temp->key != key) {
        temp = temp->Next;
    }
    return temp;
}

void List::del_tail() {
    if (Tail == nullptr) return;

    Node* temp = Tail;
    Tail = Tail->Prev;

    if (Tail != nullptr) {
        Tail->Next = nullptr;
    } else {
        Head = nullptr;
    }

    delete temp;
}

int main() {
    setlocale(0, "rus");

    auto start = chrono::high_resolution_clock::now();

    List a;
    a.type_list();

    a.add_s("first");
    a.add_e("last");

    a.show_s();
    a.show_e();

    Node* found = a.search_element("l");
    if (found != nullptr) {
        cout << "Found: " << found->key << endl;
    } else {
        cout << "Not found" << endl;
    }

    a.del_list();

    auto end = chrono::high_resolution_clock::now();
    auto duration = chrono::duration_cast<chrono::microseconds>(end - start);

    cout << "Execution time: " << duration.count() / 1000.0 << " ms" << endl;
    return 0;
}