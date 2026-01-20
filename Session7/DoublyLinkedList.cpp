#include <iostream>
using namespace std;
struct Node {
    int data;
    Node* prev;
    Node* next;
};

Node* head = NULL;
void insert(int value) {
    Node* newNode = new Node();
    newNode->data = value;
    newNode->prev = NULL;
    newNode->next = NULL;

    if (head == NULL) {
        head = newNode;
        return;
    }

    Node* temp = head;
    while (temp->next != NULL) {
        temp = temp->next;
    }

    temp->next = newNode;
    newNode->prev = temp;
}
void deleteNode(int value) {
    if (head == NULL) {
        cout << "List is empty\n";
        return;
    }

    Node* temp = head;
    if (temp->data == value) {
        head = temp->next;
        if (head != NULL)
            head->prev = NULL;
        delete temp;
        return;
    }

    while (temp != NULL && temp->data != value) {
        temp = temp->next;
    }

    if (temp == NULL) {
        cout << "Value not found\n";
        return;
    }

    temp->prev->next = temp->next;
    if (temp->next != NULL)
        temp->next->prev = temp->prev;

    delete temp;
}
void displayForward() {
    Node* temp = head;
    cout << "Forward: ";
    while (temp != NULL) {
        cout << temp->data << " ";
        temp = temp->next;
    }
    cout << endl;
}
void displayBackward() {
    if (head == NULL) return;

    Node* temp = head;
    while (temp->next != NULL) {
        temp = temp->next;
    }

    cout << "Backward: ";
    while (temp != NULL) {
        cout << temp->data << " ";
        temp = temp->prev;
    }
    cout << endl;
}
int main() {
    insert(11);
    insert(12);
    insert(13);
    insert(14);
    displayForward();
    displayBackward();
    deleteNode(14);
    displayForward();
    deleteNode(11);
    displayForward();

    return 0;
}
