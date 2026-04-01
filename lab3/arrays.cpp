#include <iostream>
#include <string>
#include <chrono>

using namespace std;

class Example {
public:
    int number;
    string key;
    string* array;

    Example() : number(0), array(nullptr) {}
    ~Example();                      // destructor
    void set_array();
    void show_array();
    void add_s();
    void add_e();
    void search_element();
    void del_s();
    void del_e();
    void f();
    void f_3();
};

Example::~Example() {
    delete[] array;
    cout << "Array has deleted successfully ...";
}

void Example::set_array() {
    cout << "Type |array|: ";
    cin >> number;

    delete[] array;
    array = new string[number];

    for (int i = 0; i < number; i++) {
        cin >> array[i];
    }
}

void Example::show_array() {
    cout << "Array: ";
    for (int i = 0; i < number; i++) {
        cout << "  " << array[i] << "  ";
    }
    cout << endl;
}

void Example::add_s() {
    cout << "Type key: ";
    cin >> key;

    string* new_array = new string[number + 1];
    new_array[0] = key;

    for (int i = 0; i < number; i++) {
        new_array[i + 1] = array[i];
    }

    delete[] array;
    array = new_array;
    number++;
}

void Example::add_e() {
    cout << "Type key: ";
    cin >> key;

    string* new_array = new string[number + 1];

    for (int i = 0; i < number; i++) {
        new_array[i] = array[i];
    }
    new_array[number] = key;

    delete[] array;
    array = new_array;
    number++;
}

void Example::search_element() {
    cout << "Type key to look for: ";
    cin >> key;

    for (int i = 0; i < number; i++) {
        if (array[i] == key) {
            cout << "The element " << key << " has been found at index: " << i << endl;
            return;
        }
    }

    cout << "Not found" << endl;
}

void Example::del_s() {
    if (number <= 0) return;

    string* new_array = new string[number - 1];
    for (int i = 1; i < number; i++) {
        new_array[i - 1] = array[i];
    }

    delete[] array;
    array = new_array;
    number--;
}

void Example::del_e() {
    if (number <= 0) return;

    string* new_array = new string[number - 1];
    for (int i = 0; i < number - 1; i++) {
        new_array[i] = array[i];
    }

    delete[] array;
    array = new_array;
    number--;
}

void Example::f() {
    for (int i = 0; i < number; i++) {
        if (array[i].length() % 2 != 0 && array[i].length() >= 2) {
            array[i].erase(0, 1);
            array[i].erase(array[i].length() - 1, 1);
        }
    }
}

int main() {
    setlocale(0, "rus");

    auto start = chrono::high_resolution_clock::now();

    Example a;
    a.set_array();
    a.show_array();

    a.del_e();
    a.show_array();

    auto end = chrono::high_resolution_clock::now();
    auto duration = chrono::duration_cast<chrono::microseconds>(end - start);

    cout << "Execution time: " << duration.count() / 1000.0 << " ms" << endl;
    return 0;
}