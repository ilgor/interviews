class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}

class LinkedList {
  constructor() {
    this.head = null;
  }

  add(data) {
    let newNode = new Node(data);

    if (this.head == null) {
      this.head = newNode;
      return this;
    }

    let currNode = this.head;

    while (currNode.next != null) {
      currNode = currNode.next;
    }

    currNode.next = newNode;
    return this;
  }

  pop(data) {
    let currNode = this.head;

    if (currNode == null) {
      throw Error("List if Emprty");
    }

    while (currNode != null) {
      if (currNode.data == data) {
        currNode = currNode.next;
      }
      curr;
    }
  }

  toString() {
    let currNode = this.head;
    let result = "";

    while (currNode) {
      result += `${currNode.data}`;

      if (currNode.next != null) {
        result += " --> ";
      }

      currNode = currNode.next;
    }

    return result;
  }
}

let ll = new LinkedList();
console.log(ll.toString());

ll.add(1).add(2).add(3);
console.log(ll.toString());
